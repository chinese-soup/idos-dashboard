import datetime
import time
import toml

from flask import Flask, render_template
from weather import Weather
from idospy import IDOSAdapter
from config import Configuration

app = Flask(__name__)
idos = IDOSAdapter("ABCz", Configuration.userID, Configuration.userDesc)

def get_idos_data():
    results = []
    for trasa in Configuration.trasy:
        result = idos.find_connection_simple(trasa[0], trasa[1], count=15)
        results.append(result)

    return results

@app.route('/')
def homepage():
    pocasi = Weather.get_weather()
    trasy = get_idos_data()
    return render_template("tabule.html", pocasi=pocasi, trasy=trasy, time=datetime.datetime.now())


if __name__ == '__main__':
    app.run(debug=True)
