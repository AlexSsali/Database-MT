from app.db import Datadb
from app.db import Datadb

dbscript = Datadb()

class User_request():
    def __init__():
        self.conn = psycopg2.connect("dbname='mainttracker' username='postgres' password='main' host='localhost' port='5432'")
        self.cur = self.conn.cursor()
    

    def create_request(self, id, name, dop, top, item_requested_for):
        # new_request={'id':id,'name':name,'dop':dop,'top':top,'item requested for':item_requested_for}
        dbscript.insert(id, name, dop, top, item_requested_for)
        # self.details.append(new_request)
        return 'Request added'
        

    def get_requests(self):
        self.cur.execute("SELECT * from requests")
        allreq = self.cur.fetchall()
        return allreq(rows)
        
    def get_request_for_one_user(self, id):
        self.cur.execute("SELECT *FROM requestTable WHERE id = '{}' .format(id)")
        usr_req = self.cur.fetchone()
        return usr_req

    def update_request(self, name, item_requested_for,id):
        self.cur.execute("UPDATE request set name='{}', item_requested_for='{}' WHERE id='{}'". format(name, item_requested_for))
        self.conn.commit()

class User_auth():
    def __init__(self):
        self.all_user = []
        self.id = user_id()
        user = {'id':'id','name':'name','email':'email','username':'king','password':'password','admin':True}
        user.append(all_user)

    def sign_up(self):
        new_user = {'id':id,'name':name,'username':username, 'password':password, 'email':email} 
        self.all_user.append(new_user)

    # def sign_in(self):
    #     for indiv in self.all_user:
    #         if indiv['id', 'username' ,'password'] = id, password, username:
    #             return indiv
    #     else:
    #         return 'Invalid username or Password'
    
    # def adminSign_in(self):
    #      for adm in self.all_user:
    #         if adm['id', 'username' ,'password'] = id, password, username:
    #             return adm
    #     else:
    #         return 'Invalid username or Password'

    
 
 
