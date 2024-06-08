import mysql.connector

def retrive_datas():

    conn = mysql.connector.connect(
        user='root',
        host='localhost',
        password='monkeydluffy2002@',
        database='movies'
    )

    cursor = conn.cursor()

    query = "SELECT name,release_date FROM movies_data "

    cursor.execute(query)

    results = cursor.fetchall()

  

    cursor.close()
    conn.close()
        

    return results





    

if __name__ == '__main__':
    ans = retrive_datas()

    contiton = "the batman"

    for data in ans:
        if 'hulk' in data[0].lower():
            print(data[0])

        
    '''if 'batman' in i[0].lower():
            print(f"Tile: {i[0]} , Release_date: {i[1]}")'''