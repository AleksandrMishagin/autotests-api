from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel
import uuid


class UserSchema(BaseModel):
    """Модель данных пользователя с базовыми полями профиля и уникальным ID."""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field (default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = "test_user@example.com"
    last_name: str
    first_name: str
    middle_name: str

    def get_username(self) -> str:
        """Метод для получения полного имени пользователя."""
        return f"{self.first_name} {self.last_name}"

class CreateUserRequestSchema(BaseModel):
    """Схема тела запроса для создания нового пользователя"""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field (default="sasha@example.com")
    password: str = Field (default="12345678")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Схема ответа API."""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    user: UserSchema

user_default_model = UserSchema(
    email="a.mishagin1986@gmail.com",
    lastName="Mishagin",
    firstName="Aleksandr",
    middleName="Sergeevich"
)

print("User default model:", user_default_model)

user_request_1 = CreateUserRequestSchema (lastName="Mishagin", firstName="Aleks", middleName="Aleksandovich")
user_request_2 = CreateUserRequestSchema (lastName="Ivanov", firstName="Ivan", middleName="Ivanovich")
print("Запрос CreateUserRequestSchema:", user_request_1)
print(user_request_2)

response_json_exmaple = """
{
    "user": {
        "id": "12345",
        "email": "a.mishagin1987@gmail.com",
        "lastName": "Mishagin",
        "firstName": "Aleksandr",
        "middleName": "Sergeevich"
    }
}
"""

response_model = CreateUserResponseSchema.model_validate_json(response_json_exmaple)
print("Ответ сервера успешно проверен:", response_model)
print("Имя зарегистрированного пользователя:", response_model.user.get_username())
