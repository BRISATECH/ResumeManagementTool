import shriaccess3
#from database import *
#db_obj=db_testcat()
global username1
username1= ''
global value1
value1=0
global role_value1
role_value1=''
global value
value=0



def login_authentication(username,password):

    print "username in login.py", username
    print "password in login.py", password

    obj = shriaccess3.userinfo()
    list = (username,password)

    global username1
    usr2 = obj.username('fetch',list)
    if usr2 != []:
        usr=usr2[0]
        username1=usr
    else:
        usr=usr2
        username1=usr2

    print "username =",username
    print "usr=",usr

    global password1
    pwd2 = obj.password('fetch',list)
    if pwd2 != []:
        pwd=pwd2[0]
        password1=pwd
    else:
        pwd=pwd2
        password1=pwd2

    print "password=",password
    print "pwd=",pwd

    global value1
    if usr==username and pwd == password:
        value=1
    elif (usr==username and pwd==[]) or (usr==[] and pwd==password):
        value=2
    else:
        value=0

    value1=value
    print "value1 = ",value
    
    status2 = obj.status('fetch',list)
    if status2 != []:
        status=status2[0]
    else:
        status=status2

    print "status=",status
    if status == 'Active':
        status_value= status
    else:
        status_value=status

    global role_value1
    role2 = obj.role('fetch',list)
    if role2 != []:
        role=role2[0]
        
    else:
        role=role2
        
    role_value1=role
    print "role_value1=",role_value1
    
   # value=db_obj.database_fetch(username,password)
    value1=value
   # print "value=",value
    #value=int(value)
   # print "value1=",value

    #role_value=db_obj.Role(username)
    #role_value1=role_value
    #status_value=db_obj.Status(username)
    #print role_value
    #role_value=str(role_value)
    #status_value=str(status_value)
    #print "status_value=" ,status_value
    #print "role_value=" ,role_value

    if value ==2:
        tag_value=0
        return tag_value,value,role_value1

    if role_value1 == "Director" and status_value=="Active":
        tag_value =1
        return tag_value,value,role_value1

    elif role_value1 == "Manager" and status_value=="Active":
        tag_value = 2
        return tag_value,value,role_value1

    elif role_value1 == "TestEngineer" and status_value=="Active":
        tag_value =3
        return tag_value,value,role_value1

    elif role_value1 == "Admin" and status_value=="Active":
        tag_value =4
        return tag_value,value,role_value1

    else:
        tag_value =5
        return tag_value,value,role_value1
