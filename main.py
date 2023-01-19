import pandas as pd
import pymssql
import elma

con = pymssql.connect(server='10.77.23.177', user='teradev2', password='P@ssw0rd', database='PG_WORK')
cur = con.cursor()

cur.execute("SELECT Id, Name FROM dbo.tbl_ContactStatus")
data = cur.fetchall()
# cur.execute(
#     "SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'tbl_ContactStatus'")
# columns = cur.fetchall()
cur.close()
con.close()
df = pd.DataFrame(data, columns=["Id", "Name"])
print(df)
df = df.reset_index()
for index, row in df.iterrows():
    elma.create_element(row['Id'], row['Name'])
    print(row['Id'], row['Name'])
columnNames = elma.get_elma_column_names()
print('x')