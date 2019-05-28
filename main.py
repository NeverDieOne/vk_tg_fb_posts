import vk_api
from dotenv import load_dotenv
import os
import settings


load_dotenv()

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
