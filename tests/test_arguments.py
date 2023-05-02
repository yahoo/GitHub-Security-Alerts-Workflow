from unittest import TestCase
import sys
from github_security_alerts.arguments import parse_arguments


class ArgumentsTestCase(TestCase):
    # Have setup and teardown save and restore the sys.argv value so the
    # tests can freely modify it.
    def setUp(self):
        self._orig_argv = sys.argv

    def tearDown(self):
        sys.argv = self._orig_argv

    def test__all_arguments_passed(self):
        sys.argv = ['graph_ql.py', 'graph_ql_authorization_key',  'jira_authorization_key', 'jira_url', 'jira_project_key', 'vulnerabilities_issue_created_track_path']
        args = parse_arguments()
        print(args)
        self.assertEqual(args.graphql_authorization, 'graph_ql_authorization_key')
        self.assertEqual(args.jira_authorization, 'jira_authorization_key')
        self.assertEqual(args.jira_url, 'jira_url')
        self.assertEqual(args.jira_project_key, 'jira_project_key')
