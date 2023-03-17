import config
from elmaConnector import elmaConnector



elma = elmaConnector(config.elma_from_config, "_system_catalogs", "KmkSysSettings")


x = elma.get_data()
for y in x:
    print(y)