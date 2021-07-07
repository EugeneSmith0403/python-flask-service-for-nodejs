import pika, sys, os

import requests
import json


class RabbitMq:
    def init(self):
        params = pika.ConnectionParameters(host='localhost')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare('users')

        def callback(ch, method, properties, body):
            data = dict(json.loads(body))
            self.sendToApi(data)

        channel.basic_consume('users', callback, False)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.start_consuming()

    def sendToApi(self, result):
        url = 'http://127.0.0.1:5000/users'
        print(result)
        action = result['action']
        data = result['data'][0]
        res = None

        if action == "create":
            res = requests.post(url, json=data)
        if action == "update":
            res = requests.put(url, json=data)
        print(res)


if __name__ == '__main__':
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
