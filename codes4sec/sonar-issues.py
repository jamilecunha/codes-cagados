# Exportar Vulnerabilidades do Sonar via CSV
 
import csv
import json
from requests import Session

MAX_PAGE_SIZE = 500

# Passo 1
def sonarAuth(api):
      sonarToken = '' # Insira o token entre as aspas simples
      try:
         with Session() as session:
               session.auth = sonarToken, ''
         return json.loads(session.get(url=f'https://sonar.organization-domain/api/{api}').content)
      except Exception as e:
         raise(e)

# Passo 2
def CSVJson(issueJson, fileName):
    csvFile = open(file=fileName, mode='w', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['KEY', 'TYPE', 'RULE', 'SEVERITY', 'STATUS', 'MESSAGE', 'COMPONENT', 'LINE', 'CREATION DATE'])
    for value in issueJson['issues']:
        try:
            csvWriter.writerow([value['key'],
                                value['type'],
                                value['rule'],
                                value['severity'],
                                value['status'],
                                value['message'],
                                value['component'],
                                value['line'],
                                value['creationDate']])
        except KeyError as e:
            if str(e) == '\'line\'':
                csvWriter.writerow([value['key'],
                                    value['type'],
                                    value['rule'],
                                    value['severity'],
                                    value['status'],
                                    value['message'],
                                    value['component'],
                                    0,
                                    value['creationDate']])
            else:
                print('KeyError :' + str(e))

# Passo 3
if __name__ == "__main__":
    sonarQubeURL = 'https://sonar.organization-domain'
    projectKey = input('Project: ')
    requestIssueURL = sonarQubeURL + '/api/issues/search?componentKeys=' + projectKey + '&ps=' + str(MAX_PAGE_SIZE)
    issueJson = sonarAuth('issues/search?componentKeys=' + projectKey + '&ps=' + str(MAX_PAGE_SIZE))
    CSVJson(issueJson, projectKey + '.csv')