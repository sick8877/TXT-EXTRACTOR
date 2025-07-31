import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "25437216"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "490ad5f5ed36ce93496c60ede5712081")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8392338221:AAFaHdpcsZo1fnuhSdfnhoKh0NxqIksKsIM")

OWNER_ID = int(os.environ.get("OWNER_ID", "684325515"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "684325515").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://ashusharma623093yhVsoTiiqL1zCP9@cluster0.ybo0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002559963953"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "1002559963953")  # Optional here you'll get all logs
