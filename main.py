# _system_catalogs ContactStatus tbl_ContactStatus

from migrator import migrator

contact_migrator = migrator('tbl_ContactStatus', '_system_catalogs', 'ContactStatus')
contact_migrator.auto_map_columns()
while True:
    print('Do you want map another columns? (y/n')
    match input().lower():
        case 'y':
            contact_migrator.manual_map_columns()
            break
        case 'n':
            break
        case '_':
            print('Incorrect variant')
            pass
# df = pd.DataFrame(data)#, columns=["Id", "Name"])
# print((sys.-[=0pgetsizeof(df)/1024)/1024)
# df = df.reset_index()
# for index, row in df.iterrows():
#     elma.create_element(row['Id'], row['Name'])
#     #print(row['Id'], row['Name'])
# columnNames = elmaConnector.get_elma_column_names()
# print('x')