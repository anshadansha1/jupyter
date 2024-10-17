#2.3 : program to implement CRUD operations using Mysql

#Step 1 : import 
import mysql.connector
from mysql.connector import Error

#Step 2 : Set Path
db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'db_python'
}

#Step 3 :Establish Connection 
def create_connection(config):
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Connection Established")
    except Error as e:
        print(e)
    return conn

#Step 4 : Create Table
def create_table(conn):
    try:
        cmd = '''CREATE TABLE IF NOT EXISTS student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
        );
        '''
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        print("Table Created/Already Exists")
    except Error as e:
        print(e)

#Step 5 : Insert Values to Table
def insert_student(conn,student):
    try:
        cmd = '''INSERT INTO student(name,email) VALUES (%s,%s)'''
        cursor = conn.cursor()
        cursor.execute(cmd,student)
        conn.commit()
        print("Student inserted.")
    except Error as e:
        print(e)
    
#Step 6:Read values from table
def read_student(conn):
    try:
        cmd = "SELECT * from student"
        cursor =conn.cursor()
        cursor.execute(cmd)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e :
        print(e)

#Step 7:Update Values
def update_student(conn,student_id,new_name):
    try:
        cmd="UPDATE student SET name = %s WHERE id = %s"
        cursor = conn.cursor()
        cursor.execute(cmd,(new_name,student_id))
        conn.commit()
        print("Student updated.")
    except Error as e:
        print(e)

#Step 8 :Delete values
def delete_student(conn,student_id):
    try:
        cmd = "DELETE FROM student WHERE id = %s"
        cursor = conn.cursor()
        cursor.execute(cmd,(student_id,))
        conn.commit()
        print("Student deleted.")
    except Error as e:
        print(e)

def main():
    #DB connection
    conn = create_connection(db_config)

    if conn is not None:
        #Create Table
        create_table(conn)

        #Insert student
        insert_student(conn,('Anshad Muhammad','mca2336@rajagiri.edu'))
        insert_student(conn,('Dilsha C P','mca2318@rajagiri.edu'))

        #Read and Display
        print("Students Before update:\n")
        read_student(conn)

        #Update a student
        update_student(conn,1,'Anshad P A')

        #Display after update
        print("Students after update:\n")
        read_student(conn)

        #Delete a Student
        delete_student(conn,2)

        #Display after Deletion
        print("Students after deletion:\n")
        read_student(conn)

        #Close connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__=='__main__':
    main()