# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.

from arguments import jira_url
from arguments import jira_authorization
from arguments import graphql_authorization



headers_graphql = {
 'Accept': 'application/vnd.github.vixen-preview',
 'Authorization': 'bearer %s' % (graphql_authorization),
}

headers_jira = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic %s' %(jira_authorization)
}

graphql_url = "https://api.github.com/graphql"

jira_url = "%s" %(jira_url)


