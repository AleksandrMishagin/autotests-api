from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

