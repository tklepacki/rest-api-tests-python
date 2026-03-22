import requests

headers = {
    "x-api-key": "reqres_c0388624c53b497eb0116d677c3e0882"
}

def get_users_list(page_id): 
    url = "https://reqres.in/api/users"

    session = requests.session()
    response = session.get(url, headers=headers, params={"page": page_id})

    return response

def get_user(page_id):
    url = f"https://reqres.in/api/users/{page_id}"

    session = requests.session()
    response = session.get(url, headers=headers)

    return response