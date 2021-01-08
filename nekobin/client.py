from json import JSONDecodeError
from typing import Union, Optional

import aiohttp
from .errors import UnknownError, HostDownError
from .types import Neko


class NekoBin:
    def __init__(
        self,
        *,
        host: str = "https://nekobin.com",
        path: str = "/api/documents"
    ) -> None:
        self._host = host
        self._path = path

    async def do_request(
        self,
        data: str,
        title: Optional[str] = None,
        author: Optional[str] = None,
    ):
        async with aiohttp.ClientSession() as ses:
            request = await ses.post(
                f"{self._host}{self._path}",
                json={
                    'content': data,
                    'title': title,
                    'author': author,
                },
                timeout=3
            )
        try:
            return await request.json(), request
        except JSONDecodeError:
            return await request.text(), request

    async def nekofy(
        self,
        content: str,
        title: Optional[str] = None,
        author: Optional[str] = None,
    ) -> Union[Neko, bool]:
        try:
            data, _ = await self.do_request(
                content,
                title,
                author
            )
            return Neko(**data)
        except UnknownError:
            return False
        except aiohttp.client_exceptions.ClientConnectorError:
            raise HostDownError("Client cannot reach Host at the moment")
