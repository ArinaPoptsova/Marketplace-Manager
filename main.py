import json
import os

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest



channels = ['Ozon Marketplace', 'Яндекс Маркет для продавцов']
client = TelegramClient('test', os.getenv('API_ID'), os.getenv('API_HASH'))

def main(phone):
    client.start()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    offset_id = 0
    channels_data = []
    all_messages = []
    limit = 10

    for channel in channels:
        channel_data = client.get_entity(channel)
        channels_data.append(channel_data)

        history = client(GetHistoryRequest(
                peer=channel_data,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
        messages = history.messages
        for i in range(len(messages)):
            image_url = f'media/marketplace/{messages[i].photo.id}.png'
            message_data = dict(model='mp_messages.message', pk=image_url, fields={})
            message_data['model'] = 'mp_messages.message'

            message_data['fields']['date'] = messages[i].date
            message_data['fields']['message_text'] = messages[i].message
            if messages[i].photo is not None:
                client.download_media(messages[i].photo, image_url)
            message_data['fields']['image_url'] = image_url
            message_data['fields']['tag'] = channel
            all_messages.append(message_data)
    with open('mp_messages/fixtures/channel_messages.json', 'w') as outfile:
        json.dump(all_messages, outfile, ensure_ascii=False, default=str)
    return all_messages


print(main(os.getenv('PHONE')))
