# simple-chat
Тестовое задание на вакансию Python разработчик  Реализовать на Джанго простой клиент-серверный чат, состоящий из сервера и клиента.
Сервер постоянно слушает заданный порт (80) и все поступившие на порт данные (дата, время, никнейм клиента и сообщение, в юникоде) необходимо выводить в консоль сервера и сохранять в текстовый лог файл.
Все поступающие сообщения на сервер пересылаются всем подключенным клиентам.
Клиент реализовать как веб страницу с двумя полями ввода (никнейм и ввод сообщения) и полем для вывода сообщений (дата, время, никнейм клиента и сообщение, в юникоде) поступающих с сервера от других участников.
Предусмотреть регистрацию и авторизацию. Неавторизированные пользователи могут только лишь читать сообщения, писать ничего не могут.
Желательно реализовать, но необязательно: для авторизированных пользователей предоставить возможность к своим сообщениям прикреплять файлы, которые потом могут быть доступны для скачивания авторизированными клиентами.


To run, do the usual:

1. Create and activate a virtualenv:
    cd simple-chat/
    virtualenv -p /usr/bin/python2.7 venv
    source venv/bin/activate


2. Install dependencies:
    pip install -r requirements/dev.txt

3. Run migrations:
    python manage.py migrate

4. Run Django dev server:
    python manage.py runserver