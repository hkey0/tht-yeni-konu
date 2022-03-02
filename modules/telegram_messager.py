import requests


def send_message(text: str, config: dict) -> None:
    data = {
        "text": text
    }
    requests.post(
        "https://api.telegram.org/bot" + config['token'] + "/sendMessage?chat_id=" + config['channel_id'], data=data)
    
