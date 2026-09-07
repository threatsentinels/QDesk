QDesk

Queue management without the chaos.

QDesk started with a pretty simple idea: why are people still standing around asking which token is being called?

So I made a small web app for handling queues at events, service desks, health camps, offices, and basically anywhere people have to wait for their turn.

You create an event, generate tokens, call people from the queue, and keep track of what's happening. There's also a separate public display for showing the current token.

Nothing too fancy. Just a queue that works.

What it has

- Organizations and events
- Multiple counters
- Custom token prefixes
- Automatic token numbering
- Queue dashboard
- Call next / finish token
- Token printing
- Public display
- Live updates
- Basic waiting & service time stats

The token flow is basically:

WAITING → SERVING → FINISHED

with cancellation when needed.

A little tech

It's built with Django, with HTMX handling the small live updates so the whole dashboard doesn't need to reload every time something happens.

The frontend is mostly Django templates with Tailwind CSS.

Current stack:

Python
Django
HTMX
Tailwind CSS
SQLite

The project is split into a few small Django apps instead of putting everything into one giant "views.py" and hoping for the best:

organizations/
events/
counters/
tokens/

Running it

If you want to try it locally:

git clone https://github.com/threatsentinels/QDesk.git
cd QDesk

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Then open:

http://127.0.0.1:8000

For Windows, activate the environment with:

venv\Scripts\activate

Demo

The current deployment is available at:

https://qdesk.ggsrclub.com

What's next?

There are still plenty of things I'd like to add.

Better counter handling, authentication, proper reporting, a nicer public display, and probably a bunch of other things I'll think of after using it for a while.

For now, it does what it was supposed to do.

That's good enough.
