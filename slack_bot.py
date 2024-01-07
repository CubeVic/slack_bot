import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from blocks import BLOCK, BLOCK_MODAL_VIEW

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = App(token=os.environ['SLACK_BOT_TOKEN'],
          signing_secret=os.environ['SLACK_SIGNING_SECRET'])

@app.message("hello")
def message_hello(message, say):
    user = message['user']

    say(
        blocks=BLOCK,
        text=f"Hey,<@{user}> \n"
    )

@app.action("button-click")
def action_button_click(body, ack, say):
    ack()
    # print(body)
    block_id = body['message']['blocks'][1]['block_id']
    content = body['state']['values'][block_id]['plain_text_input-action']['value']
    say(f"<@{body['user']['id']}> clicked the button, and the value: {content}")


# Define the listener for the action
@app.action('open_modal')
def open_modal(ack, body, client):
    # Acknowledge the action
    ack()

    # Open the modal
    client.views_open(
        trigger_id=body["trigger_id"],
        view=BLOCK_MODAL_VIEW
    )


if __name__ == "__main__":
    SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
