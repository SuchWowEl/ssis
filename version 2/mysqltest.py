import mysql.connector
import numpy

# loading
# mysqldump -u root -p test_db < mydatabase_backup.sql

# saving
# mysqldump -u root -p test_db > mydatabase_backup.sql

# mysql -u lul -p{password}

'''

'''
# custom class


class CustomException(Exception):
    pass


# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="viewer",
    password="viewingthefile",
    database="test_db"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a CREATE TABLE statement to create a new table
# mycursor.execute("CREATE TABLE students (`student id` VARCHAR(9) PRIMARY KEY, name VARCHAR(255), gender VARCHAR(15), `year level` VARCHAR(8), `course code` VARCHAR(8))")
# mycursor.execute("ALTER TABLE students CHANGE id `student id` VARCHAR(9), CHANGE email gender VARCHAR(15)")
# mycursor.execute("ALTER TABLE students ADD COLUMN `year level` VARCHAR(8), ADD COLUMN `course code` VARCHAR(8)")


def add_row(val):
    # query = "SELECT `student id` FROM students WHERE `student id` = %s"
    # value = (val[0])
    # print(result)
    # result = checker_of_student_id(val[0])
    '''
    result = duplicate_checker(val[0])
    if result is not None:
        print("cannot add")
    else:
    '''
    # try:
    sql = "INSERT INTO students (`student id`, name, gender, `year level`, `course code`) VALUES (%s, %s, %s, %s, %s)"
    # val = (val[0], val[1], val[2], val[3], val[4])
    mycursor.execute(sql, val)
    # Commit the transaction
    mydb.commit()
    '''
    except Exception as e:
        print("outside error")
        return e
        '''


def duplicate_checker(column, val, table):
    mycursor.execute(
        f"SELECT `{column}` FROM `{table}` WHERE `{column}` = '{val}'")
    # mycursor.execute(f"SELECT `student id` FROM students WHERE `student id` = '{(val[0])}'")
    return mycursor.fetchone()

# def checker_of_student_id(student_id):
#    mycursor.execute("SELECT `course code` FROM courses")
#    id_list = [id[0] for id in mycursor.fetchall()]
#    return student_id in id_list


def add_course(val):  # val is an array
    # query = f"SELECT * FROM courses WHERE `course code` = {val[0]} AND course = {val[1]}"
    # value = (val[0], val[1])
    # mycursor.execute(query)
    # result = mycursor.fetchone()
    # if result is not None:
    #    print("cannot add")
    # else:
    sql = "INSERT INTO courses (`course code`, course) VALUES (%s, %s)"
    # val = (val[0], val[1])
    mycursor.execute(sql, val)
    # Commit the transaction
    mydb.commit()


def delete_rows(id_to_delete):
    # id_to_delete = ["John Doe", "Jane Doe"]
    if not isinstance(id_to_delete, (list, tuple, numpy.ndarray)):
        id_to_delete = [id_to_delete]
    placeholders = ",".join(["%s"] * len(id_to_delete))
    sql = "DELETE FROM students WHERE `student id` IN ({})".format(
        placeholders)
    # sql2 = " IN ({})".format(placeholders)
    mycursor.execute(sql, tuple(id_to_delete))
    mydb.commit()


def delete_course(courses_to_delete):
    # names_to_delete = ["John Doe", "Jane Doe"]
    if not isinstance(courses_to_delete, (list, tuple, numpy.ndarray)):
        courses_to_delete = [courses_to_delete]
    placeholders = ",".join(["%s"] * len(courses_to_delete))
    sql = "DELETE FROM courses WHERE `course code` IN ({})".format(
        placeholders)
    # sql2 = " IN ({})".format(placeholders)
    mycursor.execute(sql, tuple(courses_to_delete))
    mydb.commit()


def edit_student(key, new, column):
    # Execute an UPDATE statement to update an entry
    sql = f"UPDATE students SET `{column}` = %s WHERE `student id` = %s"
    val = (new, key)
    mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()


def edit_course(key, new, column):
    # Execute an UPDATE statement to update an entry
    sql = f"UPDATE courses SET `{column}` = %s WHERE `course code` = %s"
    val = (new, key)
    mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()


def table_for_students():
    mycursor.execute("SELECT * FROM students")
    table = mycursor.fetchall()
    return table


def table_for_courses():
    mycursor.execute("SELECT * FROM courses")
    table = mycursor.fetchall()
    return table


def headers_of_table(table):
    mycursor.execute(f"SELECT * FROM {table} LIMIT 1")
    headers = [i[0] for i in mycursor.description]
    mycursor.fetchall()
    return headers


def list_of_courses():
    mycursor.execute("SELECT `course code` FROM courses")
    course_list = [code[0] for code in mycursor.fetchall()]
    return course_list


def close_connection():
    mydb.close()


def search_records(search_values, boolean):
    query = "SELECT * FROM test_db.students WHERE "
    conditions = []
    parameters = []
    column_names = ["student id", "name",
                    "gender", "year level", "course code"]

    # SELECT * FROM test_db.students WHERE `name` REGEXP 'an' OR `student id` REGEXP '3|6'
    for index, value in enumerate(search_values):
        if value:
            searcher = "REGEXP" if index not in [2, 3, 4] else "="
            query = query + " " + \
                f"`{column_names[index]}` {searcher} '{search_values[index]}' {boolean}"
    query = query.rstrip(f" {boolean}")
    print(query)
    mycursor.execute(query)

    rows = mycursor.fetchall()
    return rows


if __name__ == '__main__':
    '''
    edit_student("2021-0003", "2021-0000", "student id")
    lest = headers_of_table("students")
    print(lest)
    arr = ["2021-0000", "zero", "Male", "4th Year", "BSCS"]
    add_row(arr)
    arr = ["2021-0001", "one", "Female", "1st Year", "BSCA"]
    add_row(arr)
    arr = ["BSCS", "Bachelor of Science in Computer Science"]
    add_course(arr)
    arr = ["BSCA", "Bachelor of Science in Computer Application"]
    add_course(arr)

    del_arr = ["2021-0000", "2021-0001"]
    delete_rows(del_arr)
    del_arr = ["BSCS", "BSCA"]
    delete_course(del_arr)

    edit_student("2021-0001", "2021-0001", "student id")
    edit_course("bscs", "BSCS", "course code")

    mycursor.execute("SELECT * FROM courses;")
    print(mycursor.fetchone())
    mycursor.execute("SELECT * FROM students;")
    print(mycursor.fetchone())
    arr = ["2021-0001", "one", "Female", "1st Year", "BSCA"]
    add_row(arr)
    close_connection()
    '''
