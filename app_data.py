import requests as rq
import json
from flask import jsonify

def getChatStatus(fenixToken):
    url = "https://www3.directtalk.com.br/adminuiservices/api/report/chat/OperatorMonitoring"
    payload = "[\"-1\"]"
    headers = {
      'Accept': 'application/json, text/plain, /',
      'Authorization': 'DT-Fenix-Token ' + fenixToken,
      'Content-Type': 'application/json;charset=UTF-8'
      }
    response = rq.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
         return {"message": "Ocorreu um erro.", "status": response.status_code}
    response = response.json()
    return {"data": response, "status": 200}


def getFenixToken():
    fenixTokenHeaders = {
         'Accept': 'application/json, text/plain, */*',
         'Connection': 'keep-alive',
         'Content-Type': 'application/json; charset=UTF-8',
         'Authorization': 'Basic ZHRzMXdpbGxpYW0ud2VpZGdlbmFuZDozNDY2MTE3V3c='
         }
    fenix_response = rq.request("POST", "https://www3.directtalk.com.br/adminuiservices/api/Login", headers=fenixTokenHeaders)
    fenix_response = fenix_response.json()
    return fenix_response['token']