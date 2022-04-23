#!/usr/bin/env python

import asyncio
import time
import websockets

async def hello(x, string):
    async with websockets.connect("ws://localhost:8765") as websocket:
        for _ in range(100):
            await websocket.send(string)
            await websocket.recv()

async def main(x):
    string = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."
    string2 = "Hi"
    coros = [hello(i, string) for i in range(x)]
    await asyncio.gather(*coros)

if __name__ ==  '__main__':
    for i in range(7000, 12000, 100):
        t1 = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(i))
        used = time.time() - t1
        print(i,  used/i)