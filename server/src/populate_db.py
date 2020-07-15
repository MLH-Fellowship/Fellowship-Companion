####################################################
####################################################
#                                                  #
# Note : Do not use this script for now            #
#                                                  #
####################################################
####################################################

from github import Github
import os

from timeline.models import (
    Repository,
    PullRequest,
    Issue,
    Event,
)

if __name__ == '__main__':
    filepath = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'env', 'credentials.txt'
    )
    username = ""
    password = ""
    with open(filepath) as file:
        lines = file.readlines()
        username = lines[0][:-1]
        password = lines[1][:-1]

g = Github(username, password)
org = g.get_organization('MLH-Fellowship')


def get_repos():
    for repo in org.get_repos(type='forks', sort='created'):
        db_repo = Repository(
            id=repo.parent.id,
            name=repo.parent.name,
            fullname=repo.parent.full_name,
            description=repo.parent.description,
            url=repo.parent.url,
            contributed_loc=0,
            created_at=repo.parent.created_at,
        )
        db_repo.save()
