import psycopg2
CSV = open("C:\PP2\Lab10\EXAMPLE.csv")
try:
    connection = psycopg2.connect(dbname="EX1", user="HOST", password="HOST")
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        name VARCHAR(100),
        phone VARCHAR(20) UNIQUE
    );
    """
    cursor.execute(create_table_query)
    for i in CSV:
        #print(i)
        a,b = i.split()
        a = "'"+a+"'"
        b = "'"+b+"'"
        try:
            cursor.execute("INSERT INTO contacts VALUES ({} , {});".format(a,b))
        except(Exception,psycopg2.Error) as error:
            connection.rollback()
        connection.commit()
    n = int(input())
    for i in range(n):
        a,b = input().split()
        a = "'"+a+"'"
        b = "'"+b+"'"
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
    cursor.execute("SELECT * FROM contacts WHERE {} ORDER BY name {},phone {};".format(sieve,order_by_name,order_by_phone))
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.commit()
    cursor.close()
    connection.close()
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")