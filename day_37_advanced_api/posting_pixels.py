import requests
import config as conf


class PostPixel:
    def __init__(self, token):
        self.token = token

    def sending_pixel(self, day, value: str, header_name):
        pixel_config = {
            "date": day,
            "quantity": f"{value}"
        }
        pixel_header = {
            header_name: self.token,
        }

        response = requests.post(url=conf.posting_pixel_endpoint, json=pixel_config, headers=pixel_header)
        return response
