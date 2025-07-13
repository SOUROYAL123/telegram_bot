import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "🚀 Hello from your CentOS Telegram bot!"

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {'chat_id': CHAT_ID, 'text': message}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message:", response.text)

