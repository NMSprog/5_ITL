***********
Базы данных
***********

Какую сущность я хочу сохранить в базе данных?
Какие поля описывают эту сущность?
Есть ли связь этой сущности с другой сущностью?
Как я буду с этой моделью взаимодействовать в приложении?
Какие поля стоит защищать?
Какие не показывать наружу?

.. code::
    
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy() # Инициализация расширения SQLAlchemy

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nickname = db.Column(db.String(120), unique=True, nullable=False)
        email = db.Column(db.String(50), unique=True, nullable=False)

unique=True - уникальное значение
nullable=False -  обязательное
