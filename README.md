
# GitHub Security Alerts Workflow

This script is for teams that want to leverage GitHub Security Alerts into their workflow. It currently supports creating Jira tickets from the GitHub GraphQL API for security alerts. 

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Background

This purpose of this project is to manage security vulnerabilities for open source projects using GitHub’s security alerts at scale.

## Install

This script requires Python 3.5 or newer to run, so ensure you have this installed first. 
Installation of this script is as simple as the following:

```console
pip install https://github.com/yahoo/GitHub-Security-Alerts-Workflow/archive/master.tar.gz
```

## Usage

Use the following command to run this script:

`graph_ql.py graph_ql_authorization_key jira_authorization_key jira_url jira_project_key vulnerabilities_issue_created_track_path`

* graph_ql_authorization_key - A GitHub GraphQL access token that has the ability to view security alerts for the chosen repo.
* jira_authorization_key - An authorization key for your Jira instance with the ability to create and modify tickets.
* jira_url - The endpoint for your Jira instance's issue API, e.g. https://jira.xyz.com/rest/api/2/issue/
* jira_project_key - The identifier key for the Jira project you want to create issues for.
* vulnerabilities_issue_created_track_path - Issue file to create

## Contribute

Please refer to [the contributing.md file](Contributing.md) for information about how to get involved. We welcome issues, questions, and pull requests. Pull Requests are welcome.

## Maintainers
Manikandan Subramaniam: manikandan.subramaniam@verizonmedia.com
Ashley Wolf: awolf@verizonmedia.com

## License

This project is licensed under the terms of the [Apache 2.0](LICENSE-Apache-2.0) open source license. Please refer to [LICENSE](LICENSE) for the full terms.
