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

    def migrate(self):
        self.terrasoft.get_data(self.mapped_columns.keys())

    def auto_map_columns(self):
        terrasoft_columns = self.terrasoft.column_names
        self.terrasoft_columns = terrasoft_columns
        elma_columns = self.elma.column_names
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

    def print_mapped_columns(self):
        for columnName in self.terrasoft_columns:
            print('{}. {}'.format(self.terrasoft_columns.index(columnName), columnName), sep='', end='')
            if columnName in self.mapped_columns.keys():
                print(' ---> {}'.format(self.mapped_columns[columnName]))
            else:
                print()

    def print_free_elma_columns(self):
        for columnName in self.elma_columns:
            if columnName not in self.mapped_columns.values():
                print('{}. {}'.format(self.elma_columns.index(columnName), columnName), sep='')
    def manual_map_columns(self):
        while True:
            self.print_mapped_columns()
            print('Enter number of column to map or unmap (or e to exit):')
            x = input()
            if x == 'e':
                break
            try:
                column_name = self.terrasoft_columns[int(x)]
            except IndexError:
                print('Wrong column number')
            except ValueError:
                print('Not a valid number')
            else:
                if column_name in self.mapped_columns.keys():
                    del self.mapped_columns[column_name]
                else:
                    self.print_free_elma_columns()
                    print('Enter number of elma column (or e to exit):')
                    x = input()
                    if x == 'e':
                        break
                    try:
                        elma_column_name = self.elma_columns[int(x)]
                    except IndexError:
                        print('Wrong column number')
                    except ValueError:
                        print('Not a valid number')
                    else:
                        self.mapped_columns[column_name]= elma_column_name