# Library API

Простий REST API для управління бібліотекою книг, створений за допомогою FastAPI.

## Встановлення

1. Створіть віртуальне середовище:
```bash
python -m venv venv
```

2. Активуйте віртуальне середовище:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

## Запуск

Запустити сервер можна одним із способів:

1. Через Python:
```bash
python -m library_api
```

2. Через Uvicorn:
```bash
uvicorn library_api.main:app --reload
```

Сервер буде доступний за адресою: http://127.0.0.1:8000

## API Документація

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Доступні ендпоінти

- `GET /api/books` - отримати список всіх книг
- `GET /api/books/{book_id}` - отримати книгу за ID
- `POST /api/books` - додати нову книгу
- `DELETE /api/books/{book_id}` - видалити книгу за ID

## Приклад використання

### Додавання нової книги
```bash
curl -X POST "http://127.0.0.1:8000/api/books" \
     -H "Content-Type: application/json" \
     -d '{"title": "New Book", "author": "Author Name", "year": 2024}'
```

### Отримання всіх книг
```bash
curl "http://127.0.0.1:8000/api/books"
```

## Залежності

- FastAPI
- Uvicorn
- Pydantic 