from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict, Any


class UserCreateRequestDict(TypedDict, total=False):
    """
    Описание структуры данных для создания нового пользователя.
    Поддерживает любые переданные поля (email, username, password и т.д.).
    """
    email: str
    password: str
    username: str
    # Используем Any для поддержки дополнительных динамических полей
    __extra__: Any


class PublicUsersClient(APIClient):
    """
     API клиент для работы с публичными эндпоинтами /api/v1/users.
    Включает методы, не требующие авторизации.
    """

    def create_user_api(self, request: UserCreateRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания нового пользователя.

        :param request: Словарь с данными пользователя (UserCreateRequestDict).
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("api/v1/users", json=request)