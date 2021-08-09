import sqlite3

print("this is dumb bootstrapper. \nPlease do as tooltips say or you will get a bunch of errors")

file_path_tooltip = "Input file path with / > "
file_path = input(file_path_tooltip)

while True:
    check = input("Are you sure about " + file_path + " ? [y/n] ")
    check = check.lower()
    if check == "y" or check == "yes":
        break
    else:
        file_path = input(file_path_tooltip)

file_name_tooltip = "Input file name without .db > "
file_name = input(file_name_tooltip)
while True:
    check = input("Are you sure about " + file_name + " ? [y/n] ")
    check = check.lower()
    if check == "y" or check == "yes":
        break
    else:
        file_name = input(file_name_tooltip)
fullpath = file_path + file_name + ".db"
print(fullpath)
connect = sqlite3.connect(fullpath)
sql = connect.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name   TEXT NOT NULL,
    password    TEXT NOT NULL,
    role        TINYINT NOT NULL
)""")
sql.execute("""CREATE TABLE IF NOT EXISTS tasks(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    date        DATETIME,
    task_text   TEXT NOT NULL,
    user_id     INTEGER NOT NULL,
    status      TINYINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(ID)
)""")
sql.execute('INSERT INTO users (user_name, password, role) VALUES ("admin", "admin", 3)')
connect.commit()
