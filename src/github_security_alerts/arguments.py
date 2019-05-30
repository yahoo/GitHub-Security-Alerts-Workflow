# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
import argparse
import sys


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments
    """
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('graph_ql_authorization')
    parser.add_argument('jira_authorization')
    parser.add_argument('jira_url')
    parser.add_argument('jira_project_key')
    parser.add_argument('vulnerabilities_issue_created_track_path')
    return parser.parse_args()


if __name__ == '__main__':
    print(parse_arguments())
