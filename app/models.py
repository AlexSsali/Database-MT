from app.db import Datadb

dbscript = Datadb()

class User_request():
    
    # def __init__(self):
    #     # self.dbscript
        
    def create_request(self, id, name, dop, top, item_requested_for):
        new_request={'id':id,'name':name,'dop':dop,'top':top,'item requested for':item_requested_for}
        self.details.append(new_request)
        return 'Request added'
        # dbscript.create_req(new_request)

    def get_requests(self):
        return self.details

    def get_request_for_one_user(self, id):
        for detail in self.details:
            if detail['id'] == id:
                return detail
        else:
            return 'request does not exist' 

    def update_request(self, name, new_name):
       for detail in self.details:
            if detail['name'] == name:
                detail['name'] = new_name
                return detail

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

    
 
 
