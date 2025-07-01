from flask import Flask, request
import requests
import json

app = Flask(__name__)

# 你的 Channel access token
CHANNEL_ACCESS_TOKEN = 'eOtUJVnHKCD72M8iHwWb56YFpp2RdX8nMYXYiWbzY48E4rdl1P0xlS+qz0P0FLSaCqcNfmwN+slwf85A148i8HcBG/O2IUTYx+yGZWc2FHYpW1ae8yMZOyv2hr0DMSCRbme18iA5ulHTbsPK7WrHEAdB04t89/1O/w1cDnyilFU='

# 你的 userId
USER_ID = 'U2cab27af41f7eaf4bbb9a290d3dca38b'

@app.route("/", methods=['GET'])
def home():
    return "LINE Stock Webhook Ready!", 200

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_json()
    print("Received body:", body)
    return 'OK', 200

@app.route("/push", methods=['GET'])
def push_message():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }

    body = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": "📢 這是 AI 股票分析站 主動推播測試訊息。\n如果你看到這則訊息，代表設定成功！"
            }
        ]
    }

    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        return "訊息推播成功 ✅", 200
    else:
        return f"推播失敗 ❌：{response.status_code} - {response.text}", 500


if __name__ == "__main__":
    app.run()
