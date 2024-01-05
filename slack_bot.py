from slack_sdk import WebClient
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

client = WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#slackbottest', text="Hello, world!")


if __name__ == "__main__":
    app.run(debug=True)
