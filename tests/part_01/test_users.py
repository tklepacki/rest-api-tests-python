from pytest_steps import test_steps

import services.part_01.users as users

@test_steps('test_get_user_request')
def test_get_user_request():
    user_response = users.get_user(2)
    user_data = user_response.json()['data']

    assert (user_response.status_code == 200), f"Status Code validation failed for {user_response.request.url}"
    assert (user_data['id'] == 2), "User Id verfication failed"
    assert (user_data['email'] == "janet.weaver@reqres.in"), "User Id verfication failed"
    assert (user_data['first_name'] == "Janet"), "First Name verfication failed"
    assert (user_data['last_name'] == "Weaver"), "Last Name verfication failed"
    assert (user_data['avatar'] == "https://reqres.in/img/faces/2-image.jpg"), "Avatar verfication failed"
    assert (user_response.headers['content-type'] == "application/json; charset=utf-8")
    
    yield

@test_steps('test_get_user_list_request')
def test_get_user_list_request():
    get_users_list_response = users.get_users_list(2)
    user_lists_root_data = get_users_list_response.json()

    assert (get_users_list_response.status_code == 200), f"Status Code validation failed for {get_users_list_response.request.url}"
    assert (user_lists_root_data['page'] == 2), "Page verfication failed"
    assert (user_lists_root_data['per_page'] == 6), "Per_Page verfication failed"
    assert (user_lists_root_data['total'] == 12), "Total verfication failed"
    assert (user_lists_root_data['total_pages'] == 2), "Total_Pages verfication failed"

    user_lists_data_1 = user_lists_root_data['data'][0]

    assert (user_lists_data_1['id'] == 7), "User Id verfication failed"
    assert (user_lists_data_1['email'] == "michael.lawson@reqres.in"), "User Id verfication failed"
    assert (user_lists_data_1['first_name'] == "Michael"), "First Name verfication failed"
    assert (user_lists_data_1['last_name'] == "Lawson"), "Last Name verfication failed"
    assert (user_lists_data_1['avatar'] == "https://reqres.in/img/faces/7-image.jpg"), "Avatar verfication failed"
    assert (get_users_list_response.headers['content-type'] == "application/json; charset=utf-8")

    emails = [item['email'] for item in user_lists_root_data['data']]

    assert len(emails) == 6 
    assert "michael.lawson@reqres.in" in emails
    assert "lindsay.ferguson@reqres.in" in emails
    assert "tobias.funke@reqres.in" in emails
    assert "byron.fields@reqres.in" in emails
    assert "george.edwards@reqres.in" in emails
    assert "rachel.howell@reqres.in" in emails

    yield
