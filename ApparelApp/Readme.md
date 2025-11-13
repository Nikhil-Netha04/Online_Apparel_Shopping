# OnlineApparel

A small Django e-commerce demo for browsing products, serving static/media files, and basic admin management.

What this project is
- A Django project located at [OnlineApparel/manage.py](OnlineApparel/manage.py) with settings in [`Apparel.settings`](OnlineApparel/Apparel/settings.py).
- Main app: [`ApparelApp`](OnlineApparel/ApparelApp/) containing product models, views, templates and static assets:
  - Models: [`ApparelApp.models`](OnlineApparel/ApparelApp/models.py)
  - Views: [`ApparelApp.views`](OnlineApparel/ApparelApp/views.py)
  - App URLs: [OnlineApparel/ApparelApp/urls.py](OnlineApparel/ApparelApp/urls.py)
  - Admin registration: [OnlineApparel/ApparelApp/admin.py](OnlineApparel/ApparelApp/admin.py)
  - Templates: [OnlineApparel/ApparelApp/templates/](OnlineApparel/ApparelApp/templates/)
  - Static files: [OnlineApparel/ApparelApp/static/](OnlineApparel/ApparelApp/static/)

What it uses
- Python + Django (see [OnlineApparel/requirements.txt](OnlineApparel/requirements.txt))
- Project settings and URL routing in [OnlineApparel/Apparel/urls.py](OnlineApparel/Apparel/urls.py) and WSGI at [`Apparel.wsgi`](OnlineApparel/Apparel/wsgi.py).
- Environment config file: [OnlineApparel/.env](OnlineApparel/.env)
- Local SQLite DB: [OnlineApparel/db.sqlite3](OnlineApparel/db.sqlite3)
- Static assets collected to [staticfiles/](staticfiles/) and uploaded media under [media/](media/). Sample images in [sampleimages/](sampleimages/).

Quick start (development)
1. Create and activate a virtual environment:
   - python -m venv .venv
   - source .venv/bin/activate  (Windows: .venv\Scripts\activate)

2. Install dependencies:
   - pip install -r OnlineApparel/requirements.txt

3. Configure environment:
   - Copy or edit [OnlineApparel/.env](OnlineApparel/.env) to set SECRET_KEY, DEBUG, DB settings, etc.

4. Apply migrations and create a superuser:
   - python OnlineApparel/manage.py migrate
   - python OnlineApparel/manage.py createsuperuser

5. Run development server:
   - python OnlineApparel/manage.py runserver
   - Open http://127.0.0.1:8000

Testing
- Run the test suite: python OnlineApparel/manage.py test (tests are in [OnlineApparel/ApparelApp/tests.py](OnlineApparel/ApparelApp/tests.py)).

Notes
- Edit app code in [OnlineApparel/ApparelApp/](OnlineApparel/ApparelApp/).
- Adjust production settings in [`Apparel.settings`](OnlineApparel/Apparel/settings.py) (set DEBUG=False, configure DB/static/media).
- Use [OnlineApparel/manage.py](OnlineApparel/manage.py) for common Django management commands.

Files of interest
- [OnlineApparel/manage.py](OnlineApparel/manage.py)
- [`Apparel.settings`](OnlineApparel/Apparel/settings.py)
- [OnlineApparel/Apparel/urls.py](OnlineApparel/Apparel/urls.py)
- [`Apparel.wsgi`](OnlineApparel/Apparel/wsgi.py)
- [`ApparelApp.models`](OnlineApparel/ApparelApp/models.py)
- [`ApparelApp.views`](OnlineApparel/ApparelApp/views.py)
- [OnlineApparel/ApparelApp/urls.py](OnlineApparel/ApparelApp/urls.py)
- [OnlineApparel/requirements.txt](OnlineApparel/requirements.txt)
- [OnlineApparel/.env](OnlineApparel/.env)
- [OnlineApparel/db.sqlite3](OnlineApparel/db.sqlite3)
- [staticfiles/](staticfiles/) • [media/](media/) • [sampleimages/](sampleimages/)

License
- Add license text here.