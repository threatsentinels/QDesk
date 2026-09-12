# QDesk

A simple web-based queue management system for events, offices, service desks, and other places where people have to wait.



## Features

- Generate queue tokens automatically
- Call the next person in line
- Assign tokens to service counters
- Mark tokens as finished
- Track waiting, serving, and completed tokens
- Public display for currently serving tokens
- Printable tokens
- Basic queue statistics
- Support for multiple organizations and events
- Live queue updates

## How it works

```
Organization
     ↓
   Event
     ↓
  Counters
     ↓
   Tokens

A typical flow looks like:

Generate Token → Wait → Called → Go to Counter → Finished text
```

Tech Stack
```
Django
HTML / CSS
HTMX
SQLite
Pillow
Gunicorn
```
Live Demo

```https://qdesk-q7k7.onrender.com/```

Running Locally

Clone the repository:
```
git clone https://github.com/threatsentinels/QDesk.git
cd QDesk
```

Create a virtual environment:
```
python -m venv venv
```
Activate it and install the requirements:
```
pip install -r requirements.txt
```
Run migrations:
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
Then open the local address shown in the terminal.

Project Structure
```
QDesk/
├── config/
├── organizations/
├── events/
├── counters/
├── tokens/
├── templates/
├── staticfiles/
├── manage.py
└── requirements.txt
```

Status

QDesk is an ongoing project. More features and improvements are planned.
