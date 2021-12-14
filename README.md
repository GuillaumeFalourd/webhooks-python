# webhooks-python

POC of sending and receiving webhooks in Python 🐍

## References

- [How to Send Webhooks with Python](https://www.youtube.com/watch?v=X-_25tzo8Cw&ab_channel=DevOpsJourney)
- [How to Receive Webhooks with Python](https://www.youtube.com/watch?v=HQLRPWi2SeA&ab_channel=DevOpsJourney)

## Usage

First, if you don't have the dependencies installed on your computer, run:

```shell
pip install -r requirements.txt
```

### Sender (Remote)

You will be able to send a webhook request remotely running the `webhook_remote.py` file by using `python webhook_remote.py`.

_Note: You can update the webhook online url on the `webhook_remote.py` file by creating your own for free on the [Webhook site](https://webhook.site/)._

#### Demo Sender (Remote)

```shell
➜ python webhook_remote.py
Success
```

<img width="1427" alt="Screen Shot 2021-12-14 at 10 31 24" src="https://user-images.githubusercontent.com/22433243/146008397-addda76d-98fe-4042-ad9a-396eed500cac.png">

### Receiver

You will be able to run the server by using `python server.py`.

#### Demo Receiver

```shell
➜  python server.py
 * Serving Flask app 'server' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Accessing the `http://127.0.0.1:5000/` on your navigator, you'll see somthing like this:

TODO: <image>

### Sender (Local)

You will be able to send a webhook request locally to the server above running the `webhook_local.py` file by using `python webhook_local.py` (on another terminal than the one where the `server.py` script is running).

#### Demo Sender (Local)

```shell
➜ python webhook_local.py
Success
```

If you do so, the terminal with the server.py script running will return the JSON he received:

```shell
➜  python server.py
 * Serving Flask app 'server' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
{'name': 'Guillaume', 'phone': '+553499999-9999', 'email': 'guillaume@test.com'}
127.0.0.1 - - [14/Dec/2021 10:48:06] "POST /webhook HTTP/1.1" 200 -
```
