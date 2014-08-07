import sqlite3
import thread
from django.core.mail import send_mail
# from datetime import time
import time
import os



######################################################Login-authentication#########################################
server_path=os.getcwd()
class DataBase1:
    def __init__(self):
         self.conn = sqlite3.connect("sqlit3_LOCAL.db")
         self.cur = self.conn.cursor()
         self.keyVarible="$%^)*)*hgfyv     ghfdv587&%$^%#^$#@@G B78967987908 $#^$#^$# #^^?([YINTBIUTIUYTKJNp0klghbb  k879870HGFVJYURr ut7 y i"
##         pass
##
##    def database_fetch(self,uname,pwd):
##        uname=str(uname)
##        pwd=str(pwd)
##        uname=uname.lower()
##        pwd=pwd.lower()
##
##
##        cursore = self.conn.execute("SELECT Username from User_authentication where username = (?)", [uname])
##        userrow = cursore.fetchone()
##        print "################userrow",userrow
##        if userrow is None:
##            flag=0
##            return flag
##
##        role = list(userrow)
##     
##
##        var = ''
##        l = len(role)
##        i=0
##        while(1):
##                if(l==0):
##                    break
##                e = list(role[i])
##                for j in range(len(e)):
##                    e1 = e[j]
##                    e1 = str(e1)
##                    e1 = e1.encode("ascii")
##                    var = var + e1
##                i=i+1
##                l=l-1
##        print 'var',var
##        cursore = self.conn.execute("SELECT Tag_value from User_authentication where username = (?)", [uname])
##        Reference_ID = cursore.fetchone()
##
##        if var:
##            print "#####################IM i n condition########################################"
##            cursore=self.conn.execute("SELECT Password from User_authentication where password = (?)", [pwd])
##            passwcorrect = cursore.fetchone()
##            print'########passwcorrect',passwcorrect
##            if passwcorrect is None:
##                print 'passwcorrect',passwcorrect
##                flag=2
##                return flag,var,Reference_ID
##            role = list(passwcorrect)
##            var1 = ''
##            l = len(role)
##            i=0
##            while(1):
##                if(l==0):
##                    break
##                e = list(role[i])
##                for j in range(len(e)):
##                    e1 = e[j]
##                    e1 = str(e1)
##                    e1 = e1.encode("ascii")
##                    var1 = var1 + e1
##                i=i+1
##                l=l-1
##            print 'var1',var1
##            passwcorrect=var1
##            if passwcorrect:
##                flag=1
##                return flag,var,Reference_ID
##        else:
##            flag =2
##            return flag,var,Reference_ID
##        self.conn.commit()
##        #self.conn.close()
##
##    def chanpwd(self,Old_PWD,New_PWD,Cnfrm_PWD,Username):
##        old_pwd=str(Old_PWD)
##        new_pwd=str(New_PWD)
##        cnfrm_pwd=str(Cnfrm_PWD)
##        user_name=str(Username)
##        old_pwd=old_pwd.lower()
##        new_pwd=new_pwd.lower()
##        cnfrm_pwd=cnfrm_pwd.lower()
##        user_name=user_name.lower()
##        print'old_pwd',old_pwd
##
##
##        cursore = self.conn.execute("SELECT Username from User_authentication where username = (?)", [user_name])
##        userrow = cursore.fetchone()
##        print "################userrow",userrow
##        if userrow is None:
##            flag=0
##            return flag
##
##        role = list(userrow)
##   
##        var = ''
##        l = len(role)
##        i=0
##        while(1):
##                if(l==0):
##                    break
##                e = list(role[i])
##                for j in range(len(e)):
##                    e1 = e[j]
##                    e1 = str(e1)
##                    e1 = e1.encode("ascii")
##                    var = var + e1
##                i=i+1
##                l=l-1
##        print 'var',var
##       # cursore = self.conn.execute("SELECT Tag_value from User_authentication where username = (?)", [uname])
##      #  Reference_ID = cursore.fetchone()
##
##        if var:
##            print "#####################IM i n condition########################################"
##            self.conn = sqlite3.connect("sqlit3_LOCAL.db")
##            cursore=self.conn.execute("SELECT Password from User_authentication where password = (?)", [old_pwd])
##            passwcorrect = cursore.fetchone()
##            print'########passwcorrect',passwcorrect
##            if passwcorrect is None:
##                print 'passwcorrect',passwcorrect
##                flag=2
##                return flag
##            role = list(passwcorrect)
##            var1 = ''
##            l = len(role)
##            i=0
##            while(1):
##                if(l==0):
##                    break
##                e = list(role[i])
##                for j in range(len(e)):
##                    e1 = e[j]
##                    e1 = str(e1)
##                    e1 = e1.encode("ascii")
##                    var1 = var1 + e1
##                i=i+1
##                l=l-1
##            print 'var1',var1
##            passwcorrect=var1
##            print "user name in if condition___________________________",user_name
##            q = "UPDATE User_authentication SET Password = '" +new_pwd+ "' WHERE Username = '"+user_name+"'"
##            print "query string__________________________________________",q
##            cursore=self.conn.execute(q)
##            self.conn.commit()
##            print"cursore",cursore
##            if cursore:
##                flag=1
##                return flag
##        else:
##            flag =2
##            return flag
##        self.conn.commit()
##       
##
##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
##
##
##

    def getmbno(self):

        listofmbno=[]
        cur=self.conn.execute("Select Mobile_number from statuschange")
                           
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
            listofmbno.append(d)
       #     print "Requirement ID only=====",d
            pass
        print "mobile nos ::::::::::::::::::::::"  ,listofmbno
        return listofmbno


    def getresumestatuschange(self,mobileno):
        listofresults=[]
        print "\nmobileno",mobileno
        cursor= self.conn.execute("SELECT newstatusofresume,oldstatusofresume,Date,Time,Newstatus,Oldstatus,Requirement_Id,id,Mobile_number from statuschange ")
        #cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir where Status='open' or Status='Open'")
       # print "\nbyee"
        for row in cursor:
          #   print "\nhey"
             if (row[8].lower().find(mobileno.lower())>=0):
                print "\n hell"
                listofresults.append([row[1]+" to "+row[0]+" on "+row[2]+" at "+row[3]])
                pass
        print "\n       listofresults=", listofresults
##        self.conn.close()
        return listofresults

    


