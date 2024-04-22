from github import Github
import os

# Get the GitHub token from the environment variables
github_token = os.getenv('GITHUB_TOKEN')

# Initialize the GitHub instance
g = Github(github_token)

# Get the event payload
event_payload = os.getenv('GITHUB_EVENT_PATH')

# Load the event payload
with open(event_payload, 'r') as file:
    payload = json.load(file)

# Extract necessary information from the payload
repository = payload['repository']['full_name']
issue_number = payload['issue']['number']
comment_body = payload['comment']['body']

# Check if the comment contains "/hello"
if "/hello" in comment_body:
    # Get the repository
    repo = g.get_repo(repository)
    
    # Create a comment
    repo.get_issue(issue_number).create_comment("Hello!")
