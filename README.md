# WBTech Shop Backend
Backend-сервис интернет-магазина на Django и Django REST Framework.  
Реализованы аутентификация по JWT, работа с профилем пользователя, каталог товаров, корзина, оформление заказов и документация API через Swagger.

## Технологии

- Python 3.11
- Django 4.2
- Django REST Framework
- JWT authentication
- PostgreSQL / SQLite
- drf-spectacular (OpenAPI / Swagger)
- Pytest
- Docker

## Основные возможности
- Регистрация и аутентификация пользователей
- JWT-доступ к защищенным endpoint’ам
- Работа с профилем пользователя
- Каталог товаров
- Управление корзиной
- Оформление заказов
- Разграничение прав доступа для административных операций
- Swagger UI для ручного тестирования API
  
---

## Local run

### Windows
1. Install Python 3.11
2. Create virtual environment
3. Install dependencies from `requirements-win.txt`
4. Apply migrations
5. Run development server

### Quick start
```powershell
.\scripts\setup.ps1
.\scripts\run.ps1
---

## 🧭 Что умеет API
- Регистрация: `POST /api/auth/register/`
- Вход (JWT): `POST /api/auth/login/`
- Обновление токена: `POST /api/auth/refresh/`
- Профиль: `GET /api/auth/me/`
- Пополнение баланса: `POST /api/auth/me/top-up/`
- Товары (CRUD только админ): `/api/products/`
- Корзина: `GET/POST /api/cart/items/` и `GET/PATCH/DELETE /api/cart/items/{id}/`
- Заказы из корзины: `POST /api/orders/create-from-cart/`, список: `GET /api/orders/`

Бизнес-логика создания заказа находится в `orders/services.py::create_order_from_cart()` и выполняется атомарно:
- проверка остатков,
- проверка баланса,
- списание баланса и остатков,
- создание заказа и позиций,
- очистка корзины,
- логирование (консоль + `logs.txt`).

---

## 🧪 Тесты
```powershell
.\scripts	est.ps1

```


## API overview

- `POST /api/auth/register/` — user registration
- `POST /api/auth/login/` — JWT login
- `POST /api/auth/refresh/` — token refresh
- `GET /api/auth/me/` — current user profile
- `POST /api/auth/me/top-up/` — balance top-up
- `/api/products/` — products API
- `/api/cart/items/` — cart operations
- `POST /api/orders/create-from-cart/` — create order from cart
- `GET /api/orders/` — order history
- 
Присутствует интеграционный сценарий `tests/test_flow.py` (регистрация → логин → пополнение → товар → корзина → заказ).

---

## 🗃️ Переключение на PostgreSQL (опционально)
По умолчанию используется SQLite. Чтобы перейти на Postgres:
1. Установите PostgreSQL локально (или запустите отдельно).
2. Установите доп. зависимость:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements-postgres.txt
   ```
3. В `.env` укажите:
   ```env
   DB_ENGINE=postgres
   POSTGRES_DB=shop
   POSTGRES_USER=shop
   POSTGRES_PASSWORD=shop
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Примените миграции:
   ```powershell
   python manage.py migrate
   ```

---

## 🧰 Полезные команды
```powershell
# Активировать виртуальное окружение
.\.venv\Scripts\Activate.ps1

# Запуск сервера вручную
python manage.py runserver 0.0.0.0:8000
```

---

## ☁ Публикация на GitHub
Убедитесь, что Git установлен (`git --version`). Затем создайте **пустой** репозиторий на GitHub и выполните:
```powershell
.\scripts\init_git.ps1 -RepoUrl "https://github.com/USER/wbtech_shop.git"
```
Скрипт:
- инициализирует git-репозиторий,
- создаёт первый коммит,
- создаёт ветку `main`,
- настраивает `origin`,
- выполняет `git push`.

### Что не попадёт в репозиторий
В `.gitignore` добавлены:
- `.venv/`, `.env`, `db.sqlite3`, `logs.txt`
- `__pycache__/`, `*.pyc` и т. п.
- `static/`, `media/`
- файлы IDE.

---

## 🧱 Структура проекта
```text
wbtech_shop/
├─ manage.py
├─ shop/                # Django конфиг, настройки, urls, wsgi/asgi
├─ users/               # Пользователи: модель с balance, регистрация/профиль/топап
├─ products/            # Товары: модель, сериализаторы, вьюсет, права (админ на CRUD)
├─ cart/                # Корзина: CartItem + API
├─ orders/              # Заказы: модели, сериализаторы, сервис create_order_from_cart
├─ tests/               # pytest сценарии
├─ scripts/             # setup.ps1, run.ps1, test.ps1, init_git.ps1
├─ requirements-win.txt # зависимости для Windows (без psycopg2)
├─ requirements-postgres.txt # доп. зависимость для Postgres
└─ .gitignore
```

---

## ❗ Частые проблемы
- `ModuleNotFoundError: No module named 'django'` — не активировано окружение или не выполнен `scripts/setup.ps1`.
- Порт занят — поменяйте команду запуска на `runserver 0.0.0.0:8080` и откройте `http://127.0.0.1:8080`.
- Ошибки при установке `psycopg2` — используйте `requirements-win.txt`; Postgres-часть ставьте отдельно, как описано выше.
