import os

from pyrogram import Client

Bot = Client(

    "",

    bot_token=os.environ.get("BOT_TOKEN"),

    api_id=int(os.environ.get("API_ID")),

    api_hash=os.environ.get("API_HASH")

)

Bot.run()
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from RUD3US'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
