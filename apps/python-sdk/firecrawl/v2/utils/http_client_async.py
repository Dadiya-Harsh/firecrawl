import httpx
from typing import Optional, Dict, Any
from .get_version import get_version

version = get_version()


class AsyncHttpClient:
    def __init__(self, api_key: Optional[str], api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        
        self._client = httpx.AsyncClient(
            base_url=api_url,
            headers={"Content-Type": "application/json"},
            limits=httpx.Limits(max_keepalive_connections=0),
        )

    async def close(self) -> None:
        await self._client.aclose()

    def _headers(self, idempotency_key: Optional[str] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {}
        
        # Only add Authorization header if api_key is provided and not empty/whitespace
        if self.api_key and self.api_key.strip():
            headers["Authorization"] = f"Bearer {self.api_key.strip()}"
            
        if idempotency_key:
            headers["x-idempotency-key"] = idempotency_key
        return headers

    async def post(
        self,
        endpoint: str,
        data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        payload = dict(data)
        payload["origin"] = f"python-sdk@{version}"
        return await self._client.post(
            endpoint,
            json=payload,
            headers={**self._headers(), **(headers or {})},
            timeout=timeout,
        )

    async def get(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        return await self._client.get(
            endpoint, headers={**self._headers(), **(headers or {})}, timeout=timeout
        )

    async def delete(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        return await self._client.delete(
            endpoint, headers={**self._headers(), **(headers or {})}, timeout=timeout
        )

