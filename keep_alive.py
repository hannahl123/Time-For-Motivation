from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "To add the bot to your server, use this link: https://discord.com/api/oauth2/authorize?client_id=937347049979006986&permissions=8&scope=bot"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()