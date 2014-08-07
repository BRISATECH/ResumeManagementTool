import shriaccess3


def remove_unary(rows):
    var = ''
    l = len(rows)                   
    i=0
    while(1):
        if(l == 0):
            break
        e = rows[i]
        for j in range(len(e)):
            e1 = e[j]
            e1 = str(e1)
            e1 = e1.encode("ascii")
##            var.append(e1)
            var = var + str(e1)
        i = i+1
        l = l-1
    print "var = ", var
    return var

def fetch_Username_Inactive(status):
    print "status",status
    d=remove_unary(status)
    list1=[]
    list1.append(d)
##    print'Hi im in inactive status',list1
    obj = shriaccess3.Admin_userinfo()
    user_details=obj.User_Status('fetch',list1)
    return user_details

def InActive_userdetails(username):
    list1=[]
    d=remove_unary(username)
    list1.append(d)
    obj = shriaccess3.Admin_userinfo()
    value=obj.Username('fetchall',list1)
    print "values of user",value
    return value

def InActive_User_details_making_Active(username):
    list1=[]
    status='Active'
    list1.append(username)
    list1.append(status)
    
    print "list1 = ",list1
    obj = shriaccess3.Admin_userinfo()
    value =obj.Userinfo('update',list1)
    print "values in INactive ",value
    if (not value):
        return value
##        value=1
##        return "RETURN VALUE OF SUCCESSFULL  UPDATE",value
##    else:
##        value=0
##        return "RETURN VALUE OF SUCCESSFULL  UPDATE",value

    
    #value =db_obj.insert_to_Userdetailsmodified_database(list)
    #return value


##status=['rekhaji']
##k= InActive_userdetails(status)
######username = 'subodh'
####k= fetch_user_details(username)
####k=create_user_data('Mr','umamahi','k','57','MTS','TestEngineer','mahi','mahi','hdsi')
##print "value of k ",k
