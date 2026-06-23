# Weather App
# Weather App

A simple weather app built to learn DevOps fundamentals.

Live at: https://devops.martynas.online

## What it does

Shows current weather for Wroclaw  temperature, description, humidity, and feels like.

## Stack

- Python + Flask
- Docker + Docker Compose
- Nginx (reverse proxy)
- Let's Encrypt (SSL)
- Hosted on Hetzner VPS

## Project structure

```
weather-app/
 app/
    app.py
    requirements.txt
    templates/
        index.html
 nginx/
    nginx.conf
 docker-compose.yml
 .env (not committed)
```

## Running locally

Clone the repo, add a `.env` file with your OpenWeatherMap API key:

```
WEATHER_API_KEY=your_key_here
CITY=Wroclaw
```

Then:

```bash
docker-compose up -d
```

Visit `http://localhost`

## Author

Martynas  learning DevOps

