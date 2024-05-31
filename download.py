import asyncio
import time

import httpx


async def test_download(url):
    print(f"starting test...")
    t1 = time.time()
    bytes = 0
    async with httpx.AsyncClient() as client:
        async with client.stream('GET', url) as response:
            if response.status_code!=200:
                raise Exception(f'got status {response.status_code} for {url}')
            async for chunk in response.aiter_bytes(chunk_size=10*1024*1024):
                bytes += len(chunk)
    t2 = time.time()
    print(f"{bytes} bytes downloaded in {t2-t1:.3f}s")


if __name__ == '__main__':
    for i in range(5):
        asyncio.run(test_download( url = 'http://ipv4.download.thinkbroadband.com/200MB.zip'))    