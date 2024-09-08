# VidSubExplorer

## Description

This is a Django-based web application that allows users to upload videos, extract subtitles using **CCExtractor**, search for specific phrases within the subtitles, and view the video starting from the timestamp of the search result. The application also supports multiple languages for subtitles.

The backend is developed using Django and PostgreSQL for data storage, and the entire application is containerized using Docker for easy setup and deployment.

## Features

- **Video Upload**: Users can upload videos to the server.
- **Subtitle Extraction**: Subtitles are extracted from the video using **CCExtractor**.
- **Multiple Language Subtitles**: The application supports subtitle extraction in different languages.
- **Search Functionality**: Users can search for phrases within the subtitles, and the video will play from the timestamp where the phrase occurs.
- **List View**: Displays all uploaded videos, allowing users to select and watch them with subtitles.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Subtitle Extraction**: CCExtractor
- **Containerization**: Docker, Docker Compose
- **Frontend**: Simple HTML/CSS (Django Templates)
- **Asynchronous Processing**: Celery (optional, for background tasks)

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.
- **CCExtractor** installed locally for subtitle extraction.
  - Install via command line: 
    ```bash
    sudo apt-get install ccextractor
    ```

## Project Structure

```plaintext
VidSubExplorer/
│
├── docker-compose.yml        # Docker Compose file for multi-container setup
├── Dockerfile                # Dockerfile to build the Django app
├── manage.py                 # Django project management script
├── VidSubExplorer/          # Django project folder
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project URL routing
│   ├── wsgi.py
│   └── asgi.py
└── videos/                   # Django app for video processing
    ├── migrations/
    ├── templates/            # HTML templates for frontend
    │   └── videos/
    │       ├── upload.html   # Video upload page
    │       ├── list.html     # List of uploaded videos
    │       └── detail.html   # Video detail view with subtitles
    ├── __init__.py
    ├── admin.py              # Django admin configuration
    ├── apps.py
    ├── forms.py              # Video upload form
    ├── models.py             # Database models for Video and Subtitle
    ├── urls.py               # App-level URL routing
    ├── views.py              # Business logic for video upload, subtitle extraction, and search
