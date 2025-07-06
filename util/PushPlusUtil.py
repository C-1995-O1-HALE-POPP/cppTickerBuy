import json

import loguru
import requests
import playsound
import os



def send_message(token, content, title):
    try:
        url = "http://www.pushplus.plus/send"
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "token": token,
            "content": content,
            "title": title
        }
        requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as e:
        loguru.logger.info("PushPlus消息发送失败")





if __name__ == '__main__':
    playsound.playsound(os.path.join(get_application_tmp_path(), "default.mp3"))
