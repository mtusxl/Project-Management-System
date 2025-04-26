# Project Management System

Система управления проектами и задачами — это веб-приложение, разработанное на Django. Она позволяет командам создавать проекты, управлять задачами, отслеживать прогресс и эффективно взаимодействовать между участниками.

## **Функциональные возможности**

- Регистрация и авторизация пользователей
- Создание проектов с описанием
- Добавление участников в проект
- Панель управления проектами (Dashboard)
- Kanban-доска с задачами по статусам (To Do, In Progress, Done)
- CRUD-действия с задачами
- Назначение исполнителей задач
- Редактирование описания проекта
- Отображение прогресса выполнения проекта
- Модальные окна для редактирования и создания задач
- Минималистичный и адаптивный интерфейс на Bootstrap

## **Технологии**

### Backend:
- Python 3.12
- Django 5.x
- Django ORM
- MySQL

### Frontend:
- HTML, CSS (Bootstrap 5)
- JavaScript (с Fetch API)
- Именованные шаблоны Django

### Дополнительно:
- Django Messages
- Django Forms и ModelForms
- CSRF защита
- Работа с сессиями и аутентификацией

## **Структура проекта**

```
Project_Management_System/
├── Project_Menegement_System/  # Настройки Django
├── Projects/                   # Приложение с проектами
├── Tasks/                      # Приложение с задачами
├── Users/                      # Приложение с пользователями
├── templates/                  # HTML-шаблоны
├── static/                     # Статика (изображения)
└── manage.py
```

## **Как запустить проект**

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/mtusxl/Project-Management-System
cd project-management-system
```

2. **Создайте виртуальное окружение и активируйте его:**
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Примените миграции и создайте суперпользователя:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. **Запустите сервер:**
```bash
python manage.py runserver
```

## **Планы по развитию**

- Переход на SPA (Vue.js + DRF)
- Реализация drag-and-drop задач на Kanban доске
- Уведомления о новых задачах и изменениях
- Интеграция аналитики и мониторинга
- Кэширование и оптимизация запросов
- Возможность приглашения участников по email


