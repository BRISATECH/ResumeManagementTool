import sqlite3
import thread
from django.core.mail import send_mail
# from datetime import time
import time
import os



######################################################Login-authentication#########################################
server_path=os.getcwd()

class userinfo:
    def __init__(self):
         self.conn = sqlite3.connect("sqlit3_LOCAL.db")
         self.keyVarible="$%^)*)*hgfyv     ghfdv587&%$^%#^$#@@G B78967987908 $#^$#^$# #^^?([YINTBIUTIUYTKJNp0klghbb  k879870HGFVJYURr ut7 y i"
         pass

####Lavita##################################################################
    def submitSignIn(self,username,password):
        
        
        try:
            cursor = self.conn.execute("SELECT username,password from User_authentication ")
            for row in cursor :
                flag=""
               
                if(row[0]==str(username) and row[1]==str(password)):
                    flag= "true"
                    return flag
##                else:
##                     flag="is username or password correct?"
##            return flag
                     
        except sqlite3.IntegrityError:
                print "key is present"
                pass
##########Lavita##################################################################################33


    def database_fetch(self,uname,pwd):
        uname=str(uname)
        pwd=str(pwd)
        uname=uname.lower()
        pwd=pwd.lower()


        cursore = self.conn.execute("SELECT Username from User_authentication where username = (?)", [uname])
        userrow = cursore.fetchone()
        print "################userrow",userrow
        if userrow is None:
            flag=0
            return flag

        role = list(userrow)
     

        var = ''
        l = len(role)
        i=0
        while(1):
                if(l==0):
                    break
                e = list(role[i])
                for j in range(len(e)):
                    e1 = e[j]
                    e1 = str(e1)
                    e1 = e1.encode("ascii")
                    var = var + e1
                i=i+1
                l=l-1
        print 'var',var
        cursore = self.conn.execute("SELECT Tag_value from User_authentication where username = (?)", [uname])
        Reference_ID = cursore.fetchone()

        if var:
            print "#####################IM i n condition########################################"
            cursore=self.conn.execute("SELECT Password from User_authentication where password = (?)", [pwd])
            passwcorrect = cursore.fetchone()
            print'########passwcorrect',passwcorrect
            if passwcorrect is None:
                print 'passwcorrect',passwcorrect
                flag=2
                return flag,var,Reference_ID
            role = list(passwcorrect)
            var1 = ''
            l = len(role)
            i=0
            while(1):
                if(l==0):
                    break
                e = list(role[i])
                for j in range(len(e)):
                    e1 = e[j]
                    e1 = str(e1)
                    e1 = e1.encode("ascii")
                    var1 = var1 + e1
                i=i+1
                l=l-1
            print 'var1',var1
            passwcorrect=var1
            if passwcorrect:
                flag=1
                return flag,var,Reference_ID
        else:
            flag =2
            return flag,var,Reference_ID
        self.conn.commit()
        #self.conn.close()

    def chanpwd(self,Old_PWD,New_PWD,Cnfrm_PWD,Username):
        old_pwd=str(Old_PWD)
        new_pwd=str(New_PWD)
        cnfrm_pwd=str(Cnfrm_PWD)
        user_name=str(Username)
        old_pwd=old_pwd.lower()
        new_pwd=new_pwd.lower()
        cnfrm_pwd=cnfrm_pwd.lower()
        user_name=user_name.lower()
        print'old_pwd',old_pwd


        cursore = self.conn.execute("SELECT Username from User_authentication where username = (?)", [user_name])
        userrow = cursore.fetchone()
        print "################userrow",userrow
        if userrow is None:
            flag=0
            return flag

        role = list(userrow)
   
        var = ''
        l = len(role)
        i=0
        while(1):
                if(l==0):
                    break
                e = list(role[i])
                for j in range(len(e)):
                    e1 = e[j]
                    e1 = str(e1)
                    e1 = e1.encode("ascii")
                    var = var + e1
                i=i+1
                l=l-1
        print 'var',var
       # cursore = self.conn.execute("SELECT Tag_value from User_authentication where username = (?)", [uname])
      #  Reference_ID = cursore.fetchone()

        if var:
            print "#####################IM i n condition########################################"
            self.conn = sqlite3.connect("sqlit3_LOCAL.db")
            cursore=self.conn.execute("SELECT Password from User_authentication where password = (?)", [old_pwd])
            passwcorrect = cursore.fetchone()
            print'########passwcorrect',passwcorrect
            if passwcorrect is None:
                print 'passwcorrect',passwcorrect
                flag=2
                return flag
            role = list(passwcorrect)
            var1 = ''
            l = len(role)
            i=0
            while(1):
                if(l==0):
                    break
                e = list(role[i])
                for j in range(len(e)):
                    e1 = e[j]
                    e1 = str(e1)
                    e1 = e1.encode("ascii")
                    var1 = var1 + e1
                i=i+1
                l=l-1
            print 'var1',var1
            passwcorrect=var1
            print "user name in if condition___________________________",user_name
            q = "UPDATE User_authentication SET Password = '" +new_pwd+ "' WHERE Username = '"+user_name+"'"
            print "query string__________________________________________",q
            cursore=self.conn.execute(q)
            self.conn.commit()
            print"cursore",cursore
            if cursore:
                flag=1
                return flag
        else:
            flag =2
            return flag
        self.conn.commit()
       

############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



        
#__________For handling Database requirement for login________________________
class DataBase:
    
    def __init__(self):
        self.conn = sqlite3.connect("sqlit3_LOCAL.db")
        self.cur = self.conn.cursor()
        self.keyVarible="$%^)*)*hgfyv     ghfdv587&%$^%#^$#@@G B78967987908 $#^$#^$# #^^?([YINTBIUTIUYTKJNp0klghbb  k879870HGFVJYURr ut7 y i"
        pass
#  For resume submitted -------------------------------------------------------
#   name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File




##### snehali  new code 

    def createResumeSubmitTable(self):
        ##self.conn.execute("DROP TABLE Submit_resume")
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Submit_resume
            (date TEXT,
            resumestatus TEXT,
            Statusofresume TEXT,
            RequirementID TEXT,
            Client TEXT,
            name TEXT,            
            Mobile_Number TEXT PRIMARY KEY NOT NULL,
            skills TEXT,
            Date_of_birth TEXT,
            ECTC TEXT,
            Notice_Period TEXT,
            CTC TEXT,
            Email TEXT,
            myResume_File TEXT,
            currentlocation TEXT,
            locationofInterest TEXT,
            PANCARD TEXT ,
            Yearsofexperience TEXT,
            Submit_SOurce TEXT,
            Note TEXT,
            DateofSubmission DATETIME);''')
            print "table created"
            print "requirement id==="
            pass
        except sqlite3.OperationalError as err:
            print "iasdfbhiosh iohosfohsdofos ******************************************************************************************************"
            print str(err)
            pass



    def createUser_AuthenticationTable(self):
        ##self.conn.execute("DROP TABLE Submit_resume")
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS User_authentication
            (department TEXT,
            mobilenumber TEXT,
            lastname TEXT,            
            firstname TEXT,
            Tag_value Numeric,
            username TEXT,
            password TEXT);''')
            print "table created"
            print "requirement id==="
            pass
        except sqlite3.OperationalError as err:
            print "error ******************************************************************************************************"
            print str(err)
            pass


    def createrequirestatuschangeTable(self):
        ##self.conn.execute("DROP TABLE Submit_resume")
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS requirestatuschange
            (Reqid TEXT ,
            oldstatus TEXT,
            newstatus TEXT,            
            Date BLOB,
            Time BLOB);''')
            print "table created"
            print "requirement id==="
            pass
        except sqlite3.OperationalError as err:
            print "error******************************************************************************************************"
            print str(err)
            pass



    def createstatuschangeTable(self):
        ##self.conn.execute("DROP TABLE Submit_resume")
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS statuschange
            (newstatusofresume TEXT ,
            oldstatusofresume TEXT,
            Date BLOB,          
            Time BLOB,
            Newstatus TEXT,
            Oldstatus TEXT,
            Requirement_Id TEXT,
            id INTEGER,
            Mobile_number TEXT,
            sqltime TEXT);''')
            
            print "table created"
            print "requirement id==="
            pass
        except sqlite3.OperationalError as err:
            print "iasdfbhiosh iohosfohsdofos ******************************************************************************************************"
            print str(err)
            pass



