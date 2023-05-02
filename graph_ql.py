# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.

import requests
import pprint
#from queries import query
from constants import headers_graphql
from constants import graphql_url
from constants import jira_url
from arguments import jira_project_key
from constants import headers_jira
from arguments import vulnerabilities_issue_created_track_path
import json
import collections

# A simple function to use requests.post to make the API call. Note the json= section.


has_next_page = True

cursor_value = ""

print("Has next page value is {}".format(has_next_page))

while has_next_page is True:
    query = """{organization
                  (login: "yahoo")
                     {repositories(first:100 after:"%s")
                       { edges
                         { node
                           {owner
                            {  id  }
                              name
                              vulnerabilityAlerts ( first: 100 )
                                {  edges
                                  {  node
                                    {  affectedRange
                                        dismissReason
                                        dismissedAt
                                        externalIdentifier 
                                        externalReference 
                                        fixedIn 
                                        id 
                                        packageName 
                                    }
                                  } 
                                } 
                            }

                             cursor 
                         }
                    pageInfo 
                    {
                     endCursor
                     hasNextPage
                    }    
                 } 
             }
        }""" % cursor_value

    print(query)


    def run_query():
            request = requests.post(graphql_url, json={'query': query}, headers=headers_graphql)
            if request.status_code == 200:
                res = request.json()
                global cursor_value
                cursor_value = res['data']['organization']['repositories']['pageInfo']['endCursor']
                print(cursor_value)
                global has_next_page
                has_next_page = res['data']['organization']['repositories']['pageInfo']['hasNextPage']
                print(has_next_page)
            else:
                raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
            return request.json()


    result = run_query() # Execute the query
    #print(result['data']['organization']['repositories']['pageInfo']['endCursor'])


    def get_vulnerabilities():
        vulnerabilities_list = {}

        for edges in result['data']['organization']['repositories']['edges']:
            for vulIssues in edges['node']['vulnerabilityAlerts']['edges']:
                vulnerable_repo_name = edges['node']['name']
                if vulnerable_repo_name not in vulnerabilities_list:
                    vulnerabilities_list[vulnerable_repo_name] = set()
                vulnerabilities = vulIssues['node']['packageName']
                if vulIssues['node']['dismissedAt'] is None:
                    vulnerabilities_list[vulnerable_repo_name].add(vulnerabilities)
        return vulnerabilities_list


    #ordered_vulnerabilities_list = collections.OrderedDict(get_vulnerabilities())
    ordered_vulnerabilities_list = collections.OrderedDict(get_vulnerabilities())

    res = ordered_vulnerabilities_list
    vulnerabilities_keys_list = list(res.keys())
    vulnerabilities_values_list = list(res.values())

    final_vulnerabilities_list = []
    final_corresponding_repos_list = []

    for i in vulnerabilities_values_list:
        if i != set():
            final_vulnerabilities_list.append(i)

    ptr = 0

    for i in vulnerabilities_values_list:
        if i != set():
            final_corresponding_repos_list.append(vulnerabilities_keys_list[ptr])
            ptr=ptr+1

    print(final_corresponding_repos_list)
    print(final_vulnerabilities_list)

    vulnerabilities_issues_created_keys_list = []
    vulnerabilities_issues_created_values_list = []


    def create_jira_issue():
        for i in range(0,len(vulnerabilities_keys_list)):

            if vulnerabilities_keys_list[i] not in vulnerabilities_issues_created_keys_list and \
                    vulnerabilities_values_list[i] not in vulnerabilities_issues_created_values_list and \
                    vulnerabilities_keys_list[i] not in open(vulnerabilities_issue_created_track_path).read():

                issue_body = {"fields": {
                    "project":
                        {
                            "key": "%s" % (jira_project_key)
                        },
                    "summary": "Security vulnerability issues found in project %s" % (vulnerabilities_keys_list[i]),
                    "description": "Following are the list of vulnerabilities found for the above project %s" %
                                   (vulnerabilities_values_list[i]),
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

                f = open(vulnerabilities_issue_created_track_path, "w")
                f.write(tracked_repos)

                if request.status_code == 201:
                    print(request.json())

                else:
                    raise Exception("Issue failed to be created by returning code of {}. {}".format(request.status_code,
                                                                                                  request.json()))

                if len(vulnerabilities_issues_created_keys_list) == len(vulnerabilities_keys_list) and\
                        len(vulnerabilities_issues_created_values_list) == len(vulnerabilities_values_list):
                    return True
                else:
                    continue


    ans = create_jira_issue()
    print(len(vulnerabilities_issues_created_keys_list))
