import requests


def fetch_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current"]

        report = (
            "Weather Report\n"
            f"Timezone: {data['timezone']}\n"
            f"Temperature: {current['temperature_2m']} "
            f"{current['units']['temperature_2m']}\n"
            f"Windspeed: {current['wind_speed_10m']} "
            f"{current['units']['wind_speed_10m']}\n"
            f"Weather Code: {current['weather_code']}\n"
        )

        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

        print(report)

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
    except (KeyError, ValueError) as error:
        print("Invalid weather data:", error)


if __name__ == "__main__":
    fetch_weather(19.0760, 72.8777)