## end snehali

        
    def getResumeDetailById(self,mobNo):
        listOfSearchResult = []
        cursore = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where \
                                        Mobile_Number = "+'"'+str(mobNo)+'"' )
        for row in cursore:
                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                pass
       # print "data in listofsearchresult.......................................",listOfSearchResult

        return listOfSearchResult

##    def remove_unary(rows):
##       var = ''
##       l = len(rows)                   
##       i=0
##       while(1):
##          if(l == 0):
##             break
##          e = rows[i]
##          for j in range(len(e)):
##            e1 = e[j]
##            e1 = str(e1)
##            e1 = e1.encode("ascii")
####            var.append(e1)
##            var = var + str(e1)
##          i = i+1
##          l = l-1
##       print "var = ", var
##       return var

##    def getResumedataById(self,Reqid):
##        listOfSearchResult = []
##        cursore = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where RequirementID = "+'"'+str(Reqid)+'"' )
##        for row in cursore:
##                print "hi"
##                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##                pass
##       # print "data in listofsearchresult.......................................",listOfSearchResult
####        self.conn.close()
##        print "list::",listOfSearchResult
##        return listOfSearchResult

##
    

    def getResumedataById(self,Reqid):
        print " first time reqid============",Reqid
        listOfSearchResult=[]
##        
        if (Reqid != ""):
           # print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
            print "python"
            for row in cursor:
                
             # print "reqid============  ",Reqid
                
                if (row[2].lower().find(Reqid.lower())>=0):
                                                    
                    print "req id = ",Reqid.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            print listOfSearchResult
            print "list of data !!!!!!!!!!!!!::",listOfSearchResult
        return listOfSearchResult





     #db for status of resume and requirement id by akshay
    
    def getResumedataById11(self,Reqid,statusofresume123):
        print " first time reqid============",Reqid
        print "my akshay",statusofresume123
        
        listOfSearchResult=[]
##        
        if (Reqid != "" and statusofresume123!=""):
           # print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
            print "python"
            for row in cursor:
                
             # print "reqid============  ",Reqid
                
                if ((row[2].lower().find(Reqid.lower())>=0) and (row[1].lower().find(statusofresume123.lower())>=0)):
                                                    
                    print "req id = ",Reqid.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            print listOfSearchResult
            #print "list of data !!!!!!!!!!!!!::",listOfSearchResult
            
        return listOfSearchResult

    #end of code

    def getresumebymbno(self,mbno):
        print " first time mbno============",mbno
        listOfSearchResult=[]
##        
        if (mbno != ""):
           # print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
            print "python"
            for row in cursor:
                
             # print "reqid============  ",Reqid
                
                if (row[5].lower().find(mbno.lower())>=0):
                                                    
                    print "mbno = ",mbno.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            print listOfSearchResult
            print "list of data !!!!!!!!!!!!!::",listOfSearchResult
        return listOfSearchResult



    
    def delete(self,file_name):
        print "file===*************",file_name
        conn = sqlite3.connect("sqlit3_LOCAL.db")
        d=file_name.replace("u","",0)
        
        if (d != ""):
           print "f"
           q="DELETE from Submit_resume where Mobile_Number = "+'"'+str(d)+'"'
           print "QUERY STRING--------------------------------",q
           cursor=conn.execute(q)
           conn.commit()
          # cursor = self.conn.execute("DELETE from Submit_resume where Mobile Number = "+'"'+str(d)+'"' )
           
        #return true

    
        
    def getResumedataByskills(self,skills):
        print " first time skills============",skills
        listOfSearchResult=[]
        if (len(skills)>1):
                k=skills.find(',')
                if (k >= 1):
                    print "comma detected"
                    sk=skills.split(",")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
                    for row in cursor:
                        print "row[8] = ",row[8]
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "list2 in commo row",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if len(q) == len(list1):
                      #  if len(q) == len(list2):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                   # self.conn.close()
                    return listOfSearchResult

                else:
                    print "/ detected"
                    sk=skills.split("/")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
                    for row in cursor:
                        print "row[6] = ",row[8]
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "in comma list2",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if (len(q) >=1):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                   # self.conn.close()
                    return listOfSearchResult
                
##        if (skills != ""):
##           # print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
##            
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
##          
##            print "python"
##            for row in cursor:
##                            
##                if (row[8].lower().find(skills.lower())>=0):
##                    
##                  #  print "BYEEEE *************\n"
##                   
##                    print "skills = ",skills.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##
##            print listOfSearchResult
##            print "list of data skills !!!!!!!!!!!!!::",listOfSearchResult
##        return listOfSearchResult

    
            
    def getRequirementID(self):

        listofRequirementID=[]
        cur=self.conn.execute("Select ReqId from Submit_requir  where Status='open' or Status='Open'")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
            listofRequirementID.append(d)
       #     print "Requirement ID only=====",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return listofRequirementID

    

    def getReqID(self):

        listofRequirementID=[]
        cur=self.conn.execute("Select ReqId from Submit_requir")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            listofRequirementID.append(d)
         #   print "Requirement ID only=====",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return listofRequirementID
    


    def getRequirementID1(self):

        listofRequirementID=[]
        cur=self.conn.execute("Select RequirementID from Submit_resume")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
          
            listofRequirementID.append(d)
         #   print "Requirement ID ::::only*****",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return listofRequirementID


    def getSource(self):

        listofSource=[]
        cur=self.conn.execute("Select Submit_SOurce from Submit_resume")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            listofSource.append(d)
            #print "SOURCESSS ::::only*****",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return  listofSource
    

    def getSkill(self):

        listofSkill=[]
        cur=self.conn.execute("Select skills from Submit_resume")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
          
            listofSkill.append(d)
            #print "SOURCESSS ::::only*****",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return  listofSkill


    def getyrofexp(self):

        year=[]
        cur=self.conn.execute("Select Yearsofexperience from Submit_resume")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            year.append(d)
            #print "SOURCESSS ::::only*****",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return  year



    def getBDPOC(self):

        listofBDPOC=[]
        cur=self.conn.execute("Select BDPOC from Submit_requir")
                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            listofBDPOC.append(d)
           # print "BDPOC ::::only*****",d
            pass
