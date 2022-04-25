import requests
last_update_id = 0
while True:
    result = requests.get('https://api.telegram.org/bot1935327602:AAHsLgxgEFLacyTcPr03HV0Iow80HqUtzKo/getUpdates', params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        tx = chat_id = update['message']['text']
        send_result = requests.get('https://api.telegram.org/bot1935327602:AAHsLgxgEFLacyTcPr03HV0Iow80HqUtzKo/sendMessage', params={'chat_id': chat_id, 'text': tx + ' – так матери своей скажешь'})