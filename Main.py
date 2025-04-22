import requests
import time
import json

TELEGRAM_BOT_TOKEN = '8120645471:AAGlObXJ_rHjcKR6RdOlpxXvDFr5Zg6aT_E'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'  # Энэ хэсэгт өөрийн chat_id-г оруул

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def check_signals():
    # Түр зуурын BUY дохионы жишээ, бодит мэдээлэлтэй холбож болно
    example_signal = {
        "symbol": "BTCUSDT",
        "price": 62000,
        "time": time.ctime()
    }
    return example_signal

while True:
    signal = check_signals()
    if signal:
        msg = f"BUY SIGNAL:\nSymbol: {signal['symbol']}\nPrice: {signal['price']}\nTime: {signal['time']}"
        send_telegram_message(msg)
    time.sleep(3600)  # 1 цаг тутам шалгана
