import requests

def get_user(id):
    url = f"https://reqres.in/api/users/{id}"

    session = requests.session()
    response = session.get(url)

    return response

def get_users_list(page_id):
    url = "https://reqres.in/api/users"

    session = requests.session()
    response = session.get(url, params={'page': page_id})

    return response