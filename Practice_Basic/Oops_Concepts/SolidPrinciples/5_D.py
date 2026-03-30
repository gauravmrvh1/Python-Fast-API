# Dependency Inversion (DIP)
# 👉 High-level low-level pe depend na kare

class MysqlDB:
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self):
        self.db = MysqlDB()
        
app = App()
app.db.connect()




# Dependency Inversion (DIP)
# ######################################################################

class Database:
    def connect(self):
        pass

class MysqlDB(Database):
    def connect(self):
        print("MySQL Connected")

class PostgreSqlDB(Database):
    def connect(self):
        print("PostgreSQL Connected")

class App:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()


app = App(MysqlDB())
app.start()

app = App(PostgreSqlDB())
app.start()