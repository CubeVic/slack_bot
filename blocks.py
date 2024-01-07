BLOCK = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is the response *To your Hello*"
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "How can I call you",
                    "emoji": True
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Click Me",
                            "emoji": True
                        },
                        "value": "click_me_123",
                        "action_id": "button-click"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "open modal",
                            "emoji": True
                        },
                        "value": "click_me_1234",
                        "action_id": "open_modal"
                    }
                ]
            }
]

BLOCK_MODAL_VIEW = {
    "type": "modal",
    "callback_id": "modal-identifier",
    "title": {
        "type": "plain_text",
        "text": "My Modal",
    },
    "blocks": [
        {
            "type": "section",
            "block_id": "section-identifier",
            "text": {
                "type": "mrkdwn",
                "text": "This is a modal!",
            },
        },
    ],
    "close": {
        "type": "plain_text",
        "text": "Close",
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
    },
}