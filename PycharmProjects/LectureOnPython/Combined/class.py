
class user:
    name = ''
    email = ''
    password = ''
    login = False
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("Enter email : ")
        password = input(" Enter password : ")
        if email == self.email and password == self.password:
            login = True
            print("Login Successful")
        else:
            print("Login Failed")
    def logout(self):
        login = False
        print("Logged out!")
    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"\n",self.email)
        else:
            print("User is not Logged in!")

user1 = user("Jihad","bsse1413@iit.du.ac.bd","12345")
#user1.name = "Jihad"
#user1.email = "bsse1413@iit.du.ac.bd"
#user1.password = "12345"
user1.login()