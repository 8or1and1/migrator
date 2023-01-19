import pandas as pd
import pymssql


class terrasoftConnector:
    def __init__(self, config, table):
        server = config['server']
        user = config['user']
        password = config['password']
        database = config['database']
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def select_query(self, query):
        connect = pymssql.connect(server=self.server, user=self.user, password=self.password, database=self.database)
        cursor = connect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return (pd.DataFrame(data))

    def get_column_names(self):
        query = "SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{}'".format(
            self.table)
        columns_dataframe = self.select_query(query)
        y = [row[0] for index, row in columns_dataframe.iterrows()]
        return (y)
