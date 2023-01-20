import config
from elmaConnector import elmaConnector
from terrasoftConnector import terrasoftConnector


class LookupMigrator:
    def __init__(self, elma_namespace, elma_code):
        self.elma_columns = None
        self.data = None
        self.elma_from = elmaConnector(config.elma_from_config, elma_namespace, elma_code)
        self.elma_to = elmaConnector(config.elma_client_config, elma_namespace, elma_code)

    def get_data_from_source(self):
        self.data = self.elma_from.get_data()

    def put_data_in_destination(self):
        for element in self.data:
            print(element)
            self.elma_to.create_element(element)
