# URL Shortener Project

A simple URL shortener built with **Flask** and **SQLite**, featuring a web interface. Users can shorten long URLs, optionally create custom short codes, and track clicks. The project can run **locally** or inside **Docker containers**.

---

## Features

- Shorten long URLs.
- Optional custom short codes.
- Redirect short URLs to the original URL.
- Track click counts for each short URL.
- Store URLs in a SQLite database.
- Recent links displayed on the homepage.
- Dockerized for easy deployment.

---

## Project Structure

'''
url-shortener/
│
├── app/
│ ├── init.py # Flask app factory
│ ├── models.py # Database connection and initialization
│ ├── routes.py # Flask routes
│ ├── services.py # Business logic (short URL creation)
│ ├── utils.py # Helper functions (normalize URL, base62 encoding)
│ └── templates/
│ └── index.html # HTML template for homepage
│
├── instance/
│ └── urlshort.db # SQLite database file (auto-created)
│
├── static/
│ └── css/
│ └── style.css # Optional styling
│
├── requirements.txt # Python dependencies
├── run.py # Entry point to start the Flask app
├── Dockerfile # Dockerfile for building the image
└── docker-compose.yml # Docker Compose configuration
'''