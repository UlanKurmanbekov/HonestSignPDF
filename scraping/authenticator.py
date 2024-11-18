from abc import ABC, abstractmethod

import httpx

from core.config import AUTH_URL, AUTH_TOKEN_TYPE, BASE64_CODE


class Authenticator(ABC):
    @abstractmethod
    def authenticate(self) -> str:
        pass


class PasswordAuthenticator(Authenticator):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def authenticate(self) -> str:
        headers = {
            "Authorization": f"{AUTH_TOKEN_TYPE} {BASE64_CODE}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        auth_data = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password"
        }

        response = httpx.post(url=AUTH_URL, headers=headers, data=auth_data)
        response.raise_for_status()
        return response.json().get("access_token")
