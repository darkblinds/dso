import sqlite3
import pandas as pd


def insert(table, dict):
    dataframe = pd.DataFrame(dict, index=[0])
    data = sqlite3.connect('banco.db')
    dataframe.to_sql(con=data, name=table, if_exists='append', index=False)


def get(table):
    try:
        cnx = sqlite3.connect('banco.db')
        df = pd.read_sql_query(f"SELECT * FROM {table}", cnx)
        data = df.T.to_dict().values()
        return data
    except:
        return []


def delete(table, id):
    sqliteConnection = sqlite3.connect('banco.db')
    cursor = sqliteConnection.cursor()
    sql_delete_query = f"""DELETE from {table} where id = {id}"""
    cursor.execute(sql_delete_query)
    sqliteConnection.commit()
    cursor.close()


def update(table, dict, id):
    delete(table, id)
    insert(table, dict)
