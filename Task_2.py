import requests


url = 'https://cloud-api.yandex.net/v1/disk/resources'
YA_TOKEN = ''
yandex_headers = {'Authorization': f'OAuth {YA_TOKEN}'}


def add_yandex_folder(path):
    response = requests.put(
        url,
        headers=yandex_headers,
        params={'path': f'disk:/{path}'}
    )
    return response.status_code
