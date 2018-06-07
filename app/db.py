import psycopg2

class Datadb():

    def __init__(self):
        self.conn = psycopg2.connect("dbname='mainttracker' username='postgres' password='main' host='localhost' port='5432'")
        self.cur = self.conn.cursor()



    def create_request(self, id, name, dop, top, item_requested_for):
        self.cur.execute("CREATE TABLE IF NOT EXISTS requestTable (id INTEGER,name TEXT,dop INTEGER, top INTEGER, item_requested_for TEXT)")
        self.cur.execute("INSERT INTO requests VALUES('{}','{}','{}','{}','{}')" .format(user_id, id, device_type, fault_description, device_status))
        self.conn.commit()
        

    def get_requests(self):
        self.cur.execute("SELECT * from requests")
        allreq = self.cur.fetchall()
        return allreq(allreq)
        
    def get_request_for_one_user(self, id):
        self.cur.execute("SELECT *FROM requestTable WHERE id = '{}' .format(id)")
        usr_req = self.cur.fetchone()
        return usr_req

    def update_request(self, name, item_requested_for,id):
        self.cur.execute("UPDATE requestTable set name='{}', item_requested_for='{}' WHERE id='{}'". format(name, item_requested_for))
        self.conn.commit()

    def sign_up(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER,name TEXT,dop INTEGER, top INTEGER, item_requested_for TEXT)")
        self.cur.execute("INSERT INTO requests VALUES('{}','{}','{}','{}','{}')" .format(id, name, username, password))
        self.conn.commit()

    
        