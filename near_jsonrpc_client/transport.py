import httpx


class HttpTransportAsync:
    def __init__(
            self,
            base_url: str,
            *,
            timeout: float = 10.0,
            headers: dict[str, str] | None = None,
    ):
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers=headers,
        )

    async def post(self, json: dict) -> httpx.Response:
        return await self._client.post("", json=json)

    async def close(self):
        await self._client.aclose()


class HttpTransportSync:
    def __init__(
            self,
            base_url: str,
            *,
            timeout: float = 10.0,
            headers: dict[str, str] | None = None,
    ):
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers=headers,
        )

    def post(self, json: dict) -> httpx.Response:
        return self._client.post("", json=json)

    def close(self):
        self._client.close()
