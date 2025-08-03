from flask import Flask, request, send_file
from subprocess import Popen, PIPE
import os
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = str(request.args.get("url"))

    if url == "None":
        return "You didn't send anything you dummie!"

    if not("https://open.spotify.com/track/" in url):
        return "I can't help you if you don't want to send valid Spotify track URL"

    with open("/home/toustik/AUDIO01.txt", "a") as f:
        f.write("Toto bude zvukový soubor\n")

    while not(os.path.exists("/home/toustik/AUDIO01.txt")):
        print("Čekám na soubor")
        time.sleep(0.1)

    return send_file("/home/toustik/AUDIO01.txt")

