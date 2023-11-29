from datetime import datetime
from flask import Flask
import calendar


#DAYNAMES = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]

app = Flask(__name__)


@app.route("/")
def hello_world():

  now = datetime.now()
  #dayname = DAYNAMES[now.weekday()]
  dayname = calendar.day_name[now.weekday()]

  moon_landing = datetime(1969, 7, 20, 20, 17, 40)
  diff = now - moon_landing

  return f"<p>hello, world! Happy {dayname}. It has been {diff} since the Moon Landing</p>"
