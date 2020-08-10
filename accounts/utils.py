def processExcel():
    import csv
    import sqlite3
    import pandas
    con = sqlite3.connect('db.sqlite3')
    one = """
    SELECT accounts_customer.name, accounts_customer.phone, accounts_customer.email  FROM accounts_customer INNER JOIN accounts_order ON accounts_customer.id = accounts_order.customer_id;"""
    two = """
    SELECT accounts_product.pname, accounts_product.price, accounts_order.date_created FROM accounts_product  INNER JOIN accounts_order ON accounts_product.id = accounts_order.product_id;"""
    df = pandas.read_sql_query(one, con)
    df2 = pandas.read_sql_query(two, con)
    #print(df2)
    dfn2 = df2.iloc[::-1]
    #print(dfn2)
    final = pandas.concat([df, df2.iloc[::-1]], axis=1)
    print(final)
    from datetime import datetime
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    #print("timestamp =", timestamp)
    dt_object = datetime.fromtimestamp(timestamp)
    final.to_csv(r'dumps_' + str(dt_object) + '.csv',index = False, header=True)
    return 'ok'
