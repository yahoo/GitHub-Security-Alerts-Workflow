# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.

from .arguments import parse_arguments


args = parse_arguments()
headers_graphql = {
    'Accept': 'application/vnd.github.vixen-preview',
    'Authorization': 'bearer %s' % (args.graphql_authorization),
}

headers_jira = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic %s' % (args.jira_authorization)
}

graphql_url = "https://api.github.com/graphql"

jira_url = parse_arguments().jira_url
