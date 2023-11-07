import feedparser
import requests
import time

webhook = ""
username = "BlockBeats"
avatar_url = "https://cdn.discordapp.com/attachments/1114568807588057280/1171086524125823067/nioctib.png"
feed_url = "https://api.theblockbeats.news/v1/open-api/open-flash?size=10&page=1&lang=cht"

class DiscordNews:
    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook = webhook
        self.username = username
        self.avatar_url = avatar_url
        self.feed = feed
        self.latest_entry_id = None

    def get_latest_entry(self):
        latest_entry = self.feed.entries[0]  # Assuming the latest entry is at index 0
        return latest_entry

    def notify_to_discord_channel(self, data):
        headers = {"Content-Type": "application/json"}
        
        embed = {
            "author": {
            "name": "BaBy仔加密貨幣社區",
            "icon_url": "https://cdn.discordapp.com/attachments/1114568807588057280/1171086524125823067/nioctib.png"
    },
           
            "title": data.title,
            "description": data.description,
            "url": "https://discord.gg/AunF2eeJSz",
            "thumbnail": {"url": self.avatar_url}
        }

        payload = {
            "username": self.username,
            "embeds": [embed]
        }

        response = requests.post(url=self.webhook, headers=headers, json=payload)
        if response.status_code == 200:
            print("Notification sent successfully.")
        else:
            print(f"Failed to send notification. Status code: {response.status_code}")

    def check_for_new_news(self):
        latest_entry = self.get_latest_entry()
        if latest_entry.id != self.latest_entry_id:
            self.latest_entry_id = latest_entry.id
            self.notify_to_discord_channel(latest_entry)

    def run(self):
        while True:
            self.feed = feedparser.parse(feed_url)
            self.check_for_new_news()
            time.sleep(10)  # Wait for 10 seconds before checking again

discord = DiscordNews(webhook, username, avatar_url, None)
discord.run()
