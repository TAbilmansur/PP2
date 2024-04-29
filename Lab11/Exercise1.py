import psycopg2
try:
    connection = psycopg2.connect(dbname="EX3", user="HOST", password="HOST")
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        name VARCHAR(100),
        phone VARCHAR(15) UNIQUE
    )
    """
    cursor.execute(create_table_query)
    n = int(input())
    for i in range(n):
        a,b = input().split()
        a = "'"+a+"'"
        b = "'"+b+"'"
        cursor.execute("SELECT * FROM contacts where name = {}".format(a))
        Exists = bool(cursor.fetchone())
        if Exists:
            cursor.execute("UPDATE contacts SET phone = {} WHERE name = {}".format(b,a))
        else:
            try:
                cursor.execute("INSERT INTO contacts VALUES ({} , {});".format(a,b))
            except(Exception,psycopg2.Error) as error:
                connection.rollback()
        connection.commit()
    n = int(input())
    for i in range(n):
        type_of_search,a,type_of_new,new_value = input().split()
        a = "'"+a+"'"
        new_value = "'"+new_value+"'"
        try:
            cursor.execute("UPDATE contacts SET {} = {} WHERE {} = {}".format(type_of_new,new_value,type_of_search,a))
        except(Exception,psycopg2.Error) as error:
            connection.rollback()
        connection.commit()
    n = int(input())
    for i in range(n):
        type,a = input().split()
        a = "'"+a+"'"
        try:
            if type == "NAME":
                cursor.execute("DELETE FROM contacts WHERE name = {}".format(a))
            elif type == "PHONE":
                cursor.execute("DELETE FROM contacts WHERE phone = {}".format(a))
        except(Exception,psycopg2.Error) as error:
            connection.rollback()
        connection.commit()
    sieve = input()
    order_by_name,order_by_phone = input().split()
    offset,limit = map(int,input().split())
    cursor.execute("SELECT * FROM contacts WHERE {} ORDER BY name {}, phone {} , name OFFSET {} LIMIT {};".format(sieve,order_by_name,order_by_phone,offset,limit))
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.commit()
    cursor.close()
    connection.close()
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")