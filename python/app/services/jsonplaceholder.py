import requests

class JsonPlaceholder:
    @staticmethod
    def get_users():
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        if response.status_code == 200:
            return response.json()
