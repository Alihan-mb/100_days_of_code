from posting_pixels import PostPixel
import config as conf
import datetime as dt

pixel = PostPixel(conf.TOKEN)

now = dt.datetime.now()

formatted_date = now.strftime("%Y%m%d")

response = pixel.sending_pixel(formatted_date, "11.8", conf.HEADER_NAME)
assert response.status_code == 200
