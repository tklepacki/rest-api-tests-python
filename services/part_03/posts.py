import requests

def get_post(id):
    url = f"http://localhost:3000/posts/{id}"

    session = requests.session()
    response = session.get(url)

    return response

def get_posts_list():
    url = "http://localhost:3000/posts"

    session = requests.session()
    response = session.get(url)

    return response

def add_post(body):
    url = "http://localhost:3000/posts"

    session = requests.session()
    response = session.post(url, json=body)

    return response

def edit_post(id, body):
    url = f"http://localhost:3000/posts/{id}"

    session = requests.session()
    response = session.put(url, json=body)

    return response

def delete_post(id):
    url = f"http://localhost:3000/posts/{id}"

    session = requests.session()
    response = session.delete(url)

    return response