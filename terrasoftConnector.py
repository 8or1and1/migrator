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
        self.column_names = self.get_column_names()

    def select_query(self, query, columns= None):
        connect = pymssql.connect(server=self.server, user=self.user, password=self.password, database=self.database)
        cursor = connect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        data = pd.DataFrame(data) if columns is None else pd.DataFrame(data, columns=columns)
        return data

    def get_column_names(self):
        query = "SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{}'".format(
            self.table)
        columns_dataframe = self.select_query(query)
        y = [row[0] for index, row in columns_dataframe.iterrows()]
        return (y)

    def get_related_tables(self):
        query = 'EXEC sp_fkeys @fktable_name = {}'.format(self.table)
        columns_dataframe = self.select_query(query)
        y = [row[2] for index, row in columns_dataframe.iterrows()]
        return list(set(y))
    def run_custom_query(self, query):
        columns_dataframe = self.select_query(query)
        return columns_dataframe

    def run_custom_query(self, query, column_names):
        columns_dataframe = self.select_query(query, column_names)
        return columns_dataframe
    def get_data(self):
        query = 'Select * from {}'.format(self.table)
        dataframe = self.select_query(query)
        return dataframe

    def get_data(self, column_names):

        query = "Select {} FROM dbo.{}".format(', '.join(column_names), self.table)

        data = self.select_query(query, columns=column_names)
        return data
