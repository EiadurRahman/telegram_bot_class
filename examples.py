from tgm import Bot

# Initialize the Bot
auth_token = 'YOUR_BOT_TOKEN'   # Replace with your actual bot token
chat_id = 'YOUR_CHAT_ID'         # Replace with the chat ID you want to send messages to

bot = Bot(auth_token=auth_token, chat_id=chat_id)

# 1. Sending a Text Message
print("Sending a text message...")
bot.send_msg("Hello! This is a test message from the bot.")

# 2. Receiving Messages
print("Receiving messages...")
messages = bot.recive_msg()
for msg_chat_id, text in messages:
    print(f"Chat ID: {msg_chat_id}, Message: {text}")

# 3. Sending a Photo
photo_path = "path/to/photo.jpg"  # Replace with the path to your photo file
print("Sending a photo...")
if bot.send_photo(photo_path):
    print("Photo sent successfully!")
else:
    print("Failed to send photo.")

# 4. Sending a Video
video_path = "path/to/video.mp4"  # Replace with the path to your video file
print("Sending a video...")
if bot.send_vid(video_path):
    print("Video sent successfully!")
else:
    print("Failed to send video or video too large.")

# 5. Sending a Media Group
media_files = [
    "path/to/photo1.jpg",   # Replace with actual file paths
    "path/to/photo2.png",
    "path/to/video.mp4"
]
print("Sending a media group...")
media_group_response = bot.send_media_group(media_files)
if media_group_response:
    print("Media group sent successfully!")
else:
    print("Failed to send media group.")

# 6. Retrieving Updates
print("Retrieving updates...")
all_updates = bot.get_update()
print("All Updates:", all_updates)

# Retrieve only the chat ID from the latest message
latest_chat_id = bot.get_update(param='chat_id')
print("Latest Chat ID:", latest_chat_id)

