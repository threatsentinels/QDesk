**QDesk**

Standing around in a crowded room wondering which token just got called is pretty annoying. I built QDesk to fix that, making a simple web app for managing lines at events, service desks, pop-up clinics, and offices.

You set up an event, issue tokens, call the next person up, and throw a display up on a screen so people actually know where they are in line.

The app supports multiple organizations, events, and counters. Tokens get custom prefixes, automatic numbering, and can be printed out. Staff get a real-time dashboard while visitors see a clean public display in the waiting room. Everything tracks token statuses through waiting, serving, finished, or cancelled, and gives you basic stats on wait times.

On the coding paart, I splited the backend into modular Django apps for organizations, events, counters, and tokens instead of stuffing everything into one giant views.py. The backend runs on Python, Django, and SQLite, while the frontend uses Django Templates and Tailwind CSS. HTMX handles the live updates so the page never has to fully reload when a token changes.

To run it locally:

git clone https://github.com/threatsentinels/QDesk.git
cd QDesk

python -m venv venv
source venv/bin/activate (or venv\Scripts\activate on Windows)

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Then open http://127.0.0.1:8000 in your browser.

You can test the live build at https://qdesk.ggsrclub.com

Down the road I want to add better auth, real reporting features, multi-counter routing, and cleaner display styles.
