# Продуктовый помощник

![foodgram application](https://github.com/egorov-ev/foodgram-project/workflows/foodgram%20application/badge.svg)

### Description

Приложение «Продуктовый помощник»: сайт, на котором пользователи будут
публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на
публикации других авторов. Сервис позволит пользователям создавать список
продуктов, которые нужно купить для приготовления выбранных блюд.

Приложение (до хх.хх) доступно по адресу: [simplerecipes.ru](simplerecipes.ru)
или [130.193.41.26](http://130.193.41.26)

# Установка приложения на удаленный сервер

1. Склонируйте репозиторий командой:
    ```
    git clone https://github.com/egorov-ev/foodgram-project.git
    ```
2. Установите на серевере docker и docker-compose. Инструкция для установки на
   ubuntu 20-04 описан в инструкции:
    - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru
    - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru
3. Создайте в корне проекта файл ".env", укажите в нем следующие переменные:
    ```
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY="ХХХХ"
    ```
4. Скопируйте на сервер файлы "host.conf", "docker-compose.yaml", ".env"
   командами:
    * scp docker-compose.yaml {user}@{server-ip}:
    * scp .env {user}@{server-ip}:
    * scp host.conf {user}@{server-ip}:

   Например:
   ```
   ssh egorov-ev@130.193.41.26 scp -r /Users/egorovev/dev/foodgram-project/docker-compose.yaml
   ```
5. Создайте переменные окружения в разделе secrets настроек репозитория:
    ```
    DOCKER_PASSWORD # Пароль от Docker Hub
    DOCKER_USERNAME # Логин от Docker Hub
    HOST # Публичный ip адрес сервера
    USER # Пользователь зарегистрированный на сервере
    PASSPHRASE # Если ssh-ключ защищен фразой-паролем
    SSH_KEY # Приватный ssh-ключ
    TELEGRAM_TO # ID телеграм-аккаунта
    TELEGRAM_TOKEN # Токен бота
    ```
6. После деплоя проекта на сервере необходимо выполнить команды:
   ```
   python3 manage.py migrate # cоздаются необходимые таблицы в базе данных
   python3 manage.py collectstatic # собирает статические файлы из каждого приложения
   manage.py createsuperuser # создается супер пользователь
   ```
7. После каждого обновления репозитория (`git push`) будет происходить:
    - Проверка кода на стандарты `PEP8`.
    - Сборка и публикация образа на `Docker Hub`.
    - Автоматический деплой на сервере.
    - Отправка уведомления через бот Telegram.

8. При необходимости можно импортировать базу данных ингредиентов с помощью
   команды:
   ```
   python3 manage.py loaddata fixtures.json
   ```

## Технологии

При разработке приложения использованы:

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Gunicorn](https://gunicorn.org/)
* [nginx](https://nginx.org)
* [Docker](https://www.docker.com/)
* [GitHub Actions](https://github.com/features/actions)

## Автор

* [facebook](https://www.facebook.com/theonlyegor)
* [telegram](https://t.me/e_egor)
* [GitHub](https://github.com/egorov-ev)