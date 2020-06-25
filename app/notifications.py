import requests
import json

header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic N2U4MGY5OGYtOWI5ZC00MjAzLTk2OWEtNzYxMjZlYjVlOWIw"}
app = "f09c1767-31e2-4894-8b7f-66588f880318"


class Notifications:

    @staticmethod
    def SendActive():
        payload = {
            "app_id": app,
            "included_segments": ["Active Users"],
            "headings": {"en": "SmartFrame", "pt": "Retrato Inteligente", "es": "Retrato Inteligente"},
            "contents": {"en": "English Message", "pt": "Mensagem no Português", "es": "Mensaje en Español"},
            "chrome_web_badge": "https://i.imgur.com/9QFB20F.png"
        }
        req = requests.post(
            "https://onesignal.com/api/v1/notifications",
            headers=header, data=json.dumps(payload)
        )
        return req

    @staticmethod
    def SendUser(id):
        payload = {
            "app_id": app,
            # "included_segments": ["Active Users"],
            "include_player_ids": [id],
            "headings": {"en": "Order", "pt": "Pedido enviado", "es": "Su pedido fue recibido"},
            "contents": {"en": "English Message",
                         "pt": "Aguarde un pouco, nos estamos fazendo seu pedido",
                         "es": "Espere un poco, estamos preparando su pedido"},
            "chrome_web_badge": "https://i.imgur.com/9QFB20F.png"
        }
        req = requests.post(
            "https://onesignal.com/api/v1/notifications",
            headers=header, data=json.dumps(payload)
        )
        return req


    @staticmethod
    def SendDevices():
        payload = {
            "app_id": app,
            # "included_segments": ["Active Users"],
            "include_player_ids": [id],
            "headings": {"en": "SmartFrame", "pt": "Retrato Inteligente", "es": "Retrato Inteligente"},
            "contents": {"en": "English Message", "pt": "Mensagem no Português", "es": "Mensaje en Español"},
            "chrome_web_badge": "https://i.imgur.com/9QFB20F.png"
        }
        req = requests.get(
            "https://onesignal.com/api/v1/players?app_id=%s" % app,
            headers=header
        )
        return req