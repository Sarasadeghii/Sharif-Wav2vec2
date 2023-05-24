#!/usr/bin/env python3

import asyncio
import websockets
import sys
import json
import librosa

sample_rate = 16000

async def run_test(uri):
    async with websockets.connect(uri) as websocket:

        wf, rate = librosa.load(
            sys.argv[1],
            sr=sample_rate)
        buffer_size = 64000
        
        for i in range(0, len(wf), buffer_size):
            data = wf[i: i+buffer_size].tobytes()
            
            if len(data) == 0:
                break

            await websocket.send(data)
            result = json.loads(await websocket.recv())
            print(result['text'])

        await websocket.send('{"eof" : 1}')
        result = await websocket.recv()
        print(result)

asyncio.run(run_test('ws://your IP address'))
