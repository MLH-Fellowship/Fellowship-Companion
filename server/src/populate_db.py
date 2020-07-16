####################################################
####################################################
#                                                  #
# Note : Do not use this script for now            #
#                                                  #
####################################################
####################################################

from datetime import datetime, timedelta
from github import Github
from groups.models import Team, GithubUser
import os

from timeline.models import (
    Repository,
    PullRequest,
    Issue,
    Event,
)


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


def get_teams():
    for team in org.get_teams():
        db_team = Team(
            id=team.id,
            name=team.name,
            avatar_url=f"https://avatars1.githubusercontent.com/t/{team.id}",
            description=team.description,
        )
        db_team.save()


def get_users():
    for user in org.get_members():
        db_user = GithubUser(
            id=user.id,
            name=user.name,
            bio=user.bio,
            github_handle=user.login,
            avatar_url=user.avatar_url,
            location=user.location,
            followers=user.followers,
            followers_url=f"https://github.com/{user.login}?tab=followers",
            following=user.following,
            following_url=f"https://github.com/{user.login}?tab=following",
        )
        db_user.save()


def setup_teams():
    for db_team in Team.objects.all():
        github_team = org.get_team(db_team.id)
        for member in github_team.get_members():
            db_user = GithubUser.objects.get(github_handle__iexact=member.login)
            db_user.teams.add(db_team)
            db_user.save()


def get_prs():
    for db_repo in Repository.objects.all():
        print("Checking ", db_repo.fullname, "...")
        gh_repo = g.get_repo(db_repo.fullname)
        gh_prs = gh_repo.get_pulls(state='all')
        if gh_prs.totalCount > 100:
            last = 100
        else:
            last = gh_prs.totalCount
        for gh_pr in gh_prs[:last]:
            db_user = GithubUser.objects.filter(github_handle__iexact=gh_pr.user.login)
            if db_user.count() > 0:
                print("    adding ", gh_pr.title, "...")
                db_user = db_user.first()
                db_pr = PullRequest(
                    id=gh_pr.id,
                    number=gh_pr.number,
                    title=gh_pr.title,
                    description=gh_pr.body,
                    created_at=gh_pr.created_at,
                    closed_at=gh_pr.closed_at,
                    state=gh_pr.state,
                    url=gh_pr.html_url,
                    additions=gh_pr.additions,
                    deletions=gh_pr.deletions,
                    user=db_user,
                    repo=db_repo,
                    merged=gh_pr.merged,
                )
                db_pr.save()


def get_issues():
    for db_repo in Repository.objects.all():
        print("Checking ", db_repo.fullname, "...")
        gh_repo = g.get_repo(db_repo.fullname)
        for gh_issue in gh_repo.get_issues(state='all', since=datetime(2020, 6, 1)):
            if Issue.objects.filter(id=gh_issue.id).count() > 0:
                continue
            db_user = GithubUser.objects.filter(github_handle__iexact=gh_issue.user.login)
            db_pr = None
            if gh_issue.pull_request is not None:
                db_pr = PullRequest.objects.filter(
                    url__iexact=gh_issue.pull_request.raw_data["html_url"]
                )
                if db_pr.count() > 0:
                    db_pr = db_pr.first()
                else:
                    db_pr = None

            if db_user.count() > 0:
                db_user = db_user.first()
            else:
                db_user = None

            if (db_pr is None) and (db_user is None):
                continue

            print("Inserting ", gh_issue.html_url)
            db_issue = Issue(
                id=gh_issue.id,
                number=gh_issue.number,
                title=gh_issue.title,
                description=gh_issue.body,
                created_at=gh_issue.created_at,
                closed_at=gh_issue.closed_at,
                state=gh_issue.state,
                url=gh_issue.html_url,
                related_pr=db_pr,
                user=db_user,
                repo=db_repo,
            )
            db_issue.save()


username = ""
password = ""
filepath = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'env', 'credentials.txt'
)
with open(filepath) as file:
    lines = file.readlines()
    username = lines[0][:-1]
    password = lines[1][:-1]

g = Github(username, password)
org = g.get_organization('MLH-Fellowship')
