import time
import requests
from datetime import datetime, timedelta

BOT_TOKEN = '8038234180:AAEELH2g6ghhgC58Mup0B-O7OjO24IaTisY'  # встав сюди свій токен
CHAT_ID = '-1001914847589'         # встав сюди ID групи або чату

SEASON_START_DATE = datetime(2024, 5, 14)
SEASON_LENGTH_DAYS = 30
DAYS_BEFORE_END = 2
REMINDER_TEXT = "Напоминание! До конца сезона осталось 2 дня!!"

last_reminder_date = None

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    if resp.status_code == 200:
        print(f"[{datetime.now()}] Повідомлення надіслано")
    else:
        print(f"[{datetime.now()}] Помилка: {resp.text}")

def check_and_send():
    global last_reminder_date
    today = datetime.now().date()
    days_passed = (today - SEASON_START_DATE.date()).days
    if days_passed < 0:
        return
    season_number = days_passed // SEASON_LENGTH_DAYS
    season_start = SEASON_START_DATE + timedelta(days=season_number * SEASON_LENGTH_DAYS)
    season_end = season_start + timedelta(days=SEASON_LENGTH_DAYS)
    reminder_day = season_end.date() - timedelta(days=DAYS_BEFORE_END)

    if today == reminder_day and last_reminder_date != today:
        send_message(REMINDER_TEXT)
        last_reminder_date = today

if __name__ == "__main__":
    print("Бот запущено")
    while True:
        check_and_send()
        time.sleep(3600)  # перевірка кожну годину
