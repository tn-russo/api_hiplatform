from flask import Flask, request
import time
import json
import app_data as function

app = Flask(__name__)

fenixToken = ""
fenixToken_createdAt = None

@app.route('/')
def home():
  return "OK"

# Rota exclusiva para o Check Agents do Squad Premium
@app.route('/checkagents')
def CheckAgents():
   global fenixToken
   global fenixToken_createdAt

   if fenixToken and fenixToken_createdAt:
      current_datetime = time.time()
      time_elapsed = current_datetime - fenixToken_createdAt
      if time_elapsed < 36000:
        print("Reutilizou mesmo token.")
        chat_status = function.getChatStatus(fenixToken)
      else:
        print("Token expirado e criou um novo.")
        fenixToken = function.getFenixToken()
        fenixToken_createdAt = current_datetime
        chat_status = function.getChatStatus(fenixToken)
   else:
     print("Token não existe. Criando um novo...")
     fenixToken = function.getFenixToken()
     fenixToken_createdAt = time.time()
     chat_status = function.getChatStatus(fenixToken)
   print(fenixToken)
   return chat_status['data']

# Rota exclusiva para capturar webhooks
@app.route('/webhookevent', methods=['POST'])
def GetContactStatus():
  data = request.json
  print(data)
  return "OK"
  

if __name__ == '__main__': 
   app.run('0.0.0.0')