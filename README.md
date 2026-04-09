# WBTech Shop Backend

Backend-сервис интернет-магазина на Django и Django REST Framework.

Реализованы аутентификация по JWT, работа с профилем пользователя, каталог товаров, корзина, оформление заказов и документация API через Swagger.

---

## Технологии

- Python 3.11
- Django 4.2
- Django REST Framework
- JWT authentication
- PostgreSQL / SQLite
- drf-spectacular (OpenAPI / Swagger)
- Pytest
- Docker

---

## Основные возможности

- Регистрация и авторизация пользователей
- JWT-аутентификация
- Работа с профилем пользователя
- Каталог товаров
- Управление корзиной
- Оформление заказов
- Разграничение прав доступа для административных операций
- Swagger UI для тестирования API

---

## API overview

- `POST /api/auth/register/` — регистрация пользователя  
- `POST /api/auth/login/` — получение JWT токена  
- `POST /api/auth/refresh/` — обновление токена  
- `GET /api/auth/me/` — профиль текущего пользователя  
- `POST /api/auth/me/top-up/` — пополнение баланса  

- `/api/products/` — работа с товарами  
- `/api/cart/items/` — корзина  
- `POST /api/orders/create-from-cart/` — создание заказа  
- `GET /api/orders/` — список заказов  

Swagger UI доступен по адресу:  
`http://127.0.0.1:8000/api/docs/`

---

## Бизнес-логика

Оформление заказа реализовано как атомарная операция:

- проверка доступности товаров  
- проверка баланса пользователя  
- списание средств  
- создание заказа и позиций  
- очистка корзины  

Это гарантирует консистентность данных и корректное выполнение операции.

---

## Local run

### Требования

- Python 3.11+
- pip
- virtualenv (рекомендуется)

### Установка и запуск

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


### Docker запуск
```
docker compose up --build
```

### Тестирование
```
pytest
```

### Структура проекта
```
wbtech_shop/
├── apps/           # бизнес-логика (users, products, orders)
├── config/         # настройки проекта
├── scripts/        # вспомогательные скрипты
├── manage.py
└── requirements.txt
