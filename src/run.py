import os
from flask import Flask

from src.hardware.moisture_sensor import MoistureSensor


app = Flask(__name__)
moisture_sensor = MoistureSensor()


@app.route("/")
def hello():
    return "Hello!"


@app.route("/moisture")
def moisture():
    moisture_sensor.probe()
    return 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host="0.0.0.0", port=port)

