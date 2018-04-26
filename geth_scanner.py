# coding: utf-8
"""
Created by chuwt on 18/4/26.
"""
# os
import asyncio
# third

# self
from eth import ETHClient


class Connector(object):
    def __init__(self):
        self.queue = asyncio.Queue()

    async def get_ips(self):
        with open('./ips.txt', 'r+') as f:
            while True:
                data = f.readline()
                if data:
                    await self.queue.put(data)
                else:
                    await self.queue.put('end')
                    break
            f.close()

    async def geth_connector(self):
        while True:
            if self.queue.empty():
                continue
            else:
                url = await self.queue.get()
                if url.startswith('end'):
                    break
                else:
                    try:
                        data = await ETHClient(url).list_account()
                        print(data)
                    except Exception as msg:
                        print(msg)
                    finally:
                        print(url)

    async def main(self):
        task_list = list()
        task_list.append(asyncio.ensure_future(self.get_ips()))
        task_list += [asyncio.ensure_future(self.geth_connector()) for _ in range(1)]
        await asyncio.wait(task_list)

    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.ensure_future(self.main()))
        finally:
            loop.close()


if __name__ == '__main__':
    c = Connector()
    c.run()
