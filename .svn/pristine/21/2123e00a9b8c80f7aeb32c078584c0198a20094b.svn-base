import asyncio
import websockets
import logging

websockets_sesstion=set()
async def echo(websocket, path):
    websockets_sesstion.add(websocket)
    async for message in websocket:
        await websocket.send(pathSwitch(path,message))


def start(host="0.0.0.0",port=5228):
    logging.debug("启动websocket...")  
    try:
        start_server = websockets.serve(echo, host, port)
    except Exception:
        logging.error("ws服务启动失败!")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    logging.debug(f"启动websocket服务完成：ws//{host}:{port}")

def pathSwitch(path,message):
    print(path)
    return message