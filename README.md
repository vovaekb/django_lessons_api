# django_lessons_api
:books: Simple REST API application on Python Django REST Framework.

Features:
- admin panel with ability to edit lessons detail
- list group lessons in JSON format

## Run application
Clone the repo, change to the project root folder. Install dependencies from requirements.txt file:

```bash
pip install -r requirements.txt
```
Run the application:
```bash
python manage.py runserver
```

Open admin panel: http://127.0.0.1:8000/admin. Under admin account you can edit lessons and teachers in database. 

To see lessons API data open page:  http://127.0.0.1:8000/api/lessons/.
