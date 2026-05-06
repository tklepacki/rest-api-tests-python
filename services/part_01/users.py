import requests

def get_user(id):
    url = f"https://reqres.in/api/users/{id}"

    session = requests.session()
    response = session.get(url, headers={'x-api-key': 'reqres_eb68f411937a40c68226fb013febfe14'})

    return response

def get_users_list(page_id):
    url = "https://reqres.in/api/users"

    session = requests.session()
    response = session.get(url, params={'page': page_id}, headers={'x-api-key': 'reqres_eb68f411937a40c68226fb013febfe14'})

    return response