##        print "id ::::::::::::::::::::::"  ,listofRequirementID
        return  listofBDPOC

    

    def getClient(self):

        listofClient=[]
        cur=self.conn.execute("Select Client from Submit_requir")

                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            listofClient.append(d)
        
            pass
        #print "id ::::::::::::::::::::::"  ,listofClient
        return listofClient

        

        
    def getClient1(self):

        listofClient=[]
        cur=self.conn.execute("Select Client from Submit_resume")
        print "values=",cur
                                    
        for row in cur:
            strr=str(row[0])
            d=strr.replace("u","")
            d=strr.replace("'","")
            d=strr.replace("(","")
            #d=strr.replace(")","")
            d=d.lower()
            d=d.lstrip()
            d=d.rstrip()
           # str1=remove_unary([row[0]])
            listofClient.append(d)
          
            pass
       # print "CLinet ::::::::::::::::::::::"  ,listofClient
        return listofClient


    def getResumedetailsBydateId(self,date,RequirementID):
        listOfSearchResult=[]
        if (RequirementID != ""  and date!=""):
            
            #query to fetch all details for requirement id
            print "req & date===================="
            print "\n1d=",date
            print "\n2.R", RequirementID
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
            for row in cursor:
                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[18].lower().find(date.lower())>=0)):
                    print "\nd=",date
                    print "\nR", RequirementID
                   
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult

        

    def getResumedataByClient_skills(self,Client,skills):
        listOfSearchResult=[]
        #query to fetch all details for requirement id
        print "Client and skills=================="
        print "\n1d=",Client
        print "\n2.R", skills
        
        if (Client != ""  and skills!=""):
            if (len(skills)>1):
                k=skills.find(',')
                if (k >= 1):
                    print "comma detected"
                    sk=skills.split(",")
                    print "\nsk in , = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
                    for row in cursor:
                      if (row[3].lower().find(Client.lower())>=0):
                        print "\n2.row[8] = ",row[8]
                        sk=row[8].split(",")
                        print "2. sk in , = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "2.list2 in commo row",list2
                        print "\nlist11111111",list1
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                      #  if len(q) == len(list2):
                        if len(q) == len(list1):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    #self.conn.close()
                    return listOfSearchResult

                else:
                    print "/ detected"
                    sk=skills.split("/")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list22222222",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
                    for row in cursor:
                     if (row[3].lower().find(Client.lower())>=0):
                        print "\n3.row[8] = ",row[8]
                        sk=row[8].split(",")
                        print "3.sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "3.in comma list2",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "3.list of q",q
                        if (len(q) >=1):
                            print "3. whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                   # self.conn.close()
                    return listOfSearchResult



  #listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])





            
            
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[3].lower().find(Client.lower())>=0) and (row[8].lower().find(skills.lower())>=0)):
##                    print "\nd=",Client
##                    print "\nR",skills
##                   
                   # listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult



    def getResumedataByonly_skills_Yearsofexperience(self,only_skills,Yearsofexperience):
        
        listOfSearchResult=[]
        if (only_skills != ""  and Yearsofexperience!=""):
            
            #query to fetch all details 
            print "Client and Yearsofexperience=================="
            print "\n1d=",only_skills
            print "\n2.R", Yearsofexperience

            if (len(only_skills)>1):
                k=only_skills.find(',')
                if (k >= 1):
                    print "comma detected"
                    sk=only_skills.split(",")
                    print "\nsk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
                    for row in cursor:
                      if (row[15].lower().find(Yearsofexperience.lower())>=0):
                        print "\nrow[8] = ",row[8]
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "list2 in commo row",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if len(q) == len(list1):
                       # if len(q) == len(list2):
                            
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    #self.conn.close()
                    return listOfSearchResult

                else:
                    print "/ detected"
                    sk=only_skills.split("/")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","",0)
                        d=d.lower()
                        d=d.lstrip()
                        d=d.rstrip()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
                    for row in cursor:
                     if (row[15].lower().find(Yearsofexperience.lower())>=0):
                        print "\nrow[8] = ",row[8]
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","",0)
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "in comma list2",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if (len(q) >=1):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    return listOfSearchResult


                            
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[8].lower().find(only_skills.lower())>=0) and (row[15].lower().find(Yearsofexperience.lower())>=0)):
##                    print "\nd=",only_skills
##                    print "\nR",Yearsofexperience
##                   
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
       # return listOfSearchResult



    def setResumeDetail(self,resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Note,Submit_Source):
        tempFilepath = self.uploadFileGiveSavePath(Mobile_Number, myResume_File)
        try:
            print "####################################|   |#####--|--######################################"
            print "####################################|---|#######|########################################"
            print "################################### |   |#### __|_######################################"
            print "#########################################################################################"
            date=time.strftime("%x")
            print "ReqId in db query:", RequirementID
            print "\n resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Note,Submit_Source,DateofSubmission",resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,tempFilepath,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Note,Submit_Source,date
            self.conn.execute("INSERT INTO Submit_resume (resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Note,Submit_Source,DateofSubmission) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,tempFilepath,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Note,Submit_Source,date))
            print "IN vanasdfu sdfugbkb"
            self.conn.commit()

        except:

            pass


        
    def uploadFileGiveSavePath(self,MobNo,fileToSave):
#         path = os.getcwd()+r"\FileStore"+MobNo+"/"+fileToSave.name
        pathRelative = r"\FileStore/"+MobNo+"/"+fileToSave.name
        path = os.getcwd() + pathRelative
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)
        with open(path, 'wb+') as fileName:
            for chunk in fileToSave.chunks():
                fileName.write(chunk)
        return pathRelative


    
#create requirement table ------------------------------------------------------    
# ReqId,Status,Description,Primary_Skill,Note,Client,openPosition,noOfPosition  


## snehali new code 
    def createRequireSubmitTable(self):
        try:
            self.conn.execute('''CREATE TABLE Submit_requir
            (Opendate TEXT,
            ReqId BLOB,
            Client TEXT,
            Primary_Skill TEXT,
            noOfPosition TEXT,
            openPosition TEXT,
            Minimumexp TEXT,
            location TEXT,
            BDPOC TEXT,
            Status TEXT,
            Description BLOB,
            Note BLOB);''')
            print "table created"
            pass
        except sqlite3.OperationalError as err:
            print "table already existing"
            print str(err)
            pass

        ### snehali new code 

        
    def getRequireDetailById(self,ReqId):
        self.conn = sqlite3.connect("sqlit3_LOCAL.db")
        listOfSearchResult = []
        cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir where \
                                        ReqId = "+'"'+str(ReqId)+'"' )

        
        for row in cursor:
                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##        self.conn.close()
                
        print "list))___", listOfSearchResult

        return listOfSearchResult

    

    def getRequireDetailById1(self,ReqId):
        listOfSearchResult=[]
        cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )#where ReqId = '"+str(RequirementID)+"'")
        for row in cursor:
                if (row[1].lower().find(ReqId.lower())>=0):
                    print " in sifahaef row[2] = ",row[1].lower()
                    print "in jk iuhdf hsname[2] = ",ReqId.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
        return listOfSearchResult


