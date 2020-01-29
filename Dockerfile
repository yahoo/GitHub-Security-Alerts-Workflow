FROM python:3

ARG GRAPH_QL_KEY
ARG JIRA_AUTH_KEY
ARG JIRA_URL
ARG JIRA_PROJECT_KEY
ENV ISSUE_LOG=./vulnerabilities_issues_created_log

COPY . /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "graph_ql.py", "${GRAPH_QL_KEY}", "${JIRA_AUTH_KEY}", "${JIRA_URL}", "${JIRA_PROJECT_KEY}", "${ISSUE_LOG}" ]