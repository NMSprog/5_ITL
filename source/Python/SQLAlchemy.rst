****************
Flask-SQLAlchemy
****************

Flask-SQLAlchemy — обёртка над SQLAlchemy, специально адаптированная для Flask-приложений.

SQLAlchemy — ядро для работы с базами данных.

from flask_sqlalchemy import SQLAlchemy # Импорт библиотеки

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydatabase.db' # Путь

db = SQLAlchemy(app) 