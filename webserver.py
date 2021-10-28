from datetime import datetime, timedelta
from re import U
from flask import Flask, request
from flask.helpers import make_response
import jwt
from sqlalchemy.orm import session
import mainn #импортируйте main, чтобы иметь доступ к vars и методам внутри mainn.py файл

app = mainn.app #создайте var приложения для хранения там уже созданного стартера веб-сервера приложения Flask
app.config['SECRET_KEY'] = 'thisismyflasksecretkey' #определите конфигурацию приложения внутри этого файла


@app.route('/login')
def logFunc():
    consent = request.authorization
    example_id = 2 #создание переменной example_id в качестве параметра для метода глобальной функции для определения того, от имени какого пользователя мы хотим войти
    mainn.EndCustomer.globalFunction(example_id)
    if consent and consent.username == mainn.logvarr and consent.password == mainn.passvarr: # if statement to verificate are the data form database is identical with data that we input
        logFunc.token_customer = jwt.encode({'user': consent.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                                            app.config['SECRET_KEY']) # encoding unique token for logged user
        update_this = mainn.EndCustomer.query.filter_by(id_customer=example_id).first()
        update_this.token_customer = '''{}'''.format(
            logFunc.token_customer) #этот блок кода используется для обновления существующего токена пользователя новым закодированным токеном внутри правильной строки в базе данных
        mainn.base.session.commit()

        return "Customer_token: " + '''{}'''.format(logFunc.token_customer) #получение токена клиента на html-странице
    return make_response('Could not found a user with login: ' + mainn.logvarr, 401, {
        'WWW-Authenticate': 'Basic realm="Login required'}) #делает ответ что логин не найден, если наше утверждение будет ложным


@app.route('/protected')
def protFunc(): #защищенный метод проверки равенства наших токенов
    example_token = request.args.get('token') #храните значение токена внутри переменной токена
    protFunc.tokenV = '''{}'''.format(
        example_token) #храните значение токена в виде строки внутри значения токена и прямо перед ним защищенное ключевое слово для поиска между методами
    logFunc.token_customer = '''{}'''.format(
        logFunc.token_customer) #храните внутри logFunc.token_customer значение logFunc.token_customer из метода входа в систему
    if logFunc.token_customer == protFunc.tokenV: #если заявление для проверки правильности
        return '<h1>Hello, token which is provided is correct </h1>' #если это правильно, это отправит нам сообщение о том, что токен правильный
    else:
        return '<h1>Hello, Could not verify the token </h1>' #наоборот, с внутренним 'else'



if __name__ == '__main__': #используется для выполнения нашего кода
    app.run(debug=True)


