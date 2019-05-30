# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.

import json
import collections

import requests

from .arguments import parse_arguments
from .queries import query
from .constants import headers_graphql, graphql_url, jira_url, headers_jira


args = parse_arguments()


def run_query(query):
    """A simple function to use requests.post to make the API call. Note the json= section."""
    request = requests.post(graphql_url, json={'query': query}, headers=headers_graphql)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


result = run_query(query)  # Execute the query


def get_vulnerabilities():
    vulnerabilities_list = {}

    for edges in result['data']['organization']['repositories']['edges']:
        for vulIssues in edges['node']['vulnerabilityAlerts']['edges']:
            vulnerable_repo_name = edges['node']['name']
            if vulnerable_repo_name not in vulnerabilities_list:
                vulnerabilities_list[vulnerable_repo_name] = set()
            vulnerabilities = vulIssues['node']['packageName']
            vulnerabilities_list[vulnerable_repo_name].add(vulnerabilities)
    return vulnerabilities_list


ordered_vulnerabilities_list = collections.OrderedDict(get_vulnerabilities())
print(ordered_vulnerabilities_list)

res = ordered_vulnerabilities_list
vulnerabilities_keys_list = list(res.keys())
vulnerabilities_values_list = list(res.values())


vulnerabilities_issues_created_keys_list = []
vulnerabilities_issues_created_values_list = []


def create_jira_issue():
    for i in range(0, len(vulnerabilities_keys_list)):

        if vulnerabilities_keys_list[i] not in vulnerabilities_issues_created_keys_list and \
                vulnerabilities_values_list[i] not in vulnerabilities_issues_created_values_list and \
                vulnerabilities_keys_list[i] not in open(args.vulnerabilities_issue_created_track_path).read():

            issue_body = {
                "fields": {
                    "project":{
                        "key": "%s" % (args.jira_project_key)
                    },
                    "summary": "Security vulnerability issues found in project %s" % (vulnerabilities_keys_list[i]),
                    "description": "Following are the list of vulnerabilities found for the above project %s" % (vulnerabilities_values_list[i]),
                    "issuetype": {
                        "name": "Defect"
                    }
                }
            }

            issue_body_data = json.dumps(issue_body)
            request = requests.post(jira_url, data=issue_body_data, headers=headers_jira)

            vulnerabilities_issues_created_keys_list.append(vulnerabilities_keys_list[i])
            vulnerabilities_issues_created_values_list.append(vulnerabilities_values_list[i])

            tracked_repos = '\n'.join(vulnerabilities_issues_created_keys_list)

            f = open(args.vulnerabilities_issue_created_track_path, "w")
            f.write(tracked_repos)

            if request.status_code == 201:
                print(request.json())

            else:
                raise Exception("Issue failed to be created by returning code of {}. {}".format(request.status_code, request.json()))

            if len(vulnerabilities_issues_created_keys_list) == len(vulnerabilities_keys_list) and \
                    len(vulnerabilities_issues_created_values_list) == len(vulnerabilities_values_list):
                return True
            else:
                continue


ans = create_jira_issue()
print(len(vulnerabilities_issues_created_keys_list))
