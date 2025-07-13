import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "Test message from Railway!"  # Message to send

# Telegram API URL
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Payload for the message
payload = {'chat_id': CHAT_ID, 'text': message}

# Send the POST request to Telegram API
res = requests.post(url, data=payload)

# Debugging: Print the response to check the status
print("Response from Telegram API:", res.text)


