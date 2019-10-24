import pymysql

def commit(config, command):
    conn = pymysql.connect(**config)
    cursorObject = conn.cursor()
    # Execute SQL command
    cursorObject.execute(command)