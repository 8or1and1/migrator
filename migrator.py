import config
from elmaConnector import elmaConnector
from terrasoftConnector import terrasoftConnector


class migrator:
    def __init__(self, terrasoft_name, elma_namespace, elma_code):
        self.mapped_columns = None
        self.elma_columns = None
        self.terrasoft_columns = None
        self.terrasoft = terrasoftConnector(config.terrasoft_config, terrasoft_name)
        self.elma = elmaConnector(config.elma_config, elma_namespace, elma_code)

    def auto_map_columns(self):
        terrasoft_columns = self.terrasoft.get_column_names()
        self.terrasoft_columns = terrasoft_columns
        elma_columns = self.elma.get_column_names()
        self.elma_columns = elma_columns
        print('Terrasoft 3x columns: ', terrasoft_columns)
        print('ELMA365 columns: ', elma_columns)
        normalised_terrasoft_columns = [x.lower() for x in terrasoft_columns]
        normalised_elma_columns = [x[2:].lower() if x[:2] == '__' else x.lower() for x in elma_columns]
        self.mapped_columns = {}
        for column_name in normalised_terrasoft_columns:
            if column_name in normalised_elma_columns:
                elma_index = normalised_elma_columns.index(column_name)
                terrasoft_index = normalised_terrasoft_columns.index(column_name)
                self.mapped_columns[terrasoft_columns[terrasoft_index]] = elma_columns[elma_index]
        print('Result of automatic mapping:', self.mapped_columns)

    def manual_map_columns(self):
        pass
