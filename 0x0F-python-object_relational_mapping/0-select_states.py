#!/usr/bin/python3
# Lists all states from a database

if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    mysql_username = argv[1]
    mysql_password = argv[2]
    datbase_name = argv[3]

    database = MySQLdb.Connect(user=mysql_username, passwd=mysql_password, db=datbase_name, port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states SORTED BY 'states_id'")
    states = cursor.fetchall()
    for row in states:
        print(row)