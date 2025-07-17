import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

client = WebClient(token=SLACK_TOKEN)

def slack_notify(employee, reason, action):
    message = f"🔔 *Employee Risk Alert*\n👤 {employee}\n⚠️ Reason: {reason}\n💡 Recommended Action: {action}"
    try:
        client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
    except Exception as e:
        print(f"Slack error: {e}")
