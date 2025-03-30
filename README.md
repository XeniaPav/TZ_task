# Тестовое задание: Task Manager API

### Логика работы системы
Task Manager API — это RESTful API, разработанный с использованием Django Rest Framework (DRF) и PostgreSQL. Проект позволяет пользователям управлять задачами, предоставляя возможность создавать, изменять и удалять задачи. Авторизация не требуется, что упрощает взаимодействие с API.

### Стек технологий
1. Django
2. Django Rest Framework (DRF)
3. PostgreSQL
4. Python
5. Docker (опционально для контейнеризации)

### Функционал
1. Создание задачи
2. Изменение задачи
3. Удаление задачи

### Зависимости
Для управления зависимостями в проекте используется pip. Список зависимостей хранится в файле require.txt.

### Установка и запуск
1. Установите Python и pip, если они не установлены.
2. Установите все в зависимости от установки pip.
3. Создайте в корне проекта файл .env и сохраните в нем все переменные окружения.
4. Запустите поездку.
5. Создать администратора с помощью командыpython manage.py csu
6. Запустите проект.
7. Проверьте работу API. Используйте Postman или curl для тестирования эндпоинтов:
  1. POST /tasks/create — создание задачи
  2. PUT /tasks/{id}/update — изменение задачи
  3. DELETE /tasks/{id}/destroy — удаление задачи

### Докер
Для создания контейнера в докере нужно подобрать в консоли следующие команды: 
`docker network create tasksdrf_net` 
`docker run -d --network=tasksdrf_net --name=postgres_container -p 5432:5432 -e POSTGRES_DB=dockertaskDRF -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 postgres:latest`
`docker-compose up -d --build`