##    def getCountofResumes(self,ReqId):
##        listOfSearchResult=[]
##        cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )#where ReqId = '"+str(RequirementID)+"'")
##        for row in cursor:
##                if (row[1].lower().find(ReqId.lower())>=0):
##                    print " in sifahaef row[2] = ",row[1].lower()
##                    print "in jk iuhdf hsname[2] = ",ReqId.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
####            self.conn.close()
##        int count=len(listofSearchResult)
##        print "count=" ,count
##        return listOfSearchResult

   
    
    def setRequireDetail(self,Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note):
        
        print "\n \n valiues is setrequiredetail",Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note

        #try:
        cursor= self.conn.execute("INSERT INTO Submit_requir (Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                                  (Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note))
        print cursor
        self.conn.commit()

            
            
##            self.conn.close()
        #except:
          #  pass
# search result ----------------------------------------------------------------------------
#Skills,name,Mobile_Number


    def searchReturnList1(self,RequirementID,Client,Status):
        listOfSearchResult = []
        print " IN SEARCH RESULT FUNCTION DB FILE ,RequirementID=%s,Client=%s,Status=%s",RequirementID,Client,Status
##        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,\
##        CTC,Email,myResume_File from Submit_resume")
##        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File from Submit_resume")
##        for row in cursor:
###             name = row[0];Mobile_Number = row[1];skills = row[2];Date_of_birth = row[3];
###             ECTC = row[4];Notice_Period = row[5];CTC = row[6];Email  = row[7];
###Name    Mobile Number    Email    Date of birth    skills    CTC    ECTC    Notice Period    Resume
##            if (row[2].lower().find(Skills.lower())>=0 and row[0].lower().find(name.lower())>=0 \
##                and row[1].lower().find(Mobile_Number.lower())>=0):
##                listOfSearchResult.append([row[0],row[1],row[7],row[3],row[2],row[6],row[4],row[5],row[8]])
##                pass
##        return listOfSearchResult 
        if RequirementID:
            print "RequirementID ::::",RequirementID
        else:
            print "RequirementID ::",RequirementID
##       print "name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno",name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno


##        if ( RequirementID=="" and Client=="" and Status==""):
##            #render a msg to the html
##            print "1st if condition====================="
##            msg= "Please fill some field to get result"
##            return render_to_response('RequirementManagement.html',{"msgRed":"","msgBlue":"","msg":msg})
##        
##            self.conn.close()
        
############## BY ONLY RequirementID
        if (RequirementID != "" and Client=="" and Status==""):
            #query to fetch all details for requirement id
            print "req===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )#where ReqId = '"+str(RequirementID)+"'")
            for row in cursor:
                if (row[1].lower().find(RequirementID.lower())>=0):
                    print " in sifahaef row[2] = ",row[2].lower()
                    print "in jk iuhdf hsname[2] = ",RequirementID.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult
           # print "vamsi!@#$%^&",name
           
############## Client
        elif (RequirementID == "" and Client!="" and Status==""):
            #query to fetch for all details for client
            print "client===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )# where Client = '"+str(Client)+"'")
                                        #Mobile_Number = "+'"'+str(Mobile_Number)+'"' )
            for row in cursor:
                if (row[2].lower().find(Client.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult
           # print "vamsi!@#$%^&",name
##############BY Status
        elif (RequirementID == "" and Client=="" and Status!=""):
            #query to fetch for all details for status
            print "status===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir " )#where Status = '"+str(Status)+"'")#where \
                                        #Yearsofexperience = "+'"'+str(Yearsofexperience)+'"' )
            for row in cursor:
                if (row[9].lower().find(Status.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult
##            print "vamsi!@#$%^&",name
########### By ReqId and Client
        elif (RequirementID != "" and Client!="" and Status==""):
            #query to fetch all details for requirement id
            print "req & client===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
            for row in cursor:
                if ((row[1].lower().find(RequirementID.lower())>=0) and (row[2].lower().find(Client.lower())>=0)):
                   # print " in sifahaef row[2] = ",row[1].lower()
#                    print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult
           # print "vamsi!@#$%^&",name             
##########By ReqId and Status             

        elif (RequirementID != "" and Client=="" and Status!=""):
            #query to fetch all details for requirement id
            print "req & status===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )# where ReqId = '"+str(RequirementID)+"'and Status= '"+str(Status)+"'")
            for row in cursor:
                if ((row[1].lower().find(RequirementID.lower()))>=0 and (row[9].lower().find(Status.lower())>=0)):
                    print " in sifahaef row[2] = ",row[1].lower()
                   # print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult
##########By Client and Status

        elif (RequirementID == "" and Client!="" and Status!=""):
            #query to fetch all details for requirement id
            print "client & status========================"
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir" )# where ReqId = '"+str(RequirementID)+"'and Status= '"+str(Status)+"'")
            for row in cursor:
                if ((row[2].lower().find(Client.lower()))>=0 and (row[9].lower().find(Status.lower())>=0)):
                    print " in sifahaef row[2] = ",row[2].lower()
                   # print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
##            self.conn.close()
            return listOfSearchResult

        
        ##########By Client and Status & Req id 
        elif (RequirementID != "" and Client!="" and Status!=""):
            #query to fetch all details for requirement id
            print "all three===================="
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note  from Submit_requir " )#ReqId = '"+str(RequirementID)+"'and Status= '"+str(Status)+" 'and Client= '"+str(Client)+"'")
           # q = "SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir" #where ReqId = '"+str(RequirementID)+"' and Status= '"+str(Status)+"' and Client= '"+str(Client)+"'"
##            q = 'select Opendate from Submit_requir where ReqId = "'+RequirementID+'" and Status = "'+Status+'" and Client = "'+Client+'"'
           # print "QUERY STRING--------------------------------",q
##            con = sqlite3.connect('sqlit3_LOCAL.db')
##            cur = con.execute(q)
##            con.commit()
##            self.cur.execute(q)
##            self.conn.commit()
##            row = cur.fetchall()
#            print "rorororororororororororow-=================",row
            for row in cursor:
                print "ggggggggggggggggggggggg================",row
                print Client
                if ((row[2].lower().find(Client.lower())>=0) and (row[9].lower().find(Status.lower())>=0) and (row[1].lower().find(RequirementID.lower())>=0)):
                    print " in sifahaef row[2] = ",row[2].lower()
                   # print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
  #           self.conn.close()
            print "list of values = ",listOfSearchResult
            return listOfSearchResult
            
            

