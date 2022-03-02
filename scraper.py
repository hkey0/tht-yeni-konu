from modules.config import read_config
import xmltodict
import requests
from modules.telegram_messager import send_message
import time


def get_last_topic() -> bool and str:
    r    = requests.get("https://www.turkhackteam.org/forumlar/-/index.rss")
    data = dict(xmltodict.parse(r.text))

    last         = data['rss']['channel']['item'][0]
    last_as_text = f"Başlık  : {last['title']}\nContent : {last['content:encoded'][23:70]}...\nZaman   : {last['pubDate']}\nUrl     : {last['link']}"
    is_new       = False

    if last['slash:comments'] == "0":
        is_new = True
    

    print(last_as_text + "\n\n")
    return is_new, last_as_text
    

def controller() -> None:
    last = None
    config = read_config()

    while True:
        is_new, text = get_last_topic()

        if is_new and last != text and last:
            send_message(text, config)

        last = text
        time.sleep(5)

controller()