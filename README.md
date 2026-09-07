# QDesk

QDesk is a lightweight queue and token management system for managing queues at events, offices, service counters, health camps, and other places where people need to wait for their turn.

It provides tools for generating and managing tokens, operating counters, tracking token status, displaying the current queue publicly, and monitoring basic queue statistics.

## Features

* Organization and event management
* Multiple counters per event
* Configurable token prefixes
* Configurable starting token numbers
* Sequential token generation
* Queue dashboard
* Call-next queue control
* Token status tracking
* Token completion tracking
* Token cancellation support
* Token printing
* Public queue display
* Live queue updates with HTMX
* Average waiting-time calculation
* Average service-time calculation
* Django admin support

## Tech Stack

| Component    | Technology                     |
| ------------ | ------------------------------ |
| Backend      | Django                         |
| Frontend     | Django Templates, Tailwind CSS |
| Live updates | HTMX                           |
| Database     | SQLite / PostgreSQL            |
| Web Server   | Passenger / WSGI               |
| Deployment   | cPanel                         |
| Language     | Python 3.12+                   |

## Project Structure

```text
QDesk/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── organizations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── events/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── counters/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── tokens/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── manage.py
├── requirements.txt
└── passenger_wsgi.py
```

## Requirements

Before installing QDesk, make sure you have:

* Python 3.12 or newer
* pip
* Git
* A virtual environment
* SQLite or PostgreSQL
* A modern web browser

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd QDesk
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file or configure the variables through your hosting environment.

Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
```

For production, use a long randomly generated secret key and set:

```env
DJANGO_DEBUG=False
```

Do not commit your `.env` file or production secret key to Git.

### 5. Configure Django settings

Update `config/settings.py` for your environment.

For local development:

```python
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
```

For production, add your actual domain:

```python
ALLOWED_HOSTS = [
    "example.com",
]
```

If the application is served over HTTPS, configure the appropriate CSRF trusted origins:

```python
CSRF_TRUSTED_ORIGINS = [
    "https://example.com",
]
```

## Database Setup

Run Django migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

## Static Files

For production deployments, collect static files with:

```bash
python manage.py collectstatic --noinput
```

The collected files will be placed in the directory configured by `STATIC_ROOT`.

Example:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

## Media Files

QDesk supports uploaded organization logos.

Configure media storage in `settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Make sure the media directory exists and is writable by the application.

During local development, media files can be served through Django's development server.

## Running Locally

Start the development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

To allow access from other devices on the same network:

```bash
python manage.py runserver 0.0.0.0:8000
```

## Basic Usage

### 1. Create an Organization

Create an organization from the application or Django admin.

An organization can contain multiple events.

### 2. Create an Event

An event belongs to an organization and contains the queue configuration.

Example:

```text
Event: Health Camp
Location: Main Hall
Token Prefix: HC
Starting Number: 1
```

Tokens generated for this event will look like:

```text
HC-001
HC-002
HC-003
```

### 3. Create Counters

Create one or more counters for the event.

For example:

```text
Counter 1
Counter 2
Counter 3
```

### 4. Generate Tokens

When a visitor joins the queue, generate a token from the event dashboard.

Tokens are automatically numbered sequentially.

### 5. Call the Next Token

The queue operator can use **Call Next** to move the next waiting token into the serving state.

The token lifecycle is:

```text
WAITING
   ↓
SERVING
   ↓
FINISHED
```

A token can also be cancelled when necessary:

```text
WAITING → CANCELLED
```

### 6. Public Display

The public display provides a separate interface for visitors to see the currently serving token and the upcoming queue.

It can be opened on a separate screen, monitor, or device.

## Token States

| Status      | Description                     |
| ----------- | ------------------------------- |
| `WAITING`   | Token is waiting in the queue   |
| `SERVING`   | Token is currently being served |
| `FINISHED`  | Service has been completed      |
| `CANCELLED` | Token has been cancelled        |

## Queue Statistics

QDesk tracks basic queue performance information, including:

* Total tokens
* Waiting tokens
* Currently serving tokens
* Finished tokens
* Average waiting time
* Average service time

Waiting time is calculated from token generation until it is called.

Service time is calculated from when service starts until the token is finished.

## HTMX Updates

QDesk uses HTMX to update queue information without requiring a full page reload.

Queue actions such as generating and calling tokens can update the dashboard dynamically.

## Production Deployment

QDesk can be deployed using any Django-compatible WSGI server.

For cPanel hosting with Passenger, the application can be configured with:

```text
Application Root:
QDesk
```

```text
Startup File:
passenger_wsgi.py
```

```text
Entry Point:
application
```

A basic `passenger_wsgi.py`:

```python
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
```

After installing dependencies:

```bash
pip install -r requirements.txt
```

run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py check
```

Then restart the application through the hosting control panel.

## Production Settings

Before deploying to production:

```python
DEBUG = False
```

Use a secure `SECRET_KEY` and configure:

```python
ALLOWED_HOSTS = [
    "your-domain.com",
]
```

For HTTPS:

```python
CSRF_TRUSTED_ORIGINS = [
    "https://your-domain.com",
]
```

Secure cookies should also be enabled when the entire application is served through HTTPS:

```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

Additional security settings such as HSTS should only be enabled after confirming that the entire domain and its required subdomains are permanently HTTPS-only.

## Email

Email functionality is not required for the core queue system.

If email features are added later, configure Django's email backend using a production SMTP service rather than Django's console email backend.

## Development Checks

Before committing changes, run:

```bash
python manage.py check
```

For production configuration checks:

```bash
python manage.py check --deploy
```

The deployment check may report warnings for optional security settings depending on the hosting environment.

## License

Add the project's license here.

For example:

```text
MIT License
```

if the project is intended to be released under the MIT License.
