FarmerBasket Django starter (ready-to-run scaffold using your uploaded HTML design)

How to run:
1) python -m venv venv
2) source venv/bin/activate  (or venv\Scripts\activate on Windows)
3) pip install -r requirements.txt
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver

This package includes a static/ folder and media/ to avoid STATICFILES_DIRS warnings.
