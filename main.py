import vk_api
from dotenv import load_dotenv
import os
import settings
import telegram
import requests

PHOTO = '/Users/neverdie/Pictures/1.jpg'
MESSAGE = 'First post in my life'


def vk_post(photo, message):
    group_id = settings.vk_settings['group_id']
    app_id = settings.vk_settings['app_id']
    album_id = settings.vk_settings['album_id']
    owner_id = settings.vk_settings['owner_id']

    vk_session = vk_api.VkApi(token=os.getenv('VK_ACCESS_TOKEN'), api_version='5.95', app_id=app_id)
    vk = vk_session.get_api()

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(photo, album_id=album_id, group_id=group_id)

    vk.wall.post(message=message, owner_id=owner_id, attachments=f'photo{owner_id}_{photo[0]["id"]}')


def tg_post(photo, message):
    # TODO https://www.iguides.ru/blogs/leghko/long-text-image-at-the-bottom-manual/
    chat_id = settings.tg_settings['chat_id']

    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    bot.send_message(chat_id=chat_id, text=message)
    bot.send_photo(chat_id=chat_id, photo=open(photo, 'rb'))


def fb_post(photo, message):
    base_url = 'https://graph.facebook.com/'
    group_id = settings.fb_settings['group_id']

    data = {
        'access_token': os.getenv('FB_TOKEN'),
        'caption': message,
    }
    files = {'upload_file': open(photo, 'rb')}

    requests.post(f'{base_url}{group_id}/photos', files=files, data=data)


if __name__ == '__main__':
    load_dotenv()
