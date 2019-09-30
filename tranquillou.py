#!/usr/bin/env python

import argparse
import asyncio
import json
import logging as log
import pprint
import sys
import urllib.parse

from aiohttp import web

class Tranquillou:
    def __init__(self, config):
        self.listen_address = urllib.parse.urlparse("http://" + config.listen)
        self.print_body = config.print_body or config.json_body
        self.pretty_print_json = config.pretty_print_json
        self.response_code = config.response_code
        self.print_headers = config.print_headers


    async def run(self):
        app = web.Application()

        app.router.add_routes([web.route('POST', '/tokens', self._token)])
        app.router.add_routes([web.route('POST', '/tokens/', self._token)])
        app.router.add_routes([web.route('GET', '/actiontypes', self._actiontypes)])
        app.router.add_routes([web.route('GET', '/actiontypes/', self._actiontypes)])
        app.router.add_routes([web.route('*', '/{tail:.*}', self._handler)])

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=self.listen_address.hostname, port=self.listen_address.port)
        await site.start()
        while True:
            await asyncio.sleep(10)


    async def _print_raw(self, request):
        body = await request.text()
        print("----------")
        print(body)
        print("----------\n")

    async def _print_json(self, request):
        body = await request.json()
        print("----------")
        print(json.dumps(body, indent=4))
        print("----------")

    async def _token(self, request):
        print("============ token")
        return web.json_response({
            'token': "abcdefghijklmnopqrstuvwxyz",
            'chaussures': {
                    'type': "basses",
                    'pointure': 41
                }
            })

    async def _actiontypes(self, request):
        print("============ actiontypes")
        return web.json_response([{"id": 1, "type": "offer"}, {"id": 2, "type": "bid"}])

    async def _handler(self, request):
        log.warning(f"{request.method} - {request.url}")

        if self.print_headers:
            print("==== Headers")
            for name, value in request.headers.items():
                print(f'{name}: {value}')
            print("====")

        if self.print_body:
            if self.pretty_print_json:
                try:
                    await self._print_json(request)
                except json.decoder.JSONDecodeError:
                    await self._print_raw(request)
            else:
                await self._print_raw(request)

        return web.Response(status=self.response_code)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--listen', "-l", help="listen address", default='localhost:8080')
    parser.add_argument('--pretty-print-json', action='store_true')
    parser.add_argument('--print-body', action='store_true')
    parser.add_argument('--response-code', type=int, default=200)
    parser.add_argument('--print-headers', action='store_true')

    config = parser.parse_args()


    log.basicConfig(level='WARN',
                    format="%(asctime)s|%(filename)s:%(lineno)s|%(funcName)s|%(levelname)s|%(message)s",
                    stream=sys.stdout)

    app = Tranquillou(config)
    asyncio.run(app.run())
