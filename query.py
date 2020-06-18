import csv
import sqlite3
import pandas
con = sqlite3.connect('db.sqlite3')
one = """
SELECT accounts_customer.name, accounts_customer.phone, accounts_customer.email  FROM accounts_customer INNER JOIN accounts_order ON accounts_customer.id = accounts_order.customer_id;"""
two = """
SELECT accounts_product.pname, accounts_product.price, accounts_order.date_created FROM accounts_product  INNER JOIN accounts_order ON accounts_product.id = accounts_order.product_id;"""
df = pandas.read_sql_query(one, con)
print(df)
df2 = pandas.read_sql_query(two, con)
print(df2)
final = pandas.concat([df, df2], axis=1)
#final.to_csv(r'Data.csv',index = False, header=True)
print(final)
