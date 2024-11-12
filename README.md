# Telegram Bot API Class

This project provides a Python class (`tgm.py`) for interacting with the Telegram Bot API. With this class, you can send messages, receive messages, send photos, videos, and media groups, and manage basic bot interactions.

## Features

- Send text messages
- Retrieve recent messages from a chat
- Send photos and videos
- Send media groups (multiple photos or videos)
- Customizable for different bot actions

## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/EiadurRahman/telegram_bot_class](https://github.com/EiadurRahman/telegram_bot_class)
    cd telegram_bot_class
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Obtain your bot token from the [Telegram BotFather](https://core.telegram.org/bots#botfather).
2. Find the chat ID of the conversation you want the bot to interact with.

### Example Usage

1. Update `examples.py` with your bot token, chat ID, and paths to media files.
2. Run `examples.py` to test each method in the `Bot` class.

### Example Code

Here's a quick overview of how to use the `Bot` class:

```python
from tgm import Bot

# Initialize the bot with your bot token and chat ID
bot = Bot(auth_token='YOUR_BOT_TOKEN', chat_id='YOUR_CHAT_ID')

# Send a message
bot.send_msg("Hello from the bot!")

# Receive recent messages
messages = bot.recive_msg()
print("Recent Messages:", messages)

# Send a photo
bot.send_photo("path/to/photo.jpg")

# Send a video
bot.send_vid("path/to/video.mp4")

# Send a media group
media_files = ["path/to/photo1.jpg", "path/to/photo2.png", "path/to/video.mp4"]
bot.send_media_group(media_files)
