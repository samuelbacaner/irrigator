import os
from pytz import utc
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from src.hardware.moisture_sensor import MoistureSensor
from src.models import MoistureReading
from src.storage import write_moisture_reading

# TODO add layered config store that uses env variables and a persisted config file


def check_moisture():
    print("checking moisture on timer")
    raw_value, voltage = moisture_sensor.probe()
    moisture_reading = MoistureReading(raw_value, voltage)
    write_moisture_reading(moisture_reading)


moisture_sensor = MoistureSensor()
job_defaults = {"coalesce": True}
scheduler = BackgroundScheduler(job_defaults=job_defaults, timezone=utc)
scheduler.add_job(check_moisture, "interval", seconds=600)
scheduler.start()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!\n"


@app.route("/moisture")
def moisture():
    _, _ = moisture_sensor.probe()
    return 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host="0.0.0.0", port=port)
