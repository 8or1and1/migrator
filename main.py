import pandas as pd
import pymssql

con = pymssql.connect(server='10.77.23.177', user='teradev2', password='P@ssw0rd', database='PG_WORK')
cur = con.cursor()

#cur.execute("SELECT * FROM dbo.tbl_ContactStatus")
cur.execute("SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'tbl_ContactStatus'")
data=cur.fetchall()

df=pd.DataFrame(data)



cur.close()
con.close()