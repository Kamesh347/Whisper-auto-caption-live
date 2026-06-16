# import soundcard as sc
# import soundfile as sf
# import subprocess
# import os
# import time
# import warnings
# from soundcard.mediafoundation import SoundcardRuntimeWarning

# # websockets.serve(
# #     handler,
# #     "0.0.0.0",
# #     8765
# # )

# warnings.filterwarnings(
#     "ignore",
#     category=SoundcardRuntimeWarning
# )





# SAMPLERATE = 16000
# CHUNK_SECONDS = 3

# WHISPER = r"build\bin\Release\whisper-cli.exe"
# MODEL = r"models\ggml-tiny.en.bin"

# mic = sc.get_microphone("Stereo Mix", include_loopback=True)

# print("Live transcription started...\n")

# with mic.recorder(samplerate=SAMPLERATE) as recorder:

#     while True:
#         audio = recorder.record(numframes=SAMPLERATE * CHUNK_SECONDS)

#         sf.write("chunk.wav", audio, SAMPLERATE)

#         result = subprocess.run(
#             [
#                 WHISPER,
#                 "-m",
#                 MODEL,
#                 "-f",
#                 "chunk.wav",
#                 "--no-timestamps",
#                 "-np"
#             ],
#             capture_output=True,
#             text=True
#         )

#         text = result.stdout.strip()

#         if text:
#             print(text)

    

import asyncio
import subprocess
import warnings

import soundcard as sc
import soundfile as sf
import websockets

from soundcard.mediafoundation import SoundcardRuntimeWarning

warnings.filterwarnings(
    "ignore",
    category=SoundcardRuntimeWarning
)

SAMPLERATE = 16000
CHUNK_SECONDS = 3

WHISPER = r"build\bin\Release\whisper-cli.exe"
MODEL = r"models\ggml-tiny.en.bin"

clients = set()


async def broadcast(message):

    dead = []

    for client in clients:
        try:
            await client.send(message)
        except:
            dead.append(client)

    for client in dead:
        clients.remove(client)


async def websocket_handler(websocket):

    clients.add(websocket)

    print("Client Connected")
    print("Total Clients:", len(clients))

    try:
        await websocket.wait_closed()
    finally:
        clients.remove(websocket)

        print("Client Disconnected")
        print("Total Clients:", len(clients))


async def transcribe_loop():

    mic = sc.get_microphone(
        "Stereo Mix",
        include_loopback=True
    )

    print("Live transcription started...\n")

    with mic.recorder(
            samplerate=SAMPLERATE
    ) as recorder:

        while True:

            audio = recorder.record(
                numframes=SAMPLERATE * CHUNK_SECONDS
            )

            sf.write(
                "chunk.wav",
                audio,
                SAMPLERATE
            )

            result = subprocess.run(
                [
                    WHISPER,
                    "-m",
                    MODEL,
                    "-f",
                    "chunk.wav",
                    "--no-timestamps",
                    "-np"
                ],
                capture_output=True,
                text=True
            )

            text = result.stdout.strip()

            if text:

                print(text)

                await broadcast(text)

            await asyncio.sleep(0.01)


async def main():

    server = await websockets.serve(
        websocket_handler,
        "0.0.0.0",
        8765
    )

    print("WebSocket Running")
    print("ws://0.0.0.0:8765")

    await transcribe_loop()

    await server.wait_closed()


asyncio.run(main())