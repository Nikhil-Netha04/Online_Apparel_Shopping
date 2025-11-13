# Online Apparel Shopping System

A full‑stack Django web application that provides a simple, convenient platform for browsing, searching, and purchasing apparel. Users can search products by type, brand, and style, add items to a cart, and complete a basic checkout flow. Administrators can manage products via the Django admin.

## Key features
- Product catalog with search and filters (type, brand, style)
- Product detail pages and images
- Cart management (add/remove/update)
- Simple checkout flow (order creation)
- Admin interface for product and order management
- Static and media file handling for assets and uploads

## Technology stack
- Python 3.8+
- Django (see requirements.txt)
- SQLite (default local DB; configurable)
- HTML/CSS templates and static assets

## Repository layout (high level)
- OnlineApparel/manage.py
- OnlineApparel/Apparel/ (project settings, urls, wsgi)
- OnlineApparel/ApparelApp/ (main app: models, views, templates, static)
- staticfiles/, media/, sampleimages/
- OnlineApparel/requirements.txt, .env, db.sqlite3

## Quick start (development)
1. Open a terminal in the project root:
   - Windows PowerShell / CMD:
     .venv\Scripts\activate
   - or:
     python -m venv .venv
     .venv\Scripts\activate

2. Install dependencies:
   pip install -r OnlineApparel/requirements.txt

3. Configure environment:
   - Copy OnlineApparel/.env.example or create OnlineApparel/.env and set SECRET_KEY, DEBUG, DB settings as needed.

4. Database setup:
   python OnlineApparel/manage.py migrate
   python OnlineApparel/manage.py createsuperuser

5. Run server:
   python OnlineApparel/manage.py runserver
   Open http://127.0.0.1:8000

## Testing
Run the test suite:
python OnlineApparel/manage.py test

## Deployment notes
- Set DEBUG=False and provide a secure SECRET_KEY via environment variables.
- Use a production database (PostgreSQL, MySQL) and configure STATIC/MEDIA serving (e.g., collectstatic + CDN or web server).
- Configure allowed hosts and HTTPS for production.

## Contributing
- Fork, create a feature branch, add tests, and open a pull request.
- Keep feature scope small and document changes.

## License
Specify a license (e.g., MIT) or add your preferred license file.
