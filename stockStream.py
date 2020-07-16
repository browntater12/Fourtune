import config
import websocket, json
import csv
#Must run in terminal
#30 connections max

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.KEY_ID, "secret_key": config.SECRET_ID}
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "listen", "data": {"streams": ["T.TSLA"]}}

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("received a message")
    print(message)
    with open("TSLA.csv", "a") as file:
        writer = csv.writer(file, delimiter="")
        writer.writerow(data)
        print("written to csv")



def on_close(ws):
    print("closed connection")



socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()