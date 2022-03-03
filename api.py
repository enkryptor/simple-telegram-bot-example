import requests

token = "5250370860:AAFMzJEMoV9QANxygvSt_g-X0yWggVHYN7s"
base_url = "https://api.telegram.org/bot" + token

# Telegram API, see https://core.telegram.org/bots/api
get_updates_url = f"{base_url}/getUpdates"
send_message_url = f"{base_url}/sendMessage"


def get_updates(offset: int, timeout: int) -> list[dict]:
    params = {
        "offset": offset,
        "timeout": timeout,
    }
    response = requests.get(get_updates_url, params=params)
    return response.json()["result"]


def send_message(chat_id: int, message: str):
    data = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.post(send_message_url, data=data)