######### END ##############
##     
##    def searchReturnList(self,RequirementID,Client,Name,skills,Yearsofexperience):
##        listOfSearchResult = []
##        print " IN SEARCH RESULT FUNCTION DB FILE name=%s,Mobile_Number=%s,skills=%s,RequirementID=%s,Client=%s,Yearsofexperience=%s,Pancardno=%s",name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno
####        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,\
####        CTC,Email,myResume_File from Submit_resume")
####        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File from Submit_resume")
####        for row in cursor:
#####             name = row[0];Mobile_Number = row[1];skills = row[2];Date_of_birth = row[3];
#####             ECTC = row[4];Notice_Period = row[5];CTC = row[6];Email  = row[7];
#####Name    Mobile Number    Email    Date of birth    skills    CTC    ECTC    Notice Period    Resume
####            if (row[2].lower().find(Skills.lower())>=0 and row[0].lower().find(name.lower())>=0 \
####                and row[1].lower().find(Mobile_Number.lower())>=0):
####                listOfSearchResult.append([row[0],row[1],row[7],row[3],row[2],row[6],row[4],row[5],row[8]])
####                pass
####        return listOfSearchResult 
##        if name:
##            print "something in name",name
##        else:
##            print "nothing in name",name
####       print "name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno",name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno
##
##        if (Name == "" and skills=="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
##            print "sdfbhskv oshnvo nsovjosrfvsrvj",cursor
##            for row in cursor:
##                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##                pass
##            print "list of values = ",listOfSearchResult
####            self.conn.close()
##            return listOfSearchResult
##
##        
################ BY ONLY NAME
##        if (Name != "" and  skills=="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
##                                        #name = "+'"'+str(name)+'"' )
##            for row in cursor:
##                if (row[16].lower().find(Name.lower())>=0):
##                    print " in sifahaef row[2] = ",row[2].lower()
##                    print "in jk iuhdf hsname[2] = ",Name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##            print "vamsi!@#$%^&",name
##
##
##            ##############BY YEARS OF EXPERIENCE
##        if (Name == ""  and skills=="" and RequirementID=="" and Client=="" and Yearsofexperience!="" ):
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
##                                        #Yearsofexperience = "+'"'+str(Yearsofexperience)+'"' )
##            for row in cursor:
##                if (row[15].lower().find(Yearsofexperience.lower())>=0):
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
####            print "vamsi!@#$%^&",name
##
##        
##
############# BY REQUIREMENTID
##        if (Name == "" and skills=="" and RequirementID!="" and Client=="" and Yearsofexperience=="" ):
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
####                                        RequirementID = "+'"'+str(RequirementID)+'"' )
##            for row in cursor:
##                if (row[2].lower().find(RequirementID.lower())>=0):
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
####            print "vamsi!@#$%^&",name
##
##
##            ######### BY CLIENT
##        if (Name == "" and skills=="" and RequirementID=="" and Client!="" and Yearsofexperience=="" ):
##            print "IN SEARCH OF CLIENT "
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
####                                        Client = "+'"'+str(Client)+'"' )
##            for row in cursor:
##                if (row[3].lower().find(Client.lower())>=0):
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
####
##
##
##        ######### BY SKILLS
##        if (Name == "" and skills!="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
##            print "IN SEARCH OF CLIENT "
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
####                                        Client = "+'"'+str(Client)+'"' )
##            for row in cursor:
##                if (row[8].lower().find(skills.lower())>=0):
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##        
##
##        #### By Reqid and Client
##
##        elif (RequirementID != "" and Client!="" and Name == "" and skills=="" and Yearsofexperience==""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[3].lower().find(Client.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##
##
##        
##        #### By Reqid and Name
##
##        elif (RequirementID != "" and Client=="" and Name!= "" and skills=="" and Yearsofexperience==""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[16].lower().find(Name.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##
##
##
##        #### By Reqid and skills
##
##        elif (RequirementID != "" and Client=="" and Name == "" and skills!="" and Yearsofexperience==""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[8].lower().find(skills.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##
##        #### By Reqid and Yearsofexperience
##
##        elif (RequirementID != "" and Client=="" and Name == "" and skills=="" and Yearsofexperience!=""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[15].lower().find(Yearsofexperience.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##        
##
## #### By  Client and Name
##
##        elif (RequirementID == "" and Client!="" and Name != "" and skills=="" and Yearsofexperience==""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[3].lower().find(Client.lower())>=0) and (row[16].lower().find(Name.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##        
##
##        #### By  Client and skills
##
##        elif (RequirementID == "" and Client!="" and Name == "" and skills!="" and Yearsofexperience==""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[3].lower().find(Client.lower())>=0) and (row[8].lower().find(skills.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##
##        #### By  Client and Yearsofexperience
##
##        elif (RequirementID == "" and Client!="" and Name == "" and skills=="" and Yearsofexperience!=""):
##            #query to fetch all details for requirement id
##            print "req & client===================="
##            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
##            for row in cursor:
##                if ((row[3].lower().find(Client.lower())>=0) and (row[15].lower().find(Yearsofexperience.lower())>=0)):
##                   # print " in sifahaef row[2] = ",row[1].lower()
###                    print "in jk iuhdf hsname[2] = ",name.lower()
##                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####            self.conn.close()
##            return listOfSearchResult
##
##   ## By Name and yearsof exp
##        ## By name and skills
##
##        ## By Reqid, client and name
##        #Reqid, client and name
##        #Reqid, client and name
##        #Reqid, client and name
##        #Reqid, client and name
##          
##
##
##
##
########### BY SKILLS
##        if (name == ""  "" and skills!="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
##            print "skills set in search =%s",skills
##            print "lenth f skills",len(skills)
##            if (len(skills)>1):
##                k=skills.find(',')
##                if (k >= 1):
##                    print "comma detected"
##                    sk=skills.split(",")
##                    print "sk = ",sk
##                    list1=[]
##                    for i in sk:
##                        strr=str(i)
##                        d=strr.replace("u","")
##                        d=d.lower()
##                        list1.append(d)
##
##                    print "list11111111",list1
##                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")
##                    for row in cursor:
##                        
##                        sk=row[8].split(",")
##                        print "sk = ",sk
##                        list2=[]
##                        for i in sk:
##                            strr=str(i)
##                            d=strr.replace("u","")
##                            d=d.lower()
##                            d=d.lstrip()
##                            d=d.rstrip()
##                            list2.append(d)
##                        print "list2 in commo row",list2
##                        q=list(set(list1).intersection(set(list2)))
##                        print "list of q",q
##                        if len(q) == len(list2):
##                            print "whole is there"
##                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####                    self.conn.close()
##                    return listOfSearchResult
##
##                else:
##                    print "/ detected"
##                    sk=skills.split("/")
##                    print "sk = ",sk
##                    list1=[]
##                    for i in sk:
##                        strr=str(i)
##                        d=strr.replace("u","")
##                        d=d.lower()
##                        list1.append(d)
##
##                    print "list11111111",list1
##                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")
##                    for row in cursor:
##                        print "row[6] = ",row[6]
##                        sk=row[8].split(",")
##                        print "sk = ",sk
##                        list2=[]
##                        for i in sk:
##                            strr=str(i)
##                            d=strr.replace("u","")
##                            d=d.lower()
##                            d=d.lstrip()
##                            d=d.rstrip()
##                            list2.append(d)
##                        print "in comma list2",list2
##                        q=list(set(list1).intersection(set(list2)))
##                        print "list of q",q
##                        if (len(q) >=1):
##                            print "whole is there"
##                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
####                    self.conn.close()
##                    return listOfSearchResult
##
##
##            else:
##                cursor = self.conn.execute("SELECT Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )
##
##                abc=cursor.fetchone()
##                if (abc==None):
##                    skills=skills.swapcase()
##                    print "change case ",skills
##                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )
##                    print "detected case sensituve"
##                    for row in cursor:
##                        print "row[6] lower",row[8].lower()
##                        print "skills[6] lower",skills.lower()
##                        listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##                    self.conn.close()
##                    return listOfSearchResult
##                    pass
##                else:
##                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )
##                    for row in cursor:
##                        print "row[6] lower",row[8].lower()
##                        print "skills[6] lower",skills.lower()
##                        listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##                        print "while in only c is there"
####                    self.conn.close()
##                    return listOfSearchResult
##                    pass
        
        
    def searchReturnList(self,RequirementID,Client,Name,skills,Yearsofexperience):
        listOfSearchResult = []
        print " IN SEARCH RESULT FUNCTION DB FILE name=%s,Mobile_Number=%s,skills=%s,RequirementID=%s,Client=%s,Yearsofexperience=%s,Pancardno=%s",name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno
