#это mainn.py файл создается для создания необходимой таблицы в базе данных postgresql для хранения в ней пользовательских данных
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine

app = Flask(__name__) #начинаем Фласк Веб Сервер
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:291102dayana@localhost/assignment' #добавляем sqlalchemy database config для подключения сервера с postgresql
base = SQLAlchemy(app) #оздаем варийбл base для работы с sql

executing = create_engine('postgresql://postgres:291102dayana@localhost/assignment') #создание механизма для выполнения запроса select из моей базы данных


class EndCustomer(base.Model): #identify class EndCustomer as table, and is tablename
    __tablename__ = 'end_customer'
    id_customer = base.Column('id_customer', base.Integer, primary_key=True) #adding additional required queries for db table
    token_customer = base.Column('token_customer', base.Unicode)
    login_customer = base.Column('login_customer', base.Unicode)
    password_customer = base.Column('password_customer', base.Unicode)


    def __init__(self, idd, tokk, logg, passs): #определяем конструктор для EndCustomer class
        self.id_customer = idd
        self.token_customer = tokk
        self.login_customer = logg
        self.password_customer = passs


    logvarr = '' #создание пустых переменных логина и пароля для хранения внутри результатов из таблицы конечных клиентов при выборе данных
    passvarr = '' #изменение их названия, чтобы оно отличалось от столбцов таблицы для предотвращения ошибок

    def globalFunction(customer_id): #создание метода tablefunc для выполнения запроса select и хранения данных внутри наших пустых переменных с использованием механизма и подключения
        with executing.connect() as link:
            output = link.execute(text("SELECT login_customer, password_customer, token_customer FROM end_customer WHERE id_customer = " + str(customer_id)))
            for i in output:
                global logvarr
                global passvarr
                logvarr = i['login_customer']
                passvarr = i['password_customer']
        link.close() #всегда закрываем ссылку


#base.create_all() #этот блок кода прокомментирован, потому что вы должны использовать его только один раз, потому что он приведет к ошибке при создании той же таблицы, что и предыдущая


#entityRow = EndCustomer(2, 'Dayana', 'kkkk', 'danialnekrut') #этот блок кода прокомментирован, потому что вы должны вставлять только отдельные идентификаторы внутри таблицы
#base.session.add(entityRow) #или вы можете просто изменить значения вставки
#base.session.commit()
