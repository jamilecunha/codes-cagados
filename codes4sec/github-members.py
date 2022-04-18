# Listar membros da organização

from github import Github as gh
from os import environ
from github import GithubException
class GitHubMembers(gh):

    # Passo 1
    def __init__(self):
        self.GH_TOKEN = environ['RD_OPTION_GITHUB_TOKEN']
        self.GH_ACCOUNT = gh(self.GH_TOKEN, per_page=1000)
        self.GH_ORG = self.GH_ACCOUNT.get_organization('organization-name')  
        self.GH_RATE_LIMIT = self.GH_ACCOUNT.get_rate_limit()
        try:
            self.get_org_repos_infos()
        except GithubException as error:
            raise error

    # Passo 2        
    def get_org_repos_infos(self):
        print('NOME | LOGIN | EMAIL')
        try:
            for member in self.GH_ORG.get_members():
                print(f'{member.name} | {member.login} | {member.email}')
        except GithubException as error:
            raise error
GitHubMembers()