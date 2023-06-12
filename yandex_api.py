import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

        headers = {
            'Authorization': self.token
        }

        params = {
            'path': file_path
        }

        print(file_path)

        resp = requests.get(url, headers=headers, params=params)

        if 200 <= resp.status_code < 300:
            upload_url = resp.json().get('href', '')
            with open(file_path, 'rb') as file:
                upload_resp = requests.put(upload_url, files={'file': file})
        else:
            print(resp.status_code)
            print(resp.json())


if __name__ == '__main__':
    path_to_file = 'img.jpg'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)