##        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,\
##        CTC,Email,myResume_File from Submit_resume")
##        cursor =  self.conn.execute("SELECT name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File from Submit_resume")
##        for row in cursor:
###             name = row[0];Mobile_Number = row[1];skills = row[2];Date_of_birth = row[3];
###             ECTC = row[4];Notice_Period = row[5];CTC = row[6];Email  = row[7];
###Name    Mobile Number    Email    Date of birth    skills    CTC    ECTC    Notice Period    Resume
##            if (row[2].lower().find(Skills.lower())>=0 and row[0].lower().find(name.lower())>=0 \
##                and row[1].lower().find(Mobile_Number.lower())>=0):
##                listOfSearchResult.append([row[0],row[1],row[7],row[3],row[2],row[6],row[4],row[5],row[8]])
##                pass
##        return listOfSearchResult 
        if name:
            print "something in name",name
        else:
            print "nothing in name",name
##       print "name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno",name,Mobile_Number,skills,RequirementID,Client,Yearsofexperience,Pancardno

        if (Name == "" and skills=="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
            print "sdfbhskv oshnvo nsovjosrfvsrvj",cursor
            for row in cursor:
                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                pass
            print "list of values = ",listOfSearchResult
##            self.conn.close()
            return listOfSearchResult

        
############## BY ONLY BD NAME
        if (Name != "" and  skills=="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
                                        #name = "+'"'+str(name)+'"' )
            for row in cursor:
                if (row[16].lower().find(Name.lower())>=0):
                    print " in sifahaef row[2] = ",row[2].lower()
                    print "in jk iuhdf hsname[2] = ",Name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult
            print "vamsi!@#$%^&",name


            ##############BY YEARS OF EXPERIENCE
        if (Name == ""  and skills=="" and RequirementID=="" and Client=="" and Yearsofexperience!="" ):
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
                                        #Yearsofexperience = "+'"'+str(Yearsofexperience)+'"' )
            for row in cursor:
                if (row[15].lower().find(Yearsofexperience.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult
##            print "vamsi!@#$%^&",name

        

########### BY REQUIREMENTID
        if (Name == "" and skills=="" and RequirementID!="" and Client=="" and Yearsofexperience=="" ):
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
##                                        RequirementID = "+'"'+str(RequirementID)+'"' )
            for row in cursor:
                if (row[2].lower().find(RequirementID.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult
##            print "vamsi!@#$%^&",name


            ######### BY CLIENT
        if (Name == "" and skills=="" and RequirementID=="" and Client!="" and Yearsofexperience=="" ):
            print "IN SEARCH OF CLIENT "
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
##                                        Client = "+'"'+str(Client)+'"' )
            for row in cursor:
                if (row[3].lower().find(Client.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult
##


        ######### BY SKILLS
        if (Name == "" and skills!="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
            print "IN SEARCH OF CLIENT "
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")#where \
##                                        Client = "+'"'+str(Client)+'"' )
            for row in cursor:
                if (row[8].lower().find(skills.lower())>=0):
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult




        #### By Reqid and skills

        elif (RequirementID != "" and Client=="" and Name == "" and skills!="" and Yearsofexperience==""):
            #query to fetch all details for requirement id
            print "req & client===================="
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
            for row in cursor:
                if ((row[2].lower().find(RequirementID.lower())>=0) and (row[8].lower().find(skills.lower())>=0)):
                   # print " in sifahaef row[2] = ",row[1].lower()
#                    print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult


                #### By  Client and Yearsofexperience

        elif (RequirementID == "" and Client!="" and Name == "" and skills=="" and Yearsofexperience!=""):
            #query to fetch all details for requirement id
            print "req & client===================="
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume " )#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")
            for row in cursor:
                if ((row[3].lower().find(Client.lower())>=0) and (row[15].lower().find(Yearsofexperience.lower())>=0)):
                   # print " in sifahaef row[2] = ",row[1].lower()
#                    print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult

   ## By Name and yearsof exp
        ## By name and skills

        ## By Reqid, client and name
        #Reqid, client and name
        #Reqid, client and name
        #Reqid, client and name
        #Reqid, client and name
          




######### BY SKILLS
        if (name == ""  "" and skills!="" and RequirementID=="" and Client=="" and Yearsofexperience=="" ):
            print "skills set in search =%s",skills
            print "lenth f skills",len(skills)
            if (len(skills)>1):
                k=skills.find(',')
                if (k >= 1):
                    print "comma detected"
                    sk=skills.split(",")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","")
                        d=d.lower()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")
                    for row in cursor:
                        
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","")
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "list2 in commo row",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if len(q) == len(list2):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##                    self.conn.close()
                    return listOfSearchResult

                else:
                    print "/ detected"
                    sk=skills.split("/")
                    print "sk = ",sk
                    list1=[]
                    for i in sk:
                        strr=str(i)
                        d=strr.replace("u","")
                        d=d.lower()
                        list1.append(d)

                    print "list11111111",list1
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")
                    for row in cursor:
                        print "row[6] = ",row[6]
                        sk=row[8].split(",")
                        print "sk = ",sk
                        list2=[]
                        for i in sk:
                            strr=str(i)
                            d=strr.replace("u","")
                            d=d.lower()
                            d=d.lstrip()
                            d=d.rstrip()
                            list2.append(d)
                        print "in comma list2",list2
                        q=list(set(list1).intersection(set(list2)))
                        print "list of q",q
                        if (len(q) >=1):
                            print "whole is there"
                            listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])

                    return listOfSearchResult


            else:
                cursor = self.conn.execute("SELECT Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )

                abc=cursor.fetchone()
                if (abc==None):
                    skills=skills.swapcase()
                    print "change case ",skills
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )
                    print "detected case sensituve"
                    for row in cursor:
                        print "row[6] lower",row[8].lower()
                        print "skills[6] lower",skills.lower()
                        listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    self.conn.close()
                    return listOfSearchResult
                    pass
                else:
                    cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where skills = "+'"'+str(skills)+'"' )
                    for row in cursor:
                        print "row[6] lower",row[8].lower()
                        print "skills[6] lower",skills.lower()
                        listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                        print "while in only c is there"
##                    self.conn.close()
                    return listOfSearchResult
                    pass


                
                
    def getidbyBDPOC(self,Name):
        print "BDPOC============",Name
        listOfBDPOCResult=[]
##        cursor = self.conn.execute("SELECT RequirementID from Submit_resume where Submit_SOurce = '"+str(source)+"'")

##      
        if (Name != ""):
            print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
            
            
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir where status= 'Open' or 'open' ")
            #"SELECT RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"' 

            for row in cursor:
                #print "HELLOOOOO *************\n"
                if (row[8].lower().find(Name.lower())>=0):
                    print "BYEEEE *************\n"
                    #print " in sifahaef row[2] = ",row[2].lower()
                 
                    listOfBDPOCResult.append(row[1])
##            self.conn.close()
         
          #  print "list of id as per BDPOC name !!!!!!!!!!!!!::",listOfBDPOCResult
            return listOfBDPOCResult


        
    def getResumedataBydate_and_name(self,date,name):
        
        listOfSearchResult=[]
        if (name != ""  and date!=""):
            
            #query to fetch all details for requirement id
            print "req & date===================="
            print "\n1d=",date
            print "\n2.n", name
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")

            for row in cursor:
                if ((row[16].lower().find(name.lower())>=0) and (row[18].lower().find(date.lower())>=0)):
                    print "\ndate=",date
                    print "\nR:::", name
                  
#                    print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
##            self.conn.close()
            return listOfSearchResult


        

    def getReqidBydatename(self,date,name):
        listOfSearchResult=[]
        if (name != ""  and date!=""):
            
            #query to fetch all details for requirement id
            print "\n name & date===================="
            print "\n date",date
            print "\n2.name", name
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")#where ReqId = '"+str(RequirementID)+"'and Client= '"+str(Client)+"'")

            for row in cursor:
                if ((row[16].lower().find(name.lower())>=0) and (row[18].lower().find(date.lower())>=0)):
                    print "\ndate=",date
                    print "\nR:::", name
                  
#                    print "in jk iuhdf hsname[2] = ",name.lower()
                    listOfSearchResult.append([row[2]])
##            self.conn.close()
            return listOfSearchResult

        

    def searchAll(self,Value):
            print"Value",Value
            listOfSearchResult = []
            self.conn = sqlite3.connect("sqlit3_LOCAL.db")
            cur=self.conn.execute("SELECT Tag_value from User_authentication where username = (?)", [Value])
            Reference_ID=cur.fetchone()


          #  print '##########################Reference_ID##############################333',Reference_ID
            Reference_ID1=list(Reference_ID)
            Reference_ID=Reference_ID1[0]
            #print '#####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4Reference_ID##############################333',Reference_ID



            if  Reference_ID:
                cur1 = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume  where Submit_SOurce='"+str(Value)+"'")
                sss1 = cur1.fetchall()
                #print "All is well",sss1
                for row in sss1:
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    pass
                #print "list of values = ",listOfSearchResult
               # self.conn.close()
                return listOfSearchResult
            else:
                # print "Arpitha is a very gud gal:",Reference_ID
                 cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
                # print "I am in danger",cursor
                 for row in cursor:
                    listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                    pass
                 #print "\n \n list of values from searchAll function = ",listOfSearchResult
                 #self.conn.close()
                 return listOfSearchResult

                
##    def searchAll(self):
##            listOfSearchResult = []
##            self.conn = sqlite3.connect("sqlit3_LOCAL.db")
##            cursor = self.conn.execute("SELECT RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume ")
##            print "sdfbhskv oshnvo nsovjosrfvsrvj",cursor
##            for row in cursor:
##                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]])
##                pass
##            print "list of values = ",listOfSearchResult
####            self.conn.close()
##            return listOfSearchResult
    def searchRequirement(self):
            listOfSearchResult = []
            self.conn = sqlite3.connect("sqlit3_LOCAL.db")
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir")
            print "sdfbhskv oshnvo nsovjosrfvsrvj",cursor
            for row in cursor:
                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
                pass
            print "list of values = ",listOfSearchResult
            
            return listOfSearchResult
        
        

    def searchnymobile(self,resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Note,Submit_Source):
            listOfSearchResult = []
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"' )
            for row in cursor:
                listOfSearchResult.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
                pass
##           
            return listOfSearchResult

        
        
    def UpdateAllResume(self,resumestatus,Statusofresume,RequirementID,Client,name,skills,Yearsofexperience,CURRENT_LOCATION,lOCATION_OF_INTEREST,CTC,ECTC,Notice_Period,Mobile_Number,Email,Source,Date_of_birth,PANCARD_NO,dateOfSub,Note ):
##        q="RequirementID="+",Client,name,skills,Yearsofexperience,CURRENT_LOCATION,lOCATION_OF_INTEREST,CTC,ECTC,Notice_Period,Mobile_Number,Email,Source,Date_of_birth,PANCARD_NO,dateOfSub,Note"
##        tempFilepath = self.uploadFileGiveSavePath(Mobile_Number, myResume)
        conn = sqlite3.connect("sqlit3_LOCAL.db")
        print "IN UpdateAll function data ::::::::",RequirementID
        q = "UPDATE Submit_resume SET resumestatus = '" + str(resumestatus)+"',Statusofresume = '"+ str(Statusofresume)+ "',RequirementID = '"+str(RequirementID) + "',Client = '" + str(Client) + "',name = '" + str(name) + "',skills = '" + str(skills) + "',Yearsofexperience = '" + str(Yearsofexperience) + "',currentlocation = '" + str(CURRENT_LOCATION) + "',locationofInterest = '" + str(lOCATION_OF_INTEREST) + "',CTC = '" + str(CTC) + "',ECTC = '" + str(ECTC) + "',Notice_Period = '" + str(Notice_Period) + "',Email = '" + str(Email) + "',Submit_SOurce = '" + str(Source) + "',Date_of_birth = '" + str(Date_of_birth) + "',PANCARD = '" + str(PANCARD_NO) + "',DateofSubmission = '" + str(dateOfSub) + "',Note = '"+str(Note)+"'  WHERE Mobile_Number = '"+ str(Mobile_Number) + "'"
       # print "q================================ ",q
        cursor=conn.execute(q)
        conn.commit()
        print "UPDATE DONE"

    def UpdateAllRequirement(self,DateofOpening,RequirementID,Client,PrimarySkills,NoOfPositions,Openpositions,MinimumExp,location,BDPOC,Status,Description,Note):
        conn = sqlite3.connect("sqlit3_LOCAL.db")
        print "IN UpdateAll function data ::::::::",RequirementID
        q = "UPDATE Submit_requir SET Opendate = '" + str(DateofOpening) + "',Client = '" + str(Client) + "',Primary_Skill = '" + str(PrimarySkills) + "',noOfPosition = '" + str(NoOfPositions) + "',openPosition = '" + str(Openpositions) + "',MinimumExp = '" + str(MinimumExp) + "',location = '" + str(location) + "',BDPOC = '" + str(BDPOC) + "',Status = '" + str(Status) + "',Description = '" + str(Description) + "',Note = '" + str(Note) + "'  WHERE ReqId = '"+ str(RequirementID) + "'"
        print "q================================ ",q
##       
        cursor=conn.execute(q)
        print "\n done"
        
        conn.commit()
        print "UPDATE DONE"

    def searchopenstateresumes(self,state):
        listofresults=[]
        cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir where Status='open' or Status='Open'")
        for row in cursor:
                listofresults.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]])
                pass
        print "listofresults=", listofresults
##        self.conn.close()
        return listofresults


    def getidbySource(self,source):
        print "source============",source
        listOfSourceResult=[]
##        cursor = self.conn.execute("SELECT RequirementID from Submit_resume where Submit_SOurce = '"+str(source)+"'")

##        for row in cursor:
##                if (row[15].lower().find(source.lower())>=0):
##                    print " in sifahaef row[2] = ",row[1].lower()
##                    print "in jk iuhdf hsname[2] = ",source.lower()
##                    listOfSourceResult.append([row[0]])
####            self.conn.close()
##        return listOfSourceResult

        if (source != ""):
          #  print "HELLOOOOOOOOOOOOOOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          

            for row in cursor:
               # print "HELLOOOOO *************\n"
                if (row[16].lower().find(source.lower())>=0):
                   # print "BYEEEE *************\n"
                    
                   # print "in jk iuhdf hsname[2] = ",source.lower()
                    listOfSourceResult.append(row[2])
##            self.conn.close()
            print listOfSourceResult
            print "\nlist of ids for source !!!!!!!!!!!!!::",listOfSourceResult
            return listOfSourceResult
            
        


    def setstatuschange(self,RequirementID,Mobile_Number,oldstatusofresume,newstatusofresume,oldstatus,newstatus,Date,Time):
##        
##        try:
##            
##            print "#########################################################################################"
##            date=time.strftime("%x")
##            print "ReqId in db query:", RequirementID
           print "\n newstatusofresume,oldstatusofresume,Date,Time,Newstatus,Oldstatus,Requirement_Id,Mobile_number",newstatusofresume,oldstatusofresume,Date,Time,newstatus,oldstatus,RequirementID,Mobile_Number
           self.conn.execute("INSERT INTO statuschange (newstatusofresume,oldstatusofresume,Date,Time,Newstatus,Oldstatus,Requirement_Id,Mobile_number) VALUES (?,?,?,?,?,?,?,?)", (newstatusofresume,oldstatusofresume,Date,Time,newstatus,oldstatus,RequirementID,Mobile_Number))
           print "done inserting"
           self.conn.commit()


           
      
    def setstatuschange1(self,RequirementID,oldstatus,newstatus,date,time):
        print "\n RequirementID,oldstatus,newstatus,date,time",RequirementID,oldstatus,newstatus,date,time
        self.conn.execute("INSERT INTO requirestatuschange (Reqid,oldstatus,newstatus,Date,Time) VALUES (?,?,?,?,?)",(RequirementID,oldstatus,newstatus,date,time))
        print "done inserting"
        self.conn.commit()
####            
##        except:
####            self.conn.close()
##            pass



    def getskillsbyclient(self,client):
        print "client============",client
        listOfSkillsResult=[]
##        

        if (client != ""):
            print "clientOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note from Submit_requir")
            #"SELECT RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"' 

            for row in cursor:
                print "HELLOOOOO *************\n"
                if (row[2].lower().find(client.lower())>=0):
                    print "BYEEEE *************\n"
                    #print " in sifahaef row[2] = ",row[2].lower()
                    print "in jk iuhdf hsname[2] = ",client.lower()
                    listOfSkillsResult.append(row[3])
