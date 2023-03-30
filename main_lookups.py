# _system_catalogs ContactStatus tbl_ContactStatus
import time
from lookup_migrator import LookupMigrator as migrator
#'ContractTypes', 'KmkProjecType', 'KmkAccountType', 'KmkClientStatus',
lookup_names = ['KmkSysSettings']

for lookup_name in lookup_names:
    print(lookup_name)
    lookup_name_migrator = migrator('_system_catalogs', lookup_name)
    lookup_name_migrator.get_data_from_source()
    lookup_name_migrator.put_data_in_destination()
    time.sleep(3)