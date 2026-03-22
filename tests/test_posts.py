from pytest_steps import test_steps

import services.posts as posts

@test_steps('add_post_request')
def test_add_post_request():
    body = {
        "title": "TestTitle",
        "views": 100,
    }

    add_post_response = posts.add_post(body)
    added_post_data = add_post_response.json()

    assert (add_post_response.status_code == 201), f"Status Code validation failed for {add_post_response.request.url}"
    assert (added_post_data["title"] == "TestTitle"), f"Post title validation failed for {add_post_response.request.url}"
    assert (added_post_data["views"] == 100), f"Post views validation failed for {add_post_response.request.url}"

    added_post_id = added_post_data["id"]

    posts_response = posts.get_post(added_post_id)
    post_data = posts_response.json()

    assert (posts_response.status_code == 200), f"Status Code validation failed for {posts_response.request.url}"
    assert (post_data["title"] == "TestTitle"), f"Post title validation failed for {posts_response.request.url}"
    assert (post_data["views"] == 100), f"Post views validation failed for {posts_response.request.url}"
    assert (post_data["id"] == added_post_id), f"Post id validation failed for {posts_response.request.url}"

    yield

@test_steps('delete_post_request')
def test_delete_post_request():
    body = {
        "title": "TestTitle",
        "views": 100,
    }

    add_post_response = posts.add_post(body)
    added_post_data = add_post_response.json()

    assert (add_post_response.status_code == 201), f"Status Code validation failed for {add_post_response.request.url}"

    added_post_id = added_post_data["id"]

    delete_post_response = posts.delete_post(added_post_id)

    assert (delete_post_response.status_code == 200), f"Status Code validation failed for {delete_post_response.request.url}"

    get_posts_list_response = posts.get_posts_list()
    posts_list = get_posts_list_response.json()
    post_ids = [item["id"] for item in posts_list]

    assert added_post_id not in post_ids, f"Post deletion failed for {delete_post_response.request.url}"

    yield

@test_steps('edit_post_request')
def test_edit_post_request():
    body = {
        "title": "TestTitle",
        "views": 100,
    }

    add_post_response = posts.add_post(body)
    added_post_data = add_post_response.json()

    assert (add_post_response.status_code == 201), f"Status Code validation failed for {add_post_response.request.url}"

    added_post_id = added_post_data["id"]

    edit_body = {
        "title": "EditedTestTitle",
        "views": 150,
    }

    edit_post_response = posts.edit_post(added_post_id, edit_body)

    assert (edit_post_response.status_code == 200), f"Status Code validation failed for {edit_post_response.request.url}"

    get_post_response = posts.get_post(added_post_id)
    post_data = get_post_response.json()

    assert (post_data["title"] == "EditedTestTitle"), f"Post title validation failed for {edit_post_response.request.url}"
    assert (post_data["views"] == 150), f"Post views validation failed for {edit_post_response.request.url}"   

    yield
