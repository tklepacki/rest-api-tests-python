from pytest_steps import test_steps

import services.users as users 

@test_steps('test_get_user_list_request')
def test_get_user_list_request():
    get_user_list_response = users.get_users_list(2)
    user_lists_root_data = get_user_list_response.json()

    assert (get_user_list_response.status_code == 200), f"Status Code validation failed for {get_user_list_response.request.url}"
    assert (user_lists_root_data["page"] == 2), f"Page number validation failed for {get_user_list_response.request.url}"
    assert (user_lists_root_data["per_page"] == 6), f"Per page validation failed for {get_user_list_response.request.url}"
    assert (user_lists_root_data["total"] == 12), f"Total number validation failed for {get_user_list_response.request.url}"
    assert (user_lists_root_data["total_pages"] == 2), f"Total pages validation failed for {get_user_list_response.request.url}"

    user_list_data_1 = user_lists_root_data["data"][0]

    assert (user_list_data_1["id"] == 7), f"User id validation failed for {get_user_list_response.request.url}"
    assert (user_list_data_1["email"] == "michael.lawson@reqres.in"), f"User email validation failed for {get_user_list_response.request.url}"
    assert (user_list_data_1["first_name"] == "Michael"), f"User first name validation failed for {get_user_list_response.request.url}"
    assert (user_list_data_1["last_name"] == "Lawson"), f"User last name validation failed for {get_user_list_response.request.url}"
    assert (user_list_data_1["avatar"] == "https://reqres.in/img/faces/7-image.png"), f"User avatar validation failed for {get_user_list_response.request.url}"

    emails = [item["email"] for item in user_lists_root_data["data"]]

    assert len(emails) == 6, f"User list count validation failed for {get_user_list_response.request.url}"
    assert "michael.lawson@reqres.in" in emails, f"User email validation failed for {get_user_list_response.request.url}"

    yield