##            self.conn.close()
            print listOfSkillsResult
            print "list of source !!!!!!!!!!!!!::",listOfSkillsResult
            return listOfSkillsResult


    def getyrexpbyclient(self,client):
         print "client============",client
         listOfyrexpResult=[]
##        

         if (client != ""):
            print "clientOOOOOOOOOOOO *************\n"
            
           
            cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
            #"SELECT RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"' 

            for row in cursor:
                print "HELLOOOOO *************\n"
                if (row[3].lower().find(client.lower())>=0):
                    print "BYEEEE *************\n"
                    #print " in sifahaef row[2] = ",row[2].lower()
                    print "in jk iuhdf hsname[2] = ",client.lower()
                    listOfyrexpResult.append(row[15])
##            self.conn.close()
            print listOfyrexpResult
            print "\nlist of source !!!!!!!!!!!!!::",listOfyrexpResult
            return listOfyrexpResult



#######################################lavita##entire code starts here#######################################################
    def createSignIn_Up(self):
        try:
             self.conn.execute('''CREATE TABLE User_authentication
        (
           mobilenumber  NUMERIC,
           lastname      TEXT,
           firstname     TEXT,
           tag_value     NUMERIC,
           username      TEXT,
           password      TEXT,
        
           
         );''')

        except sqlite3.OperationalError:
        
                print "Table Task_Detail is present"
        pass


    

    def newPassword(self,username,oldpassword,newpassword):
        password =oldpassword
        try:
            cursor = self.conn.execute("SELECT username,password from User_authentication")
            for row in cursor:
                flag=""
                if (str(row[0])== str(username) and str(row[1])== str(password)):
                    flag = "true"
                    self.conn.execute("UPDATE  User_authentication SET password=? WHERE password = ?",(newpassword,password))
                    self.conn.commit()
                else:
                    continue
                return flag
        except sqlite3.IntegrityError:
            print ""



    def signup1(self,mobilenumber,lastname,firstname,username,password):
        Tag_value=1
        print "=============",username, password,firstname,lastname,mobilenumber

        try:
            
            flag=""
            self.createSignIn_Up()
            
            if(len(mobilenumber)!=10):
                flag="mobile number should be of 10 or 11 digits"
                return flag
            else:
                 flag="thank you for signup"
                 self.conn.execute("INSERT INTO  User_authentication VALUES(?,?,?,?,?,?)",
                              (mobilenumber,lastname,firstname,Tag_value,username,password))
                
                 self.conn.commit()
            return flag
        except sqlite3.IntegrityError:
            print "key is present"
            pass


#########################Lavita's code ends here################################################################################

#code by akshay for stats,yearofexp and moblno for autocomplete        
    def getautostats(self):
        
        
        listOfSearchResult=[]
        cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
        print "python"
        for row in cursor:
              listOfSearchResult.append(row[8])
##            self.conn.close()
        print listOfSearchResult
        print "list of data skills !!!!!!!!!!!!!::",listOfSearchResult
         
        return listOfSearchResult
    def getautoexp(self):
        
        
        listOfSearchResult=[]
        cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
        print "python"
        for row in cursor:
              listOfSearchResult.append(row[15])
##            self.conn.close()
        print listOfSearchResult
        print "list of data of yearofexp!!!!!!!!!!!!!::",listOfSearchResult
         
        return listOfSearchResult
    
    def getautombno(self):
        
        
        listOfSearchResult=[]
        cursor = self.conn.execute("SELECT resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File from Submit_resume")
          
        print "python"
        for row in cursor:
              listOfSearchResult.append(row[5])
##            self.conn.close()
        print listOfSearchResult
        print "list of data of mbno !!!!!!!!!!!!!::",listOfSearchResult
         
        return listOfSearchResult
#end of code

        
