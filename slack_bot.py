import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = App(token=os.environ['SLACK_BOT_TOKEN'])


@app.message("hello")
def message_hello(message, say):
    user = message['user']
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey,<@{user}> \n"},
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "action_id": "button-click"
                }
            }
        ],
        text=f"Hey,<@{user}> \n"
    )

@app.action("button-click")
def action_button_click(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
