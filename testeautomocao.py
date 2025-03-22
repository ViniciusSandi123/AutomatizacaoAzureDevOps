import os
import requests
import json
from requests.auth import HTTPBasicAuth

AZURE_ORG = "viniciussandi98"
AZURE_PROJECT = "TesteAutomoção" 
AZURE_PAT = os.getenv("AZURE_PAT")

if AZURE_PAT is None:
    print("Erro: Token não encontrado.")
    exit(1)


url = f"https://dev.azure.com/{AZURE_ORG}/{AZURE_PROJECT}/_apis/wit/workitems/$Issue?api-version=6.0"

headers = {
    "Content-Type": "application/json-patch+json"
}

payload = [
    {"op": "add", "path": "/fields/System.Title", "value": "Issue Criado via API"},
    {"op": "add", "path": "/fields/System.Description", "value": "Este é um Issue criado automaticamente usando Python."},
    {"op": "add", "path": "/fields/System.WorkItemType", "value": "Issue"},
    {"op": "add", "path": "/fields/System.IterationPath", "value": "TesteAutomoção\\Sprint 1\\Teste"}
]
auth = HTTPBasicAuth("", AZURE_PAT)

try:

    response = requests.post(url, headers=headers, auth=auth, json=payload)
    response.raise_for_status()
    print("Work Item criado com sucesso!")
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.HTTPError as err:
    print("Erro HTTP:", err)
    print("Resposta do Servidor:", response.text)
except requests.exceptions.RequestException as err:
    print("Erro na Requisição:", err)
