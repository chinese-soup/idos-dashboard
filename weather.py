import requests
from config import Configuration

class Weather:
    @staticmethod
    def get_weather():  # move to a seperate module
        pocasi = None
        params = {"q": "Prague",
                  "appid": Configuration.weatherAppID,
                  "units": "metric",
                  "lang": "cz"}

        req = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)

        if req.status_code == 200:
            try:
                parsed = req.json()
                pocasi = {"success": True, "message": "200"}
                if "main" in parsed:
                    pocasi["icon"] = parsed["weather"][0]["icon"]
                    pocasi["teplota"] = parsed["main"]["temp"]
                    pocasi["vlhkost"] = parsed["main"]["humidity"]

                if "wind" in parsed:
                    pocasi["vitr_rychlost"] = parsed["wind"]["speed"]
                    pocasi["vitr_uhel"] = parsed["wind"]["deg"]

                if "weather" in parsed:
                    pocasi["popis"] = parsed["weather"][0]["description"]

            except Exception as exp:
                pocasi = {"success": False, "message": str(exp)}

        else:
            pocasi = {"success": False, "message": "Non-OK code returned."}

        return pocasi
