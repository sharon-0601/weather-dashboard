# # # from flask import Flask, render_template
# # # import requests
# # #
# # # app = Flask(__name__)
# # #
# # # API_KEY = "a35f07db7411913780191cdce6d6c301"  # your key
# # # cities = ["Berlin", "Munich", "Hamburg"]
# # #
# # # # ✅ Only one get_weather function with error handling
# # # def get_weather(city):
# # #     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
# # #     response = requests.get(url).json()
# # #
# # #     # Check if API returned weather data
# # #     if "main" in response:
# # #         data = {
# # #             "city": city,
# # #             "temperature": response["main"]["temp"],
# # #             "description": response["weather"][0]["description"]
# # #         }
# # #     else:
# # #         # Handle missing data (city not found or API error)
# # #         data = {
# # #             "city": city,
# # #             "temperature": "N/A",
# # #             "description": response.get("message", "No data")
# # #         }
# # #     return data
# # #
# # # @app.route('/')
# # # def home():
# # #     weather_data = [get_weather(city) for city in cities]
# # #     return render_template("index.html", weather_data=weather_data)
# # #
# # # if __name__ == "__main__":
# # #     app.run(debug=True, port=5001)  # use port 5001 instead of 5000
# #
# #
# # from flask import Flask, render_template
# # import requests
# #
# # app = Flask(__name__)
# #
# # API_KEY = "a35f07db7411913780191cdce6d6c301"  # replace with your OpenWeatherMap API key
# #
# # # 20 German cities
# # cities = [
# #     "Berlin", "Munich", "Hamburg", "Pforzheim", "Frankfurt",
# #     "Cologne", "Stuttgart", "Dresden", "Leipzig", "Düsseldorf",
# #     "Bremen", "Hannover", "Nuremberg", "Dortmund", "Essen",
# #     "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Mannheim"
# # ]
# #
# #
# # def get_weather(city):
# #     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
# #     response = requests.get(url).json()
# #
# #     if "main" in response:
# #         return {
# #             "city": city,
# #             "temperature": response["main"]["temp"],
# #             "description": response["weather"][0]["description"]
# #         }
# #     else:
# #         return {
# #             "city": city,
# #             "temperature": "N/A",
# #             "description": response.get("message", "No data")
# #         }
# #
# #
# # @app.route('/')
# # def home():
# #     weather_data = [get_weather(city) for city in cities]
# #     return render_template("index.html", weather_data=weather_data)
# #
# #
# # if __name__ == "__main__":
# #     app.run(debug=True, port=5001)
#
#
# from flask import Flask, render_template, jsonify
# import requests
#
# app = Flask(__name__)
#
# API_KEY = "a35f07db7411913780191cdce6d6c301"  # your OpenWeatherMap API key
#
# cities = [
#     "Berlin", "Munich", "Hamburg", "Pforzheim", "Frankfurt",
#     "Cologne", "Stuttgart", "Dresden", "Leipzig", "Düsseldorf",
#     "Bremen", "Hannover", "Nuremberg", "Dortmund", "Essen",
#     "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Mannheim"
# ]
#
#
# def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url).json()
#
#     if "main" in response:
#         return {
#             "city": city,
#             "temperature": response["main"]["temp"],
#             "description": response["weather"][0]["description"]
#         }
#     else:
#         return {
#             "city": city,
#             "temperature": "N/A",
#             "description": response.get("message", "No data")
#         }
#
#
# @app.route('/')
# def home():
#     return render_template("index.html")
#
#
# @app.route('/weather_data')
# def weather_data():
#     data = [get_weather(city) for city in cities]
#     return jsonify(data)
#
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = "a35f07db7411913780191cdce6d6c301"

cities = [
    "Berlin", "Munich", "Hamburg", "Pforzheim", "Frankfurt",
    "Cologne", "Stuttgart", "Dresden", "Leipzig", "Düsseldorf",
    "Bremen", "Hannover", "Nuremberg", "Dortmund", "Essen",
    "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Mannheim"
]


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if "main" in response:
        return {
            "city": city,
            "temperature": response["main"]["temp"],
            "description": response["weather"][0]["description"]
        }
    else:
        return {
            "city": city,
            "temperature": "N/A",
            "description": response.get("message", "No data")
        }


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/weather_data')
def weather_data():
    data = [get_weather(city) for city in cities]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)