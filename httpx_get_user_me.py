import httpx

login_payload = {
  "email": "a.mishagin1986@gmail.com",
  "password": "cfif"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']
print("JSON с токенами:", login_response_data['token'])

headers = {"Authorization": f"Bearer {access_token}"}

user_info_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
user_info_response_date = user_info_response.json()
print("Данные пользователя: ", user_info_response_date)
print("Статус-код ответа: ", user_info_response.status_code)