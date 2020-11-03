#!/usr/bin/env python

import argparse
import asyncio
import json
import logging as log
import pprint
import sys
import urllib.parse

from aiohttp import web
from datetime import datetime, timezone

class Tranquillou:
    def __init__(self, config):
        self.listen_address = urllib.parse.urlparse("http://" + config.listen)
        self.print_body = config.print_body or config.pretty_print_json
        self.pretty_print_json = config.pretty_print_json
        self.response_code = config.response_code
        self.print_headers = config.print_headers


    async def run(self):
        app = web.Application()

        app.router.add_routes([web.route('*', '/status/{code}', self._return_code)])
        app.router.add_routes([web.route('*', '/{tail:.*}', self._handler)])

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=self.listen_address.hostname, port=self.listen_address.port)
        await site.start()
        while True:
            await asyncio.sleep(10)


    async def _print_raw(self, request):
        body = await request.text()
        if len(body) > 0:
            print("---------- Body (raw)")
            print(body)
            print("----------\n")

    async def _print_json(self, request):
        body = await request.json()
        print("---------- Body (json)")
        print(json.dumps(body, indent=4))
        print("----------")

    async def _print_headers(self, request):
        if self.print_headers:
            print("---------- Headers")
            for name, value in request.headers.items():
                print(f'{name}: {value}')
            print("----------")

    async def _print_body(self, request):
        if self.print_body:
            if self.pretty_print_json:
                try:
                    await self._print_json(request)
                except json.decoder.JSONDecodeError:
                    await self._print_raw(request)
            else:
                await self._print_raw(request)


    async def _print_method_and_url(self, request):
        print(f'{request.method} - {request.url}')


    async def _print_source(self, request):
        print(f'From: {request.remote}')

    async def _print_all(self, request):
        print(datetime.now(timezone.utc).isoformat())
        await self._print_source(request)
        await self._print_method_and_url(request)
        await self._print_headers(request)
        await self._print_body(request)

    async def _return_code(self, request):
        print(f"================")
        await self._print_all(request)
        code = int(request.match_info["code"])
        print(f"RETURNING {code}")
        print(f"================\n")
        return web.Response(status=code)

    async def _handler(self, request):
        print(f"================")
        await self._print_all(request)
        print(f"================\n")
        return web.Response(status=self.response_code)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--listen', "-l", help="listen address", default='localhost:8080')
    parser.add_argument('--pretty-print-json', action='store_true',
        help="Attempt to pretty-print the body as JSon, fallback to simple text. Implies --print-body")
    parser.add_argument('--print-body', action='store_true', help="Print the full body")
    parser.add_argument('--response-code', type=int, default=200, help="Which http code to return by default")
    parser.add_argument('--print-headers', action='store_true', help="Whether to print request headers")

    config = parser.parse_args()


    log.basicConfig(level='WARN',
                    format="%(asctime)s|%(filename)s:%(lineno)s|%(funcName)s|%(levelname)s|%(message)s",
                    stream=sys.stdout)

    app = Tranquillou(config)
    asyncio.run(app.run())
