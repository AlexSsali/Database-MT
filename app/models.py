from app.db import Datadb
from app.db import Datadb

dbscript = Datadb()

class User_request():
    

    def create_request(self, id, name, dop, top, item_requested_for):
        new_request={'id':id,'name':name,'dop':dop,'top':top,'item requested for':item_requested_for}
        dbscript.create_request(new_request['id'], new_request['name'], new_request['dop'], new_request['top'], new_request['item requested for'])
       # self.details.append(new_request)
        return 'Request added'
        

    def get_requests(self):
        reqs = dbscript.get_requests()
        for req in reqs:
            return self.reqs
            
#     def get_request_for_one_user(self, id):
#         for detail in details:
#             if detail['id'] == id:
#                 return detail
#         else:
#             return 'request does not exist' 

#     def update_request(self, name, item_requested_for):
#        for detail in self.modify:
#             if detail['name'] == name:
#                 detail['name'] = modified
#                 return detail

# class User_auth():
#     def __init__(self):
#         self.all_user = []
#         self.id = user_id()
#         user = {'id':'id','name':'name','email':'email','username':'king','password':'password','admin':True}
#         user.append(all_user)

#     def sign_up(self, name, email, username, password):
#         new_user= {'name':name, 'email':email, 'username':username, 'password':password}
#         new_user.split()
#         dbData=new_user([0],[1],[2],[3]).dbscript.sign_up()
#         return dbData

    # def sign_in(self):
    #     for indiv in self.all_user:
    #         if indiv['id', 'username' ,'password'] = id, password, username:
    #             return indiv
    #     else:
    #         return 'Invalid username or Password'
    
    

    
 
 
