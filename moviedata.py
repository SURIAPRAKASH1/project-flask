import mysql.connector
from datetime import datetime

def datas(m_name,r_date):

    conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='monkeydluffy2002@',
    database='movies'
    )

    if (r_date):
            
        release_date = datetime.strptime(r_date, "%Y-%m-%d").date()
        
    else:
        release_date = '3001-01-01'


    if (m_name):
        movie_name = m_name
    else:
        movie_name = 'UN titled'

    cursor = conn.cursor()

    query = "SELECT * FROM movies_data WHERE name = %s AND release_date = %s"

    cursor.execute(query,(movie_name,release_date))

    result = cursor.fetchall()

    try:
        if not result:

            data_to_insert = (movie_name,release_date)
            insert_query = "INSERT INTO movies_data(name,release_date) VALUES(%s,%s)"
            cursor.execute(insert_query,data_to_insert)
    
    except:
        print("Duplicate found") 



    

    conn.commit()

    cursor.close()
    conn.close()

    return result





