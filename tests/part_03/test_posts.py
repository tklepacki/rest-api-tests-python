from pytest_steps import test_steps

import services.part_03.posts as posts

@test_steps('test_get_post_request')
def test_get_post_request():
    posts_response = posts.get_post(1)
    post_data = posts_response.json()

    assert (posts_response.status_code == 200), f"Status Code validation failed for {posts_response.request.url}"
    assert (post_data['id'] == "1"), "Post Id verfication failed"
    assert (post_data['title'] == "a title"), "Title verfication failed"
    assert (post_data['views'] == 100), "Views verfication failed"
    assert (posts_response.headers['content-type'] == "application/json")
    yield

@test_steps('test_get_posts_list_request')
def test_get_posts_list_request():
    get_posts_list_response = posts.get_posts_list()
    posts_lists_data = get_posts_list_response.json()

    assert len(posts_lists_data) > 0, "No Posts are stored in the list"

    for post in posts_lists_data:
        assert (post['id'] != ''), "Post Id not exist"
        assert (post['title'] != ''), "Title not exist"
    yield

@test_steps('add_post_request')
def test_add_post_request():
    body = {
        "title": "TestTitle",
        "views": 100,
    }
    add_post_response = posts.add_post(body)
    added_post_data = add_post_response.json()

    assert (add_post_response.status_code == 201), f"Status Code validation failed for {add_post_response.request.url}"
    assert (added_post_data['title'] == "TestTitle"), "Title verfication failed"
    assert (added_post_data['views'] == 100), "Views verfication failed"

    added_post_id = added_post_data['id']

    posts_response = posts.get_post(added_post_id)
    post_data = posts_response.json()

    assert (posts_response.status_code == 200), f"Status Code validation failed for {posts_response.request.url}"
    assert (post_data['id'] == added_post_id), "Post Id verfication failed"
    assert (post_data['title'] == "TestTitle"), "Title verfication failed"
    assert (post_data['views'] == 100), "Views verfication failed"
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
    assert (added_post_data['title'] == "TestTitle"), "Title verfication failed"
    assert (added_post_data['views'] == 100), "Views verfication failed"

    added_post_id = added_post_data['id']

    body = {
        "title": "UpdatedTestTitle",
        "views": 500,
    }

    edit_post_response = posts.edit_post(added_post_id, body)
    edit_post_data = edit_post_response.json()

    assert (edit_post_response.status_code == 200), f"Status Code validation failed for {edit_post_response.request.url}"
    assert (edit_post_data['title'] == "UpdatedTestTitle"), "Updated Title verfication failed"
    assert (edit_post_data['views'] == 500), "Updated Views verfication failed"

    posts_response = posts.get_post(added_post_id)
    post_data = posts_response.json()

    assert (posts_response.status_code == 200), f"Status Code validation failed for {posts_response.request.url}"
    assert (post_data['id'] == added_post_id), "Updated Post Id verfication failed"
    assert (post_data['title'] == "UpdatedTestTitle"), "Updated Title verfication failed"
    assert (post_data['views'] == 500), "Updated Views verfication failed"
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
    assert (added_post_data['title'] == "TestTitle"), "Title verfication failed"
    assert (added_post_data['views'] == 100), "Views verfication failed"

    added_post_id = added_post_data['id']

    delete_post_response = posts.delete_post(added_post_id)

    assert (delete_post_response.status_code == 200), f"Status Code validation failed for {delete_post_response.request.url}"
    
    get_posts_list_response = posts.get_posts_list()
    posts_lists_data = get_posts_list_response.json()

    id_list = [item['id'] for item in posts_lists_data]

    assert added_post_id not in id_list

    yield