import asyncio
from math import ceil
from typing import Mapping, Optional, List, Dict

from aiohttp import ClientSession, ClientError
from tqdm import asyncio as tqdm_aio


class BaseRepository:
    MASTER_URL = 'https://api.bagelstudio.co/api/public'

    def __init__(self, settings):
        self.settings = settings
        self.enable_tqdm = settings.debug
        self.headers = {"Authorization": f"Bearer {settings.api_token.get_secret_value()}", "Accept-Version": "v1"}

    @staticmethod
    async def fetch_json(url: str, params: Optional[Mapping[str, str]], session: ClientSession) -> tuple:
        data = None
        retries = 10
        while data is None or retries == 0:
            try:
                async with session.get(url, params=params) as response:
                    retries -= 1
                    data = await response.json()
            except ClientError:
                await asyncio.sleep(1)
            except asyncio.exceptions.TimeoutError:
                await asyncio.sleep(1)
        return url, data

    async def parallel_fetching_by_urls(self, urls: set) -> []:
        async with ClientSession(headers=self.headers) as session:
            tasks = []
            for url in urls:
                tasks.append(
                    BaseRepository.fetch_json(url=url, params=None, session=session)
                )
            results = await tqdm_aio.tqdm.gather(*tasks)
        jsons = []
        for result in results:
            jsons.append(result[1])
        return jsons

    async def parallel_fetching_by_params(self, url: str, params: List[Mapping[str, str]]) -> List[Dict]:
        async with ClientSession(headers=self.headers) as session:
            tasks = []
            for p in params:
                tasks.append(
                    BaseRepository.fetch_json(url=url, params=p, session=session)
                )
            results = await tqdm_aio.tqdm.gather(*tasks)
        jsons = []
        for result in results:
            jsons.append(result[1])
        return jsons
