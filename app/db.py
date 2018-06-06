import psycopg2

class Datadb():

    def create_table(self):
        conn=psycopg2.connect("dbname='mainttracker' user='postgres' password='mine' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS requestTable (id INTEGER,name TEXT,dop INTEGER, top INTEGER, item_requested_for TEXT)")
        conn.commit()
        conn.close()

        conn=psycopg2.connect("dbname='mainttracker' user='postgres' password='mine' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER,name TEXT,email TEXT, password TEXT)")
        conn.commit()
        conn.close()

    def insert(self,id,name,dop,top,item_requested_for):
        conn=psycopg2.connect("dbname='mainttracker' user='postgres' password='mine' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("INSERT INTO requestTable VALUES(%s,%s,%s)", (id,name,dop,top,item_requested_for))
        conn.commit()
        conn.close()

    def update(self):
        conn=psycopg2.connect("dbname='mainttracker' user='postgres' password='mine' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("INSERT INTO requestTable VALUES(%s,%s,%s)", (id,name,dop,top,item_requested_for))
        conn.commit()
        conn.close()

    def view(self,id,name,dop,top,item_requested_for):
        conn=psycopg2.connect("dbname='mainttracker' user='postgres' password='mine' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("INSERT INTO requestTable VALUES(%s,%s,%s)", (id,name,dop,top,item_requested_for))
        conn.commit()
        conn.close()
        