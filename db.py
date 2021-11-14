import os
import sqlite3


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'example.sqlite3') #строим пусть к бд
    connection = sqlite3.connect(db_path) #подключаемся к бд
    cursor = connection.cursor() #вызов курсора для внесения изменений
    cursor.execute(query) #выполнение запроса
    connection.commit() # подтверждение результата
    records = cursor.fetchall() #
    return records
