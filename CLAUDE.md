# CLAUDE.md - AI Assistant Guide for Slack Bot

This document provides context for AI assistants working with this codebase.

## Project Overview

**Name:** Slack Bot
**Version:** 0.1.0
**Author:** CubeVic (victoraguirre.f@gmail.com)
**Description:** A Python-based Slack bot built using the Slack Bolt framework with Socket Mode integration.

The bot responds to messages and provides interactive UI elements including buttons and modal dialogs.

## Project Structure

```
slack_bot/
├── .github/
│   └── workflows/
│       ├── auto_assign.yml       # Auto-assigns PR authors
│       └── quality.yaml          # Pre-commit quality checks CI
├── slack_bot.py                  # Main application entry point
├── blocks.py                     # Slack Block Kit UI definitions
├── pyproject.toml                # Poetry project configuration
├── poetry.lock                   # Dependency lock file
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── .gitignore                    # Git ignore rules
└── README.md                     # Project readme
```

## Key Files

### `slack_bot.py` - Main Application
- Initializes the Slack app using environment variables
- Contains three main event handlers:
  - `@app.message("hello")` - Responds to "hello" messages with block UI
  - `@app.action("button-click")` - Handles button click actions
  - `@app.action("open_modal")` - Opens modal dialogs
- Uses SocketModeHandler for real-time WebSocket connection

### `blocks.py` - UI Components
- `BLOCK` - Main message block with input field and action buttons
- `BLOCK_MODAL_VIEW` - Modal dialog view definition

## Tech Stack

- **Python:** ^3.10
- **Package Manager:** Poetry
- **Framework:** Slack Bolt for Python (^1.18.1)
- **Environment Variables:** python-dotenv (^1.0.0)
- **Slack SDK:** ^3.26.1 (transitive dependency)

## Development Commands

### Setup
```bash
# Install dependencies with Poetry
poetry install

# Or with pip (not recommended)
pip install python-dotenv slack-bolt
```

### Running the Bot
```bash
# Requires .env file with credentials
poetry run python slack_bot.py
```

### Pre-commit Hooks
```bash
# Install hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

## Required Environment Variables

Create a `.env` file with the following variables:
- `SLACK_BOT_TOKEN` - Bot User OAuth Token (xoxb-...)
- `SLACK_SIGNING_SECRET` - Signing secret from Slack app settings
- `SLACK_APP_TOKEN` - App-level token for Socket Mode (xapp-...)

## Code Conventions

### Python Style
- **Import Organization:** Enforced by reorder-python-imports
- **Quote Style:** Double quotes (enforced by pre-commit)
- **Line Length:** Flexible (E501 ignored in flake8)
- **Formatting:** autopep8 with trailing commas
- **Syntax:** Modern Python 3.7+ patterns (enforced by pyupgrade)

### Pre-commit Hooks (14 hooks enabled)
1. Trailing whitespace removal
2. End-of-file fixer
3. Debug statement detection
4. Merge conflict detection
5. Symlink validation
6. Private key detection
7. JSON/YAML/TOML syntax validation
8. Mixed line ending detection
9. AST validation
10. Double quote enforcement
11. reorder-python-imports
12. flake8 (E501 ignored)
13. autopep8
14. add-trailing-comma
15. pyupgrade (Python 3.7+)

### Slack Bolt Patterns

**Event Handler Pattern:**
```python
@app.message("trigger_word")
def handler_name(message, say):
    say(blocks=BLOCK_DEFINITION)
```

**Action Handler Pattern:**
```python
@app.action("action_id")
def action_handler(body, ack, say):
    ack()  # Always acknowledge first
    # Process the action
```

**Modal Opening Pattern:**
```python
@app.action("open_modal")
def open_modal_handler(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=MODAL_VIEW
    )
```

## CI/CD Workflows

### Quality Workflow (`.github/workflows/quality.yaml`)
- **Triggers:** Push and Pull Requests
- **Environment:** Ubuntu latest, Python 3.10
- **Actions:**
  1. Checkout code
  2. Setup Python 3.10
  3. Run pre-commit hooks

### Auto Assign Workflow (`.github/workflows/auto_assign.yml`)
- **Triggers:** PR opened/reopened
- **Action:** Assigns PR author automatically

## Adding New Features

### Adding a New Message Handler
1. Add the decorator and handler function in `slack_bot.py`
2. Define any new blocks in `blocks.py`
3. Run pre-commit hooks before committing

### Adding New UI Blocks
1. Define block dictionaries in `blocks.py`
2. Follow Slack Block Kit format: https://api.slack.com/block-kit
3. Import and use in handlers in `slack_bot.py`

### Adding New Actions
1. Define action buttons with unique `action_id` in `blocks.py`
2. Create corresponding `@app.action("action_id")` handler in `slack_bot.py`
3. Always call `ack()` first in action handlers

## Testing

No test framework is currently configured. When adding tests:
- Use pytest as the testing framework
- Add pytest to dev dependencies in `pyproject.toml`
- Create a `tests/` directory following pytest conventions

## Common Issues

### Bot Not Responding
1. Verify all three environment variables are set
2. Ensure Socket Mode is enabled in Slack app settings
3. Check that the bot has appropriate OAuth scopes

### Pre-commit Hook Failures
- Run `pre-commit run --all-files` to see specific failures
- Most issues auto-fix; re-stage and commit

## Architecture Notes

- **Socket Mode:** Uses WebSocket connection instead of HTTP webhooks
- **Block Kit:** All UI rendered using Slack Block Kit components
- **No Database:** Currently stateless, no persistence layer
- **No Logging:** Consider adding structured logging for production

## Git Workflow

- Main development happens on feature branches
- PRs trigger quality checks via GitHub Actions
- PR authors are auto-assigned to their PRs

## Future Considerations

- Add structured logging
- Implement error handling middleware
- Add unit tests with pytest
- Consider adding modal submission handlers
- Add environment-based configuration for staging/production
