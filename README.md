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


---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/jthhn/IOSS.git
cd IOSS
```


2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt


# Setup Instructions (Docker)
1. Build and start the project
docker-compose up --build


This builds the Docker image and starts the container.

Flask will run inside the container and bind to http://localhost:5000.

Open your browser at:

http://127.0.0.1:5000

2. Stop the container
docker-compose down


Your data persists in ./instance/urlshort.db.

Usage

Paste a long URL in the input box.

Optionally, enter a custom short code.

Click Shorten.

The page will display your short URL: