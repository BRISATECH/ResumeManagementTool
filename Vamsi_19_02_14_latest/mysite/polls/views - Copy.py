from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf.urls import patterns, include, url
from django.core.files.storage import Storage
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
#for Json,for implementing drop down based on product selected
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
##from django.utils import simplejson
import socket

##from BRISAfileOperation import UploadFileForm
import datetime
# import DateTimeInput
from BRISAdb import *
from db import *
import os
from time import time
from django.template import loader
from django.core.files.storage import FileSystemStorage
from filetransfers.api import serve_file
import sqlite3
import mimetypes
from django.core.servers.basehttp import FileWrapper
from datetime import datetime
import sys
import datetime

import Send_EMAIL

from time import gmtime, strftime,time, sleep

#rom reportlab.graphics.charts.piecharts import *
import xlrd
import xlwt
import nltk

try: import simplejson as json
except ImportError: import json

# from BRISAeMail import *
# obj = 
print "starting of view"




####################################Arpitha################################################################################################################################################
global Value
global Reference_ID
################################################################################

@csrf_exempt
def firstPage(request):

    # for dropdown how to pass values in list example:::
    
    #req=['asdf','jwegh','wgwygwg']
    #ipAdd = get_client_ip(request)
    #return render_to_response('resumeSubmit.html',{'val':req,"msgRed":"","msgBlue":"","msgGreen":""})
    dB = DataBase()
    requirementid=dB.getRequirementID()
    getSource=dB.getSource()
    list2=set(getSource)

    getClient=dB.getClient()
    list3=set(getClient)
    
    
    statusofresume1=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status1 =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
    

    ipAdd = get_client_ip(request)
    return render_to_response('loginpage.html')
    return render_to_response('resumeSubmit.html',{'getClient':list3,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":""})
    

#def login():

@csrf_exempt
def resunsub(request):
    
    dB = DataBase()
    requirementid=dB.getRequirementID()
    getSource=dB.getSource()
    list2=set(getSource)
    getClient=dB.getClient()
    list3=set(getClient)
    print "requiremnt id :::::::::::::::requirementids::::", requirementid

    ipAdd = get_client_ip(request)
    statusofresume1=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status1 =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
   
    return render_to_response('resumeSubmit.html',{'getClient':list3,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,"msgRed":"","msgBlue":"Fill all the fields ","msgGreen":""})

@csrf_exempt
def submtResume(request):
    global Value
    print "val",Value
    statusofresume1=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status1 =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
    
    RequirementID=request.POST["ReqId"]
    print "ReqId:", RequirementID
    Client = request.POST["Client"]
    Mobile_Number = request.POST["Mobile_Number"]
    name = request.POST["name"]
    skills = request.POST["skills"]
    Date_of_birth     = request.POST["Date_of_birth"]
    ECTC = request.POST["ECTC"]
    Notice_Period  = request.POST["Notice_Period"]
    CTC = request.POST["CTC"]
    Email = request.POST["Email"]
    CURRENT_LOCATION = request.POST["CURRENT LOCATION"]
    lOCATION_OF_INTEREST = request.POST["lOCATION OF INTEREST"]
    PANCARD_NO = request.POST["PANCARD NO"]
    Yearsofexperience = request.POST["Yearsofexperience"]

    #### Commented status are dropdown boxes
    
    #Statusofresume= request.POST["statusofresume1234"]
    
    Statusofresume="Line_up"
    #resumestatus=request.POST["status1234"]

    resumestatus="Yes"
    
    Note=request.POST["Note"]
    Submit_Source = request.POST["Source"]
    myResume_File = request.FILES["myResume"]
    print'submitresume '
    
    print name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Submit_Source

####### get ids from DB
    dB = DataBase()
    requirementid=dB.getRequirementID()

    getSource=dB.getSource()
    list2=set(getSource)
    getClient=dB.getClient()
    list3=set(getClient)
    #### EMAIL  ##################

    #if test_status:
##    subject = "Resume has been submitted by " + str(Value)
##    #message = "Run completed without problems: \nProject: " + str(project2) + "\nProduct: " + str(product[0]) + "\nRelease: " + str(release[0]) + "\nBuild: " + str(build[0]) + "\nModule: " + str(module[0]) + "\nCategory: " + str(category[0]) + "\nCommunication: " + str(communication[0])
##   # else:
##    #subject = "Resume has been submitted by " + str(Value)
##    #message = "Run couldn't complete: \nProject: " + str(project2) + "\nProduct: " + str(product[0]) + "\nRelease: " + str(release[0]) + "\nBuild: " + str(build[0]) + "\nModule: " + str(module[0]) + "\nCategory: " + str(category[0]) + "\nCommunication: " + str(communication[0])
##
##    user_list = []
##    user_list.append(Value)
##    print "user_list______________________________________________________________________",user_list
##
##    #email=Send_EMAIL.sendemail('testcatbrisa@gmail.com',user_list,'', subject,message,'testcatbrisa@gmail.com','testcat1')
##    email=Send_EMAIL.sendemail('testcatbrisa@gmail.com',user_list,'', subject,'testcatbrisa@gmail.com','testcat1')
##    print "email is sent: ",email
##                        
	#############################################


                        
    if (PANCARD_NO):
        PANCARD_NO=PANCARD_NO
    else:
        PANCARD_NO='Not Available'

    if (len(Mobile_Number)<10 or len(Notice_Period)==0 or len(resumestatus)==0 or len(Statusofresume)==0 or len(name)==0 or len(skills)==0 or   \
         len(ECTC)==0 or len(CTC)==0 or len(Email)==0 or  len(RequirementID)==0 or len(Client)==0 or len(CURRENT_LOCATION)==0 or  len(lOCATION_OF_INTEREST)==0 or len(Yearsofexperience)==0 or len(Submit_Source)==0 ):
        print 'Check code of submitresume'
		
        return render_to_response('resumeSubmit.html',{'getClient':list3,'statusofresume1234':Statusofresume,'status1234':resumestatus,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,"msgRed":"Fill all the fields and check your mobile number","msgBlue":"","msgGreen":""\
                                                       ,'RequirementID':RequirementID,'Client':Client,'name':name,'Mobile_Number':Mobile_Number,\
                                                       'skills':skills,'Date_of_birth':Date_of_birth,'ECTC':ECTC,'Notice_Period':Notice_Period,\
                                                       'CTC':CTC,'Email':Email,'CURRENT_LOCATION':CURRENT_LOCATION,'lOCATION_OF_INTEREST':lOCATION_OF_INTEREST,\
                                                       'PANCARD_NO':PANCARD_NO,'Yearsofexperience':Yearsofexperience,'Submit_Source':Submit_Source})
    else:
        dB = DataBase()
        dB.createResumeSubmitTable()
        print "IN resumesubmit table"
        
        q= "SELECT Mobile_Number from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"'
        conn = sqlite3.connect("sqlit3_LOCAL.db")
        cursor=conn.execute(q)
        print "list of mob",cursor
		
        a= cursor.fetchone()
        print "value of a ",a
        print "mobile is",Mobile_Number
##        for i in cursor:
##            print "value si n lisod mobuibasfda ad",i
##            strr=str(i)
##            print "after string conversion jsf",strr
##            d=strr.replace("u","")
##            list1=list1.append(d)
##        print "list1 value sdifhs ofefdjsef",list1   
####            if str(i) != str(Mobile_Number):
####                k=k+1
####            else:
####                k=1
        if (not a):
            dB = DataBase()
            requirementid=dB.getRequirementID()
            dB.setResumeDetail(resumestatus,Statusofresume,RequirementID,Client,name,Mobile_Number,skills,Date_of_birth,ECTC,Notice_Period,CTC,Email,myResume_File,CURRENT_LOCATION,lOCATION_OF_INTEREST,PANCARD_NO,Yearsofexperience,Note,Submit_Source)
            print "!!!!!!!!!SUCCESSFULLY INSERTED!!!!!!!!!!!!!!!!!!!1"
            return render_to_response('resumeSubmit.html',{'getClient':list3,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"Data saved Successfully"})
            pass
        else:
            dB = DataBase()
            requirementid=dB.getRequirementID()
            return render_to_response('resumeSubmit.html',{'getClient':list3,'statusofresume1234':Statusofresume,'status1234':resumestatus,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,"msgRed":"Mobile number is existed.Please enter another mobile nuber","msgBlue":"","msgGreen":""\
                                                           ,'RequirementID':RequirementID,'Client':Client,'name':name,'Mobile_Number':Mobile_Number,\
                                                       'skills':skills,'Date_of_birth':Date_of_birth,'ECTC':ECTC,'Notice_Period':Notice_Period,\
                                                       'CTC':CTC,'Email':Email,'CURRENT_LOCATION':CURRENT_LOCATION,'lOCATION_OF_INTEREST':lOCATION_OF_INTEREST,\
                                                       'PANCARD_NO':PANCARD_NO,'Yearsofexperience':Yearsofexperience,'Submit_Source':Submit_Source})
          
##                
##        
@csrf_exempt
def requiresub(request):
    #Status = request.POST["status"]
    list1=['Open','Close','On_hold','Resume']
    dB = DataBase()
    getBDPOC=dB.getBDPOC()
    list2=set(getBDPOC)

    #getSource=dB.getSource()
    #list2=set(getSource)
    getClient=dB.getClient()
    list3=set(getClient)
   
    return render_to_response('requirmentSubmit.html',{'getClient':list3,'getBDPOC':list2,'list':list1,"msgRed":"","msgBlue":"Fill all the field","msgGreen":""})

@csrf_exempt
def submtRrequire(request):
    
#    ReqId,Status,Description,Primary_Skill,Note,Client,openPosition,noOfPosition
    Opendate=request.POST["Date_of_OPening"]
    #ReqId = request.POST["ReqId"]
    dB = DataBase()
    getSource=dB.getSource()
    list2=set(getSource)
    list1=['Open','Close','On_hold','Resume']
    getBDPOC=dB.getBDPOC()
    list3=set(getBDPOC)
    getClient=dB.getClient()
    list4=set(getClient)
    Status = request.POST["status"]
    print "Status==============================================",Status
    Description = request.POST["Description"]
    Primary_Skill = request.POST["Primary_Skill"]
    Note = request.POST["Note"]
    Client = request.POST["Client"]
    openPosition = request.POST["openPosition"]
    noOfPosition = request.POST["noOfPosition"]
    MinExp = request.POST["MinimumExperience"]
    BDPOC = request.POST["BD_POC"]
    Location = request.POST["Location"]
    
    ########getting system date & time#############
    sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
    print "system date and time___________",sys_date_time
    sys_dt = sys_date_time.split(" ")
    print "system date/time_______________",sys_dt
    sys_date = sys_dt[0]
    print "system date____________",sys_date
    sys_time = sys_dt[1]
    print "system time____________",sys_time
    
    ##########################################
##    sentence = ' hello  apple'
##    s=Primary_Skill.replace("  ", "")
##    print 's::::',s
    
    ReqId="BD_"+Client+"_"+Primary_Skill+"_"+sys_date+"_"+sys_time

    print "\n reqid=" ,ReqId
    
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print ReqId,Status,Description,Primary_Skill,Note,Client,openPosition,noOfPosition,MinExp,Location
    if (len(Status)==0 or len(Description)==0 or len(Primary_Skill)==0 or len(MinExp)==0 or len(Client)==0 or len(openPosition)==0 or len(BDPOC)==0 or len(noOfPosition)==0 or len(Opendate)==0 or len(Location)==0 ):
        return render_to_response('requirmentSubmit.html',{'getClient':list4,'getBDPOC':list3,'getSource':list2,"msgRed":"Fill all the field","msgBlue":"","msgGreen":""\
                                                       ,'ReqId':ReqId,'status':Status,'BD_POC':BDPOC,'Description':Description,\
                                                       'Primary_Skill':Primary_Skill,'list':list1,'Note':Note,'Client':Client,'openPosition':openPosition,\
                                                       'noOfPosition':noOfPosition,'MinimumExperience':MinExp,'Date of OPening':Opendate,'Location':Location})
    else:
       
        dB.createRequireSubmitTable()
        print "Requirement submit success"
        
        dB.setRequireDetail(Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,MinExp,Location,BDPOC,Status,Description,Note)
        print "successfully inserted"
        msg = "The requirement id given to the submitted Requirement details is: "+ReqId
      
        return render_to_response('requirmentSubmit.html',{'getClient':list4,'getBDPOC':list3,'getSource':list2,"msgRed":"","msgBlue":"","msg":msg,'list':list1})
    
        #return render_to_response('requirmentSubmit.html',{"msgRed":"","msgBlue":"","msgGreen":"Data save"})
    
@csrf_exempt
def submt(request):
    dB=DataBase()
    getClient=dB.getClient()
    list4=set(getClient)
    return render_to_response('resumeSubmit.html',{'getClient':list4,"msgRed":"","msgBlue":"","msgGreen":""})


@csrf_exempt
def editMyTask(request):
        dB = DataBase()
        db1= DataBase1()
        requirementid=dB.getRequirementID1()
       # requirementid=dB.getRequirementID1()
        list1=set(requirementid)
        getClient=dB.getClient()
        list3=set(getClient)
        getSource=dB.getSource()
        list2=set(getSource)
##        getBDPOC=dB.getBDPOC()
##        list2=set(getBDPOC)
        getSkill=dB.getSkill()
        list4=set(getSkill)
        getyr=dB.getyrofexp()
        list5=set(getyr)

##        getClient=dB.getClient()
##        list6=set(getClient)
        global Value
        #statusofresume1=request.POST["statusofresume1"]
        #status1=request.POST["status"]
        
        
        sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
        print "system date and time:::{}}}{}{}{}{}{",sys_date_time

       # date=Date1.replace ("/", "-")
        #print "new date",date
        tmp2=''
        
        tmp=sys_date_time
        tmp2 = tmp.split(" ")
        date=tmp2[0]
        time=tmp2[1]
        print "date", date
        print "time", time
        #tmp2.reverse()
        ##"".join(tmp2)
        print "tmp2",tmp2
##        l=tmp2[0]
##        m=tmp2[1]
##        n=tmp2[2]
##        flag=0
##        user_date=l+'-'+n+'-'+m 
##        print "new DATE &&&&&&&&&  ",user_date
      
        statusofresume1=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
        status1 =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
        iD = request.POST["uniqID"] 
        print "mobilenumber = ",iD
        
        listOfList = dB.getResumeDetailById(iD)
        [[status,statusofresume,RequirementID,Client,name,Mobile_Number,Email,Date_of_birth,skills,CTC,ECTC,Notice_Period,currentlocation,locationofInterest,PANCARD,Yearsofexperience,Submit_SOurce,Note,DateofSubmission,myResume_File]]=listOfList
        listOfSearchResult=dB.searchAll(Value)
        s=' '
        for i in listOfSearchResult:
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                print "\n l", len(mb) 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s                   
                   
                if(len(mb)==0):
##                       for j in k
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)

        

        print "statusofresume",statusofresume
        print "status::",status
        
        return render_to_response('Search.html',{'status':status,'statusofresume1':statusofresume,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",
                           'RequirementID':RequirementID,'Client':Client,'name':name,'Mobile_Number':Mobile_Number,'Email':Email,'Date_of_birth':Date_of_birth,'skills':skills,
         'CTC':CTC,'ECTC':ECTC,'Notice_Period':Notice_Period,'currentlocation':currentlocation,'locationofInterest':locationofInterest,'PANCARD':PANCARD,
         'Yearsofexperience':Yearsofexperience,'Submit_SOurce':Submit_SOurce,'Note':Note,'DateofSubmission':DateofSubmission,'myResume_File':myResume_File,
         'listSearchResult':listOfSearchResult})

###########################################################################################

    

@csrf_exempt
def editMyRequirement(request):
        dB = DataBase()
        iD = request.POST["uniqID"]
        requirementid=dB.getRequirementID1()
        list1=set(requirementid)
        getClient=dB.getClient()
        list3=set(getClient)
        print "Reqid = ",iD
        getSource=dB.getSource()
        list2=set(getSource)
##        getBDPOC=dB.getBDPOC()
##        list2=set(getBDPOC)
        list8=['Open','Close','On_hold','Resume']
       # Status=request.POST["status2"]
    
        getSkill=dB.getSkill()

##        getClient=dB.getClient()
##        list6=set(getClient)
        
        list4=set(getSkill)
        getyr=dB.getyrofexp()
        list5=set(getyr)
        listOfList = dB.getRequireDetailById(iD)
        [[Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,
         location,BDPOC,Status,Description,Note]]=listOfList

        print "Reqid in edit my requirementsbf bihf **********************************************************",ReqId
        listOfSearchResult=dB.searchRequirement()
        return render_to_response('Search.html',{'status2':list8,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",
                                                 'Opendate':Opendate,'ReqId':ReqId,'client':Client,'Primary_Skill':Primary_Skill,'noOfPosition':noOfPosition,'openPosition':openPosition,'Minimumexp':Minimumexp,
         'location':location,'BDPOC':BDPOC,'Status':Status,'Description':Description,'note':Note,'listSearchResult1':listOfSearchResult})


##############################################################################################



@csrf_exempt
def editMyRequirement1(request):
        dB = DataBase()
        getSource=dB.getSource()
        list2=set(getSource)
       
        requirementid=dB.getReqID()
        
        getClient=dB.getClient()
        list3=set(getClient)
        
        getyr=dB.getyrofexp()
        list5=set(getyr)

##        print "status=",Status
        #list1=['Open','Close','On_hold','Resume']
        status2=['Open','Close','On_hold','Resume']
        ##return render_to_response('RequirementManagement.html',{'list':list1,'requirementids':requirementid,'getClient':getClient})
        iD = request.POST["uniqID"] 
        print "Reqid = ",iD
        listOfList = dB.getRequireDetailById(iD)
        [[Opendate,ReqId,Client,Primary_Skill,noOfPosition,openPosition,Minimumexp,location,BDPOC,Status,Description,Note]]=listOfList

        print "Reqid in edit my requirementsbf bihf **********************************************************",ReqId
        listOfSearchResult=dB.searchRequirement()
        return render_to_response('RequirementManagement.html',{'status2':status2,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",
                                                 'Opendate':Opendate,'ReqId':ReqId,'client':Client,'Primary_Skill':Primary_Skill,'noOfPosition':noOfPosition,'openPosition':openPosition,'Minimumexp':Minimumexp,
         'location':location,'BDPOC':BDPOC,'Status':Status,'Description':Description,'note':Note,'listSearchResult1':listOfSearchResult})




@csrf_exempt       
def saveEditResume(request):
    global Value
    Value2=Value
    dB = DataBase()
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
    getClient=dB.getClient()
    list3=set(getClient)
    
    getSource=dB.getSource()
    list2=set(getSource)

##    getBDPOC=dB.getBDPOC()
##    list2=set(getBDPOC)
    getSkill=dB.getSkill()
    list4=set(getSkill)
    getyr=dB.getyrofexp()
    list5=set(getyr)
    
    print'####VALUE####',Value2
    statusofresume1=request.POST["statusofresume123"]
   # status1=request.POST["status123"]
    status1=""
    print "  statusofresume1::",  statusofresume1
    #print " status1::",status1
    
    RequirementID=request.POST["RequirementID"] 
    Client=request.POST["Client"] 
    name=request.POST["name"] 
    skills=request.POST["skills"] 
    Yearsofexperience=request.POST["Yearsofexperience"] 
    CURRENT_LOCATION=request.POST["CURRENT LOCATION"] 
    lOCATION_OF_INTEREST=request.POST["lOCATION OF INTEREST"] 
    CTC=request.POST["CTC"] 
    ECTC=request.POST["ECTC"] 
    Notice_Period=request.POST["Notice_Period"] 
    Mobile_Number=request.POST["Mobile_Number"] 
    Email=request.POST["Email"]
    Source=request.POST["Source"]
    Date_of_birth=request.POST["Date_of_birth"]
    PANCARD_NO=request.POST["PANCARD NO"]
    dateOfSub=request.POST["dateOfSub"]
    Note=request.POST["Note"]
    
     ##### status change##
    oldstatusofresume=request.POST["oldstatusofresume"]
    oldstatus=request.POST["oldstatus"]

    print "oldstatusofresume",oldstatusofresume
    
    print "oldstatus",oldstatus
    

    sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
    print "system date and time:::{}}}{}{}{}{}{",sys_date_time

       # date=Date1.replace ("/", "-")
        #print "new date",date
    tmp2=''
        
    tmp=sys_date_time
    tmp2 = tmp.split(" ")
    date=tmp2[0]
    time=tmp2[1]
    print "date", date
    print "time", time
       #tmp2.reverse()
        ##"".join(tmp2)
    print "tmp2",tmp2
        

    statusofresume=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
    
##    myResume=request.FILES["myResume"]
    print "all values coming from editing section",statusofresume1,RequirementID,Client,name,skills,Yearsofexperience,CURRENT_LOCATION,lOCATION_OF_INTEREST,CTC,ECTC,Notice_Period,Mobile_Number,Email,Source,Date_of_birth,PANCARD_NO
    dB.UpdateAllResume(status1,statusofresume1,RequirementID,Client,name,skills,Yearsofexperience,CURRENT_LOCATION,lOCATION_OF_INTEREST,CTC,ECTC,Notice_Period,Mobile_Number,Email,Source,Date_of_birth,PANCARD_NO,dateOfSub,Note)
   
    dB.setstatuschange(RequirementID,Mobile_Number,oldstatusofresume,statusofresume1,oldstatus,status1,date,time)

##     dB.setstatuschange(RequirementID,Mobile_Number,oldstatusofresume,statusofresume1,oldstatus,status1,date,time)
    
    listOfSearchResult=dB.searchAll(Value2)
    #print "updating done @@@@@@@@@@@@@@@@@@@@@@@@@#################",listOfSearchResult
    return render_to_response('Search.html',{'status123':status,'statusofresume123':statusofresume,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",'listSearchResult':listOfSearchResult})

###############################################################################
@csrf_exempt       
def saveEditRequirement(request):
    dB = DataBase()
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
    getClient=dB.getClient()
    list3=set(getClient)
    getSource=dB.getSource()
    list2=set(getSource)
##    getBDPOC=dB.getBDPOC()
##    list2=set(getBDPOC)
    getSkill=dB.getSkill()
    list4=set(getSkill)
    getyr=dB.getyrofexp()
    list5=set(getyr)
    DateofOpening=request.POST["DateofOpening"] 
    Client=request.POST["client"] 
    PrimarySkills=request.POST["PrimarySkills"] 
    NoOfPositions=request.POST["NoOfPositions"] 
    Openpositions=request.POST["Openpositions"] 
    MinimumExp=request.POST["MinimumExp"] 
    location=request.POST["location"] 
    BDPOC=request.POST["BDPOC"]
    
    Status=request.POST["status2"]
    
    oldstatus= request.POST["oldstatus"]
    
    Description=request.POST["Description"] 
    Note=request.POST["note"] 
    RequirementID=request.POST["RequirementID"] 
    #myResume=request.FILES["myResume"]
    
    print "all values coming from editing section",

    status2=['Open','Close','On_hold','Resume']
    
    sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
    print "\n system date and time &&&& *** ",sys_date_time

    tmp2=''
        
    tmp=sys_date_time
    tmp2 = tmp.split(" ")
    date=tmp2[0]
    time=tmp2[1]
    print "date", date
    print "time", time
       #tmp2.reverse()
        ##"".join(tmp2)
    print "tmp2",tmp2

    dB.setstatuschange1(RequirementID,oldstatus,Status,date,time)
        
    dB.UpdateAllRequirement(DateofOpening,RequirementID,Client,PrimarySkills,NoOfPositions,Openpositions,MinimumExp,location,BDPOC,Status,Description,Note)

    listOfSearchResult=dB.searchRequirement()

    #print "list:::",listOfSearchResult
    
  
    return render_to_response('Search.html',{'status2':status2,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",'listSearchResult1':listOfSearchResult})

#############################################################################



@csrf_exempt       
def saveEditRequirement1(request):
    dB = DataBase()

    requirementid=dB.getReqID()
    getClient=dB.getClient()
    
    list3=set(getClient)
    list1=['Open','Close','On_hold','Resume']
    getSource=dB.getSource()
    list2=set(getSource)
    DateofOpening=request.POST["DateofOpening"] 
    Client=request.POST["client"] 
    PrimarySkills=request.POST["PrimarySkills"] 
    NoOfPositions=request.POST["NoOfPositions"] 
    Openpositions=request.POST["Openpositions"] 
    MinimumExp=request.POST["MinimumExp"] 
    location=request.POST["location"] 
    BDPOC=request.POST["BDPOC"] 
    #Status=request.POST["Status"]
    
    Status=request.POST["status2"]
    
    oldstatus= request.POST["oldstatus1"]
    
    print "\n new status",Status
    Description=request.POST["Description"] 
    Note=request.POST["note"] 
    RequirementID=request.POST["RequirementID"] 
    #myResume=request.FILES["myResume"]
    print "all values coming from editing section\n",

    ##### status change##
    oldstatus=request.POST["oldstatus1"]
    status2=['Open','Close','On_hold','Resume']
    
    print "\n oldstatusof::",oldstatus    
    
    sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
    print "\n system date and time &&&& *** ",sys_date_time

    tmp2=''
        
    tmp=sys_date_time
    tmp2 = tmp.split(" ")
    date=tmp2[0]
    time=tmp2[1]
    print "date", date
    print "time", time
       #tmp2.reverse()
        ##"".join(tmp2)
    print "tmp2",tmp2
    
    dB.setstatuschange1(RequirementID,oldstatus,Status,date,time)
    
    dB.UpdateAllRequirement(DateofOpening,RequirementID,Client,PrimarySkills,NoOfPositions,Openpositions,MinimumExp,location,BDPOC,Status,Description,Note)
    listOfSearchResult=dB.searchRequirement()
    
   # print "updating done ::::::::::::!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@@#################",listOfSearchResult
    return render_to_response('RequirementManagement.html',{'status2':status2,'getSource':list2,'list':list1,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",'listSearchResult':listOfSearchResult})




##@csrf_exempt
##def selectskills(request):
##        		
##	if request.POST.has_key('client_response'):
##         #       x = request.POST['client_response']
##             
##                #print "======================================================================="
##                #print "value from drop down==",x
##                #print "======================================================================="
##      
##                
##                dB=DataBase()
##                getSkill=dB.getSkill()
##                list4=set(getSkill)
##                output = []
##                for x in list4:
##                   if x not in output:
##                      output.append(x)
####                reqid = dB.getRequirementID()
####                list1=[]
####                x=x.lower()
####                  
####                for i in reqid:
####                    if x in i:
####                        list1.append(i)
####                        
####                print "\nlist of id::",list1
##                
##                response_dict = {}
##                results=[]
##                print "\nskills:",output
##                if (len(output)!=0):
##            
##                    response_dict.update({'server_response': output })
##                else:
##                    output=['No skills are available']
##                    response_dict.update({'server_response': output })
####               		 
##                return HttpResponse(simplejson.dumps(output), mimetype='application/json')
##        else:
##                    return render_to_response('Search.html', context_instance=RequestContext(request))
####



@csrf_exempt
def selectclient(request):
        		
	if request.POST.has_key('client_response'):
                x = request.POST['client_response']
             
                print "======================================================================="
                print "value from drop down==",x
                print "======================================================================="
      
                
                dB=DataBase()        
                reqid = dB.getRequirementID()
                list1=[]
                x=x.lower()
                  
                for i in reqid:
                    if x in i:
                        list1.append(i)
                        
                print "\nlist of id::",list1
                
                response_dict = {}
                
                if (len(list1)!=0):
                    response_dict.update({'server_response': list1 })
                else:
                    list1=['No Open state IDs are available for this client']
                    response_dict.update({'server_response': list1 })
##                response_dict.update({'server_response_communication': communication })

##                response_dict.update({'server_response_category': category  })
		 
                return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        else:
                return render_to_response('resumeSubmit.html', context_instance=RequestContext(request))





@csrf_exempt
def selectclient1(request):
           	
	#return render_to_response('output.html',{'val':value})
	if request.POST.has_key('client_response'):
                x = request.POST['client_response']
             
                print "======================================================================="
                print "value from drop down==",x
                print "======================================================================="
                list2=['bd_Philips_Android_2014-03-06_10:09:20','bd_Philips_Android_2014-03-06_10:09:20','bd_Philips_Android_2014-03-06_10:09:20']
                
                dB=DataBase()
##        
                reqid = dB.getReqID()
                
                list1=[]
                x=x.lower()
                skills= dB.getskillsbyclient(x)
                
                skill=set(skills)
                skill=list(skill)

                yrexp=dB.getyrexpbyclient(x)
                yrexps=set(yrexp)
                yrexp=list(yrexps)
                print "\nyrexp::",yrexp
                
                for i in reqid:
                    if x in i:
                        list1.append(i)
                        
                print "\nlist of id::",list1
                
                response_dict = {}
                
                if (len(list1)!=0):
                    response_dict.update({'server_response': list1 })
                else:
                    list1=['No IDs are available for this client']
                    response_dict.update({'server_response': list1 })
                    
                if (len(skill)!=0):
                    response_dict.update({'server_response_skills': skill })
                else:
                    skill=['No skills are available for this client'] 
                    response_dict.update({'server_response_skills': skill })
                    
                if (len(yrexp)!=0):
                    response_dict.update({'server_response_yrexp': yrexp })
                else:
                    yrexp=['No years of experiance are available for this client']   
                    response_dict.update({'server_response_yrexp': yrexp  })
                    
		 
                return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        else:
                return render_to_response('Search.html', context_instance=RequestContext(request))


            

@csrf_exempt
def selectclient2(request):
    
       	if request.POST.has_key('client_response'):
                x = request.POST['client_response']
             
                print "======================================================================="
                print "value from drop down==",x
                print "======================================================================="
                        
                dB=DataBase()
##        
                reqid = dB.getReqID()
                list1=[]
                x=x.lower()
                  
                for i in reqid:
                    if x in i:
                        list1.append(i)
                        
                print "\nlist of id::",list1
                
                response_dict = {}
                
                if (len(list1)!=0):
                    response_dict.update({'server_response': list1 })
                else:
                    list1=['No IDs are available for this client']
                    
                    response_dict.update({'server_response': list1 })
##                response_dict.update({'server_response1': rel  })

		 
                return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        else:
                return render_to_response('RequirementManagement.html', context_instance=RequestContext(request))



            
@csrf_exempt

def query(request):
    global Value2
    global Value
    Value2=Value
##    Date1 = request.POST["datepicker"]
##    Date2 = request.POST["datepicker1"]
    dB = DataBase()
    getClient=dB.getClient()
    list3=set(getClient)
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
    #getSource=dB.getSource()
    
    getSource=dB.getSource()
    list2=set(getSource)
    
   # list2=set(getSource)
    getSkill=dB.getSkill()
    list4=set(getSkill)
    
    #Date1 = request.POST["datepicker"]
    #Date2 = request.POST["datepicker1"]
    print "In the bee Value2",Value2
    print "I am in Value",Value
    
 #   getSource=dB.getSource()
    #list2=set(getSource)
    getyr=dB.getyrofexp()
    list5=set(getyr)
    return render_to_response('Search.html',{'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",'value':Value2,'getSource':list2})



@csrf_exempt
def back(request):
    list1=['Open','Close','On_hold','Resume']
    dB = DataBase()
   # requirementid=dB.getRequirementID()

    getSource=dB.getSource()
    list2=set(getSource)

    getBDPOC=dB.getBDPOC()
    list2=set(getBDPOC)

    return render_to_response('requirmentSubmit.html',{'getBDPOC':list2,'list':list1})



def RequirementManagement(request):
   # Date1 = request.POST["Date1"]
    
    dB = DataBase()
    requirementid=dB.getReqID()
    getClient=dB.getClient()
    list3=set(getClient)
    getSource=dB.getSource()
    list2=set(getSource)
    print "list2: Source", list2
    list1=['Open','Close','On_hold','Resume']
    #return render_to_response('RequirementManagement.html',{'Date1':Date1,'list':list1,'requirementids':requirementid,'getClient':getClient})
    return render_to_response('RequirementManagement.html',{'list':list1,'getSource':list2,'getClient':list3})



### Commented below def searchResult code which has search for bd name plus start date end date ####


##@csrf_exempt
##def searchResult(request):
##    print "IN searchResult*********************************^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
##    
##    skills = request.POST["skills"]
##    Date1 = request.POST["datepicker"]
##    Date2 = request.POST["datepicker1"]
##
##    print "date1",Date1
##    print "date2",Date2
##
##    flag2=0
##   # print "skill in search result function",skills
##    
##   #name = request.POST['name']
##    #Mobile_Number = request.POST['Mobile_Number']
##    
##    RequirementID=request.POST["ReqId"]
##    Client = request.POST["Client"]
##    Yearsofexperience = request.POST["Yearsofexperience"]
##    Name=request.POST["Name"]
##    
##    #Pancardno = request.POST["PANCARD"]
##
##    print "values from search function",skills,Name,RequirementID,Client,Yearsofexperience
##    dB = DataBase()
##
##    #### Resume table ids !!!
##    requirementid=dB.getRequirementID1()
##    list1=set(requirementid)
##    
##      
##    dB = DataBase()
##    getClient=dB.getClient1()
##    list3=set(getClient)
##    getSource=dB.getSource()
##    list2=set(getSource)
##
####    getBDPOC=dB.getBDPOC()
####    list2=set(getBDPOC)
##    
##    getSkill=dB.getSkill()
##    list4=set(getSkill)
##    getyr=dB.getyrofexp()
##    list5=set(getyr)
##
##    #if RequirementID:
##        
##    ##### list of id as per BD name ###
##    if Name:
##         listofid=dB.getidbyBDPOC(Name)
##
##    ##### start date to end date list @@@
##    count_list=[]
##    count=0
##
##    
##  ##### date1 !!!
##   
##    if  (Date1!=" "):
##     Date1=Date1.replace("20","")
##     print "new D=====",Date1
##     tmp2=''
##     count=0
##     tmp=Date1
##     tmp2 = tmp.split('/')
##     tmp2.reverse()
##        ##"".join(tmp2)
##           
##     print "tmp",tmp2
##     l=tmp2[0]
##     print "l --",l
##     m=tmp2[1]
##     print "m --",m
##     n=tmp2[2]
##     flag=0
##     user_date=l+'/'+n+'/'+m 
##     print "user_date:::" , user_date
##
####### date 2 n  reqid !!!!!
##     
##     if (Date2!="" and RequirementID!=""):
##         
##      Date2 = request.POST["datepicker1"]
##      print "date:::::",Date2
##      Date2=Date2.replace("20","")
##      print "new D2::: ==",Date2
##      tmp2=''
##      count=0
##      tmp=Date2
##      tmp2 = tmp.split('/')
##      tmp2.reverse()
##      print " \n tmp",tmp2
##      l=tmp2[0]
##      print "\n l", l
##      m=tmp2[1]
##      n=tmp2[2]
##      flag=0
##      user_date1=l+'/'+n+'/'+m 
##      print "user_date1 ::" , user_date1
##
##    #status= request.POST["status"]
##
##      
##      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
##      print "system date and time___________",sys_date_time
##
####           
####           user_date1=l+'-'+n+'-'+m 
####           print "new DATE &&&&&&&&&  ",user_date1
##           
##
##      endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
##      
##      startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")
##
##      print "start date________________",startDate
##      print "\n end date_______________",endDate 
##
##      count_list=[]
##      date_list=[]
##      flag1=0
##
##           #incrementing the start date by 1 day untill the end date is reached
##      while(1):
##            if flag1==0:
##               date1 = str(startDate)
##               date1 = date1.split(" ")
##               date_list.append(date1[0])
##               flag1=1
##            else:   
##               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
##               date1 = str(startDate)
##               date1 = date1.split(" ") #fetching only the "date" part
##               print date1
##               date_list.append(date1[0]) #appending the date" part to a list
##               if startDate == endDate:
##                  break
##      print "\n final list of dates for req id n dates $$$$$$$$$$",date_list
##
########## datelist has dates in format as per submission dates ######
##      
##      datelist=[]
##      listofresumedata=[]
##      finallist=[]
##      flag=0
##      
##      for i in date_list:
##          i=i.replace("20","")
##          tmp2=''
##          
##          tmp=i
##          tmp2 = tmp.split('-')
##          tmp2.reverse()
##          print "tmp",tmp2
##          l=tmp2[0]
##          m=tmp2[1]
##          n=tmp2[2]
##          flag=0
##          user_date1=m+'/'+l+'/'+n
##          datelist.append(user_date1)
##      print "\n datelist ::" , datelist
##
##      ######## Fetch resume data as per req id and date !!!!!
##
##      for i in datelist:
##          list1 =dB.getResumedetailsBydateId(i,RequirementID)
##          print "count \n"
##          listofresumedata.append(list1)
##        #listofresumedata=dB.getResumedataById(i)
##
##      print "list:::###",listofresumedata
##
##   
##      for i in listofresumedata:
##        if flag==0:
##             print "i***",i
##        for j in i:
##             finallist.append(j)
##             if flag==0:
##               print "j%%%%% ", j
##               flag=1
####    print "first::",finallist[0]           
##
##      listOfSearchResult=finallist
##      print "finallist :::: \n \n ",    finallist
##      print "\nlist ****::",listOfSearchResult
##      
##
##      requirementid=dB.getRequirementID1()
##      list1=set(requirementid)
##      flag2=1
##          
## ####################################################################
##      
##   ###### idfordate is d list which has req ids from start date to end date####
##    
####      idfordate=[]
####      for i in date_list:
####               print "i========= ",i
####               for j in listofid:
####                   print "j",j
####                   if i in j:
####                       idfordate.append(j)
####
####      print "idfordate**$$#*%(@#*$*$$", idfordate
##
##
##    
##### date 2 and NAME  ****
##
##      
##    if (Date2!="" and Name!=""):
##      Date2 = request.POST["datepicker1"]
##      print "date:::::",Date2
##      Date2=Date2.replace("20","")
##      print "new D2=====",Date2
##      tmp2=''
##      count=0
##      tmp=Date2
##      tmp2 = tmp.split('/')
##      tmp2.reverse()
##      print "tmp",tmp2
##      l=tmp2[0]
##      m=tmp2[1]
##      n=tmp2[2]
##      flag=0
##      user_date1=l+'/'+n+'/'+m 
##      print "user_date1" , user_date1
##
##    #status= request.POST["status"]
##
##      
##      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
##      print "system date and time___________",sys_date_time
##
####           
####           user_date1=l+'-'+n+'-'+m 
####           print "new DATE &&&&&&&&&  ",user_date1
##           
##
##      endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
##      
##      startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")
##
##      print "start date________________",startDate
##      print "\n end date_______________",endDate 
##
##      count_list=[]
##      date_list=[]
##      flag1=0
##
##           #incrementing the start date by 1 day untill the end date is reached
##      while(1):
##            if flag1==0:
##               date1 = str(startDate)
##               date1 = date1.split(" ")
##               date_list.append(date1[0])
##               flag1=1
##            else:   
##               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
##               date1 = str(startDate)
##               date1 = date1.split(" ") #fetching only the "date" part
##               print date1
##               date_list.append(date1[0]) #appending the date" part to a list
##               if startDate == endDate:
##                  break
##      print "\n final list of dates ^^^^%%$$$$$$(#*#*#*#$&$@&^$^$^$",date_list
##
##   ###### idfordate is d list which has req ids from start date to end date####
##    
##      idfordate=[]
##      for i in date_list:
##               print "i========= ",i
##               for j in listofid:
##                   print "j",j
##                   if i in j:
##                       idfordate.append(j)
##
##      print "idfordate**$$#*%(@#*$*$$", idfordate
##
##
##    ##########################################
##
##    ### if only start date is given ###
##    
####    if not Date2:
####
####         sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
####         print "sys_date_time",sys_date_time
####         
####         tmp2 = tmp.split(' ')
####         edate=tmp2[0]
####
####         print "edate",edate
####         edate1=edate.replace("-","/")
####
####         print "edate1",edate1
####         
####         endDate = datetime.datetime.strptime(edate1, "%y/%m/%d")
####      
####         startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")
####
####         print "start date________________",startDate
####         print "\n end date_______________",endDate 
####
####         count_list=[]
####         date_list=[]
####         flag1=0
####
####           #incrementing the start date by 1 day untill the end date is reached
####         while(1):
####            if flag1==0:
####               date1 = str(startDate)
####               date1 = date1.split(" ")
####               date_list.append(date1[0])
####               flag1=1
####            else:   
####               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
####               date1 = str(startDate)
####               date1 = date1.split(" ") #fetching only the "date" part
####               print date1
####               date_list.append(date1[0]) #appending the date" part to a list
####               if startDate == endDate:
####                  break
####                
####         print "\n final list of dates another loop^^^^%%$$$$$$(#*#*#*#$&$@&^$^$^$",date_list
####
####   ###### idfordate is d list which has req ids from start date to end date####
####    
####         idfordate=[]
####         for i in date_list:
####               print "i========= ",i
####               for j in listofid:
####                   print "j",j
####                   if i in j:
####                       idfordate.append(j)
####
####         print "idfordate**$$#*%(@#*$*$$", idfordate
##
##    ###########################################################################
##
##      listofresumedata=[]
##      finallist=[]
##      flag=0
##      print "idfordate**$$#*%(@#*$*$$", idfordate
##    
##      for i in idfordate:
##        print " &&&&&&&&&&&&&&&  i", i
##        list1 =dB.getResumedataById(i)
##        print "count \n"
##        listofresumedata.append(list1)
##        #listofresumedata=dB.getResumedataById(i)
##
##   # print "list:::###",listofresumedata
##
##   
##      for i in listofresumedata:
##        if flag==0:
##             print "i::##",i
##        for j in i:
##             finallist.append(j)
##             if flag==0:
##               print "j:: ", j
##               flag=1
####    print "first::",finallist[0]           
##
####
##      print "finallist \n \n ",    finallist
##      print "idfordate \n", idfordate
##      print "######################################################end"
##
##         
##   # listOfSearchResult = dB.searchReturnList(RequirementID,Client,Name,skills,Yearsofexperience,Startdate,Enddate)
##
##      listOfSearchResult=finallist
##      print "list$$$** :::",listOfSearchResult
##      
##
##      requirementid=dB.getRequirementID1()
##      list1=set(requirementid)
##      
##    msg="Please select Name, Start Date and End date for a search"
##    msg1="Please select Requirement id, Start Date and End date for a search"
##
##    if (flag2==1):
##     if( not RequirementID or not Date1 or not Date2):
##         
##       print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
##       return render_to_response('Search.html',{'msg1':msg,'Date1':Date1,'Date2':Date2,'getyear':list5,'getSkill':list4,'getClient':list3,'getSource':list2,'requirementids':list1,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
##     else:
##       return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getyear':list5,'getSkill':list4,'getClient':list3,'getSource':list2,'requirementids':list1,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})
##    
##    if( not Name or not Date1 or not Date2):
##       print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
##       return render_to_response('Search.html',{'msg':msg,'Date1':Date1,'Date2':Date2,'getyear':list5,'getSkill':list4,'getClient':list3,'getSource':list2,'requirementids':list1,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
##    else:
##       return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getyear':list5,'getSkill':list4,'getClient':list3,'getSource':list2,'requirementids':list1,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})




@csrf_exempt
def searchResult(request):
    print "IN searchResult*********************************^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

    ### dropdown skills##
  #  skills = request.POST["skills"] 
    Date1 = request.POST["datepicker"]
    Date2 = request.POST["datepicker1"]
    only_skills= request.POST["only_skills"]
    #Yearsofexperience = request.POST["Yearsofexperience"]
   # history=request.POST["history"]

    ## textbox###
    yrexp = request.POST["yrexp"]

    print "date1",Date1
    print "date2",Date2
    flag3=0
    flag2=0
    flag4=0
    flag5=0
    flag6=0
    flag7=0
    RequirementID=request.POST["ReqId"]
    Client = request.POST["Client"]
 
    Name=request.POST["Name"]
    
     #print "values from search function",skills,Name,RequirementID,Client,Yearsofexperience
    dB = DataBase()
    db1=DataBase1()

    #### Resume table ids !!!
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
          
    getClient=dB.getClient()
    list3=set(getClient)
    getSource=dB.getSource()
    list2=set(getSource)

##    getBDPOC=dB.getBDPOC()
##    list2=set(getBDPOC)
    
    getSkill=dB.getSkill()
    list4=set(getSkill)
    getyr=dB.getyrofexp()
    list5=set(getyr)

    #if RequirementID:
        
    ##### list of id as per BD name ###
##    if Name:
##         listofid=dB.getidbyBDPOC(Name)

    ##### start date to end date list @@@
    count_list=[]
    count=0

    
  ##### date1 !!!
   
    if  (Date1):
     Date1=Date1.replace("20","")
     print "new D=====",Date1
     tmp2=''
     count=0
     tmp=Date1
     tmp2 = tmp.split('/')
     tmp2.reverse()
        ##"".join(tmp2)
           
     print "tmp",tmp2
     l=tmp2[0]
    # print "l --",l
     m=tmp2[1]
     #print "m --",m
     n=tmp2[2]
     flag=0
     user_date=l+'/'+n+'/'+m 
     print "user_date:::" , user_date

     ###############################################################
####################################################################
     
##### date 2 n  reqid !!!!!
     
     if (Date2!="" and RequirementID!=""):
         
      print "\n $$$$$$$$$$$$$$$$$$$$$$$__________#)))))))))))))))@(((((((((((((((((((((((((((((((((((((@@@@@@@@@##########################"
      Date2 = request.POST["datepicker1"]
      print "date:::::",Date2
      Date2=Date2.replace("20","")
      print "new D2::: ==",Date2
      tmp2=''
      count=0
      tmp=Date2
      tmp2 = tmp.split('/')
      tmp2.reverse()
      print " \n tmp",tmp2
      l=tmp2[0]
    #  print "\n l", l
      m=tmp2[1]
      n=tmp2[2]
      flag=0
      user_date1=l+'/'+n+'/'+m 
      print "user_date1 ::" , user_date1

    #status= request.POST["status"]

      
      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
      print "system date and time___________",sys_date_time

##           
##           user_date1=l+'-'+n+'-'+m 
##           print "new DATE &&&&&&&&&  ",user_date1
           

      endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
      
      startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")

      print "start date________________",startDate
      print "\n end date_______________",endDate 

      count_list=[]
      date_list=[]
      flag1=0

           #incrementing the start date by 1 day untill the end date is reached
      while(1):
            if flag1==0:
               date1 = str(startDate)
               date1 = date1.split(" ")
               date_list.append(date1[0])
               flag1=1
            else:   
               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
               date1 = str(startDate)
               date1 = date1.split(" ") #fetching only the "date" part
               print date1
               date_list.append(date1[0]) #appending the date" part to a list
               if startDate == endDate:
                  break
      print "\n final list of dates for req id n dates $$$$$$$$$$",date_list

######## datelist has dates in format as per submission dates ######
      
      datelist=[]
      listofresumedata=[]
      finallist=[]
      flag=0
      
      for i in date_list:
          i=i.replace("20","")
          tmp2=''
          
          tmp=i
          tmp2 = tmp.split('-')
          tmp2.reverse()
          print "tmp",tmp2
          l=tmp2[0]
          m=tmp2[1]
          n=tmp2[2]
          flag=0
          user_date1=m+'/'+l+'/'+n
          datelist.append(user_date1)
      print "\n datelist date n id ::" , datelist

      ######## Fetch resume data as per req id and date !!!!!

      for i in datelist:
          list1 =dB.getResumedetailsBydateId(i,RequirementID)
          print "count \n"
          listofresumedata.append(list1)
        #listofresumedata=dB.getResumedataById(i)

      print "\n list in date n id as per req id and date====",listofresumedata

   
      for i in listofresumedata:
        if flag==0:
             print "i***",i
        for j in i:
             finallist.append(j)
             if flag==0:
               print "j%%%%% ", j
               flag=1
##    print "first::",finallist[0]           

      listOfSearchResult=finallist
   #   print "finallist date n id as per req id and date:::: \n \n ",    finallist
      print "\nlist date n id as per req id and date****::",listOfSearchResult
      
      #   fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
      s=' '
      for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                #print "\n l", len(mb)
                 
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                       
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
      

      requirementid=dB.getRequirementID1()
      list1=set(requirementid)
      flag2=1
          
 ####################################################################
  ############################################    
   ###################################

    
### date 2 and NAME  ****

      
    if (Date2!="" and Name!=""):
      Date2 = request.POST["datepicker1"]
      print "date:::::",Date2
      Date2=Date2.replace("20","")
      print "new D2=====",Date2
      tmp2=''
      count=0
      tmp=Date2
      tmp2 = tmp.split('/')
      tmp2.reverse()
      print "tmp",tmp2
      l=tmp2[0]
      m=tmp2[1]
      n=tmp2[2]
      flag=0
      user_date1=l+'/'+n+'/'+m 
      print "user_date1" , user_date1

    #status= request.POST["status"]
      
      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
      print "system date and time___________",sys_date_time

##           
##           user_date1=l+'-'+n+'-'+m 
##           print "new DATE &&&&&&&&&  ",user_date1
         
      endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
      
      startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")

      print "start date________________",startDate
      print "\n end date_______________",endDate 

      count_list=[]
      date_list=[]
      flag1=0

           #incrementing the start date by 1 day untill the end date is reached
      while(1):
            if flag1==0:
               date1 = str(startDate)
               date1 = date1.split(" ")
               date_list.append(date1[0])
               flag1=1
            else:   
               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
               date1 = str(startDate)
               date1 = date1.split(" ") #fetching only the "date" part
               print date1
               date_list.append(date1[0]) #appending the date" part to a list
               if startDate == endDate:
                  break
      print "\n final list of dates  &$@&^$^$^$",date_list

   
    ##########################################

    ##         print "idfordate**$$#*%(@#*$*$$", idfordate

    ###########################################################################

      listofresumedata=[]
      finallist=[]
      flag=0
##      print "idfordate**$$#*%(@#*$*$$", idfordate

      datelist=[]
        
##      
      for i in date_list:
         i=i.replace("20","")
         tmp2=''             
         tmp=i
         tmp2 = tmp.split('-')
         tmp2.reverse()
         print "tmp",tmp2
         l=tmp2[0]
         m=tmp2[1]
         n=tmp2[2]
         flag=0
         user_date1=m+'/'+l+'/'+n
         datelist.append(user_date1)
      print "\n datelist ::" , datelist

      ###### fetch resumedata as per date n name
      
      for i in datelist:
        print " &&&&&&&&&&&&&&&  i", i
        list1 =dB.getResumedataBydate_and_name(i,Name)
        print "count \n"
        listofresumedata.append(list1)
        #listofresumedata=dB.getResumedataById(i)

      print "list:::###",listofresumedata

   
      for i in listofresumedata:
        if flag==0:
             print "i::##",i
        for j in i:
             finallist.append(j)
             if flag==0:
               print "j:: ", j
               flag=1



      print "######################################################end"

         
   # listOfSearchResult = dB.searchReturnList(RequirementID,Client,Name,skills,Yearsofexperience,Startdate,Enddate)

      listOfSearchResult=finallist
      print "\n finallist \n \n ",    finallist
      print "list$$$** :::",listOfSearchResult
   

   
    ####   fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
      s=' '
      for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                       for j in k:
##                        i.append(j)
##                        flag9=0
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
      
      flag4=1
      requirementid=dB.getRequirementID1()
      list1=set(requirementid)


########################################
      ################################ ONLY   REQ   ID  !!!!!!!!!!!!!!
      
    if (RequirementID ):

        listofids=[]
        list44=[]
        db=DataBase()
        db1=DataBase1()
        listOfSearchResult=db.getResumedataById(RequirementID)
        print "\nlistofdata",listOfSearchResult
        

##        ####### 
##        for i in listOfSearchResult:
##            for j in i:
##                list44.append(j)
##        print "\n list44---",list44
        

####### fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
        s=' '
        for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                      
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
        flag3=1
        
        
##        listofmbno=db1.getmbno()
##
##        mobile=[]
##
##        for x in  listofmbno:
##           if x not in mobile:
##                    mobile.append(x)
##        print "\nmmmms__", mobile
##
##        listmb=[]
##        for i in mobile:
##            
##          mb=db1.getresumestatuschange(i)
##          listmb.append(mb)
##          
##        print "\n listmb:", listmb    
            

##        db.getresumestatuschanges()
##         


 ####################################################
        ####################  ONLY  SKILLS  ##########

      
  #  only_skills= request.POST["only_skills"]
    if (only_skills):
        db=DataBase()
        listOfSearchResult=db.getResumedataByskills(only_skills)
        print "\n only_skills:::",listOfSearchResult
        
        #   fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
        s=' '
        for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                       for j in k:
##                        i.append(j)
##                        flag9=0
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
        
        flag6=1

         ########################################
      ################################ Yrs of Experiance and Skills  !!!!!!!!!!!!!!

    listofdata=[]
    getClient=dB.getClient()
    list8=set(getClient)
     
    if (only_skills and yrexp ):
        db=DataBase()
        flag7=1
        print "\ns n y", only_skills
        print "\ny",yrexp

        ####### if yr of exp has comma separeted values ###
        
        k=yrexp.find(',')
        if (k >= 1):
            print "comma detected"
            s=yrexp.split(",")
            print"s:::",s
            length=len(s)
            flag=0
            j=0
            v=s[1]
            l=[]
            v=int(s[1])
             
            ##############
          
            if(flag==0):
                    l.append(s[0])
                    flag=1
                   
            if(flag==1):
                 print "lfff",l[j]
                      
                 if(s[0]!=s[1]):
                    while True:
                      print "heloo"
                      if(l[j-1]==v):
                          break;
                      if j==0:
                          j=1
                      l[j-1]=int(l[j-1])
                      print "add",l[j-1]+1
                                         
                      l.append(l[j-1]+1)
                      j=j+1

            print "list:",l
            
           ##### if both same nos in s list then break,  ####
            ###########################

            if(s[0]==s[1]):
##                l.append(s[0])
                  #break;
                  print "list:####",l
        #############

    ####### if yr of exp has / separeted values 
    
        k=yrexp.find('/')
        if (k >= 1):
            print "/detected"
            s=yrexp.split("/")
            print"s:::",s
            length=len(s)       
            v=s[1]
            l=[]
                
            ##############
            i=0
            while (len(l)!=len(s)):
               l.append(s[i])
               i=i+1
             
            print "list:####",l
#######################################         

###########  yr of exp  has only one value ############################

        else:          
          listOfSearchResult=db.getResumedataByonly_skills_Yearsofexperience(only_skills,yrexp)
          list3=listOfSearchResult
          for i in list3:
            
            for j in i:
                 print "j",j
                 k=i[15]
                 print "k",k
                 print "k[:1]",k[:1]
            if (k[:1]==yrexp):
                 listofdata.append(i)
                 
          print "\nlistofdata:::",  listofdata

        #   fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
        s=' '
        for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb
             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                       for j in k:
##                        i.append(j)
##                        flag9=0
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
       # print "\nlistofdata for only_skills and Yearsofexperience",listOfSearchResult
       
    if(flag7==1):
         print "\n huh"
         if (listofdata!=" "):
           return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list8,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listofdata })
         else:
           msg="No resumes are found for this search combination"
           return render_to_response('Search.html',{'message':msg,'Date1':Date1,'Date2':Date2,'getClient':list8,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listofdata })



        
    ########################################
      ################################ Client and Skills  !!!!!!!!!!!!!!

    if (Client and  only_skills):
        db=DataBase()
        
        listOfSearchResult=db.getResumedataByClient_skills(Client,only_skills)
        print "listofdata for Client and skills",listOfSearchResult
        
          #   fetch the status chnages of resume for each resume using mobile no. (i[5]) ############
        ##################################################################
        
        s=' '
        for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
                      break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
        flag5=1
        
    msg="Please select Name, Start Date and End date for a search"
    msg1="Please select Requirement id, Start Date and End date for a search"
    msg2="Select atleast Client and Requirement ID for a search"
    msg3="Select something for a search"
    msg5="Please select Client and Skills "

    if (flag6==1):
        return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})
        

    if (flag7==1):
        print "\n byeee"
        return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listofdata })

    
    if(flag3==1):
        if(not RequirementID):
          return render_to_response('Search.html',{'msg2':msg,'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
        else:
          return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})


    if (flag2==1):
     if( not RequirementID or not Date1 or not Date2):
         
       print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg1
       return render_to_response('Search.html',{'msg1':msg,'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
     else:
       return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})

    if (flag5==1):
     if( not Client or not skills):
         
       print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg5
       return render_to_response('Search.html',{'msg5':msg,'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
     else:
       return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})



    if(flag4==1):
      if( not Name or not Date1 or not Date2):
        print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
        return render_to_response('Search.html',{'msg':msg,'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result"})
      else:
        return render_to_response('Search.html',{'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})
    else:
        return render_to_response('Search.html',{'msg3':msg,'Date1':Date1,'Date2':Date2,'getClient':list3,'getSource':list2,"msgRed":"","msgBlue":"","msgGreen":"In search result"})






@csrf_exempt
def searchResult1(request):
    print "IN searchResult*********************************^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    #Skills,name,Mobile_Number
    #skills = request.POST["skills"]
#    print "skill in search result function",skills
    #name = request.POST['name']
    msg="Please fill atleast one field"
    dB = DataBase()
    requirementid=dB.getReqID()
    getClient=dB.getClient()
    list3=set(getClient)
    list1=['Open','Close','On_hold','Resume']

    getSource=dB.getSource()
    list2=set(getSource)
  

    RequirementID=request.POST["ReqId"]
    Status = request.POST["status"]
    Client = request.POST["Client"]
    #Yearsofexperience = request.POST["Yearsofexperience"]
    
    print "%%%%%%%%%%%%%%%%%%%%%",Status
    print "#################",RequirementID
    print "^^^^^^^^^^^^^^^^^^^^^^",Client
    

    print "values from search function",RequirementID,Client,Status
    dB = DataBase()
    listOfSearchResult = dB.searchReturnList1(RequirementID,Client,Status)
    
  #  print "listofserachs ::::",listOfSearchResult

    if( not RequirementID and not Status and not Client):
       print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
       listOfSearchResult=dB.searchRequirement()
       return render_to_response('RequirementManagement.html',{'getSource':list2,'list':list1,'getClient':getClient,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})
    else:
       print "msg1::::::", listOfSearchResult
       return render_to_response('RequirementManagement.html',{'getSource':list2,'list':list1,'getClient':list3,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})




@csrf_exempt
def searchResume(request):
    global Value
    Value2=Value
    print'####VALUE####',Value2
    dB=DataBase()
    db1=DataBase1()
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
    getClient=dB.getClient1()
    list3=set(getClient)
    
    getSource=dB.getSource()
    list2=set(getSource)

##    getBDPOC=dB.getBDPOC()
##    list2=set(getBDPOC)
    
    getSkill=dB.getSkill()
    list4=set(getSkill)
    getyr=dB.getyrofexp()
    list5=set(getyr)
    listOfSearchResult=dB.searchAll(Value2)
 
    print "list **",listOfSearchResult

    s=' '
    for i in listOfSearchResult:
        #    listofids.append(i[5])
            print "\ni[5]", (i[5])
            length=len(i)
            mb=db1.getresumestatuschange(i[5])
            print "\n mb:::",mb

            u=0
            for k in mb:
                
                print "\n org mb:",mb
             
                print "\n l", len(mb)
 
                
                if (len(mb))>1:
                   u=u+1
                   s = ', '.join(k) + ','+s
                   print "\n mb::jon::",s
                   
                   
                if(len(mb)==0):
##                       for j in k:
##                        i.append(j)
##                        flag9=0
                   break;
                   
                elif(len(mb)==1):

                    for j in k:
                        i.append(j)

                if (u==len(mb)):
                     i.append(s)
    
    statusofresume=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
    
    return render_to_response('Search.html',{'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult})
	
@csrf_exempt
def searchRequirements(request):
    dB=DataBase()
    listOfSearchResult1=dB.searchRequirement()
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
    getClient=dB.getClient1()
    list3=set(getClient)
    
##    getBDPOC=dB.getBDPOC()
##    list2=set(getBDPOC)
    getSource=dB.getSource()
    list2=set(getSource)
    
    getSkill=dB.getSkill()
    list4=set(getSkill)
    getyr=dB.getyrofexp()
    list5=set(getyr)
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print str(listOfSearchResult1)
    
    return render_to_response('Search.html',{'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult1':listOfSearchResult1})

@csrf_exempt
def searchRequirements1(request):
    dB=DataBase()
    listOfSearchResult1=dB.searchRequirement()
    dB = DataBase()
    getSource=dB.getSource()
    list2=set(getSource)
    requirementid=dB.getReqID()
    getClient=dB.getClient()
    list3=set(getClient)
   # return render_to_response('RequirementManagement.html',{'requirementids':requirementid,'getClient':getClient})
    list1=['Open','Close','On_hold','Resume']

    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print str(listOfSearchResult1)
    
    return render_to_response('RequirementManagement.html',{'list':list1,'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"","msgGreen":"In search result",'listSearchResult':listOfSearchResult1})



####### SHOW OPEN STATE RESUMES
@csrf_exempt
def openstateresume(request):
   dB=DataBase()
   state='open'
   listofopenresumes=dB.searchopenstateresumes(state)
   print listofopenresumes
   return render_to_response('openstateresume.html',{'list':listofopenresumes})



  ##### DOWNLOAD FILE ON CLIENT MACHINE  
@csrf_exempt
def download(request,file_name):
    file_path =os.getcwd()+'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    nameOnly = file_name.split('/')
    response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
    return response



###### GET IP of Client machine
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print x_forwarded_for,"One Two Three"
    if x_forwarded_for:
        print "inside if"
        ip = x_forwarded_for.split(',')[0]
        print ip
    else:
        print "inside else "
        ip = request.META.get('REMOTE_ADDR')+"-'SAFTYKey'-"+request.META.get('HTTP_USER_AGENT')
        print ip
    return ip



##################################################################
##################################################################
##################################################################

#to go to the page where export options are available
@csrf_exempt
def Export_to1(request):
      print "inside export_to:::::::::::::::****************************"
      status1=['DSR','WSR']
      status= request.POST["status"]
      

     ##if status=="DSR:
      
      Date1 = request.POST["datepicker"]
      print "date:::::",Date1
       
      status= request.POST["status"]
      print "status::::",status
      Source = request.POST["Source"]
      print "Source:::::",Source

      print "date",Date1
      print "status",status

      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
      print "\n system date and time___________",sys_date_time

      date=Date1.replace ("/", "-")
      print "\n new date::",date
      tmp2=''
      count=0
      tmp=date
      tmp2 = tmp.split('-')
      tmp2.reverse()
        ##"".join(tmp2)
      print "tmp",tmp2
      l=tmp2[0]
      m=tmp2[1]
      n=tmp2[2]
      flag=0
      user_date=l+'-'+n+'-'+m 
      print "\n new DATE &&&&&&&&&  ",user_date
      
      if status=="DSR":
        print "date1:: ",Date1
        
##        print "status",status
##
##        sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
##        print "system date and time___________",sys_date_time
##
##        date=Date1.replace ("/", "-")
##        print "new date",date
##        tmp2=''
##        count=0
##        tmp=date
##        tmp2 = tmp.split('-')
##        tmp2.reverse()
##        ##"".join(tmp2)
##        print "tmp",tmp2
##        l=tmp2[0]
##        m=tmp2[1]
##        n=tmp2[2]
##        flag=0
##        user_date=l+'-'+n+'-'+m 
##        print "new DATE &&&&&&&&&  ",user_date

##        i=i.replace("20","")
##              tmp2=''
##          
##              tmp=i
##              tmp2 = tmp.split('-')
##              tmp2.reverse()
##              print "tmp",tmp2
##              l=tmp2[0]
##              m=tmp2[1]
##              n=tmp2[2]
##              flag=0
##              user_date1=m+'/'+l+'/'+n
##              datelist.append(user_date1)
        date=Date1.replace("20","")
        print "\n replaced 20::",date
        
        ###########  fetch req id as per source name and dates (submission dates)
           ############################################

        dB=DataBase()
        #for i in datelist:
        list44 =dB.getReqidBydatename(date,Source)
        print "count \n"
              #listofresumedata.append(list44)
        #listofresumedata=dB.getResumedataById(i)

        print "\nlist in date n id ====",list44



        ###### unique ids out of list44###

        idfordate = []
        count=0
        count_list=[]

        for x in list44:
           if x not in idfordate:
                    idfordate.append(x)
           print "\nidfordate__", idfordate

           
     ##   #######  count  no.  of  resumes per id###########      
        for i in idfordate:
               for j in list44:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
        print "\n c===",count_list

###### since listofresumedata is list of list of list i.e [[[]]] hence list55
##           
##           list55=[]
##           for i in listofresumedata:
##               for j in i:
##                   for k in j:
##                     list55.append(k)
##           print "list55\n",list55
##
##  ###### unique ids out of list55###
##           
##           idfordate = []
##           
##           for x in list55:
##             if x not in idfordate:
##                  idfordate.append(x)
##           print "\nidfordate__", idfordate
##           
##          # listresult=set(listofresumedata)
##           #idfordate=list(listresult)
##           count=0
##           count_list=[]
##           
##   #######  count  no.  of  resumes per id###########
##
##           
##           for i in idfordate:
##               for j in list55:
##                   if (i==j):
##                       count=count+1
##               count_list.append(count)
##               count=0
##           print "\n c===",count_list
        
##        db=DataBase()
##        ### IDS from Submit_requir table
##        listId_Submit_requir_table=db.getRequirementID()
##       # print "list of ids from submit_require::: ",listId_Submit_requir_table
##
##        
##       # print listofReqId
##        ### IDS from Submit_resume table
##        listId_Submit_resume_table=db.getRequirementID1()
##      #  print "\nlist of ids from submit_resume:::  ",listId_Submit_resume_table
##
##        listofDetaireq=[]
##        listofid=[]
##        list1= set(listId_Submit_resume_table)
##
##        print "\nunique list of submit resume",list1
##
##        length=len(listId_Submit_resume_table)
##        print "length:::",length
##        count_list=[]
##        count=0
##        list21=[]
##        
##        for id1 in (listId_Submit_requir_table):
##                if(user_date in id1):
##                    
##                    listofDetaireq.append(id1)
##
##          ### Lsit of ids for a source          
##        listofid=db.getidbySource(Source)
##        print "\nreturned list as per source name::",listofid
##        
##        # set(listofid)
##
##
##        
##        ### List of unique ids for a source 
##        output = []
##        for x in listofid:
##             if x not in output:
##                  output.append(x)
##        print "\nout__", output
##
##        
##   #     print "list of submit res:::",listId_Submit_resume_table
##        
####        
##
##        for i in output:
##                   strr=str(i)
##                   d=strr.replace("u","")
##                   d=d.lower()
##                   d=d.lstrip()
##                   d=d.rstrip()
##                   list21.append(d)
##        print "\nlist21====",list21
##
##        ### list5:::: List of unique ids with a particular date of a source 
##        list5=[]
##        for id1 in output:
##                if(user_date in id1):
##                    
##                    list5.append(id1)
##        print "\nlist5=",list5
##
##        
##        
##        for i in list5:
##          #  print "i=",i
##            for j in listofid:
##
##                if i==j:
##                    count=count+1
##            print count
##            count_list.append(count)
##            count=0
##               
##                   #if(j==length-1)
##                 
##        print "\ncount_list" ,count_list
        
        
        ############# EXCEL SHEET for DSR###########
        
        server_path_views = os.getcwd()
                
        dummy1=[]
        dummy2=[]

       # header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
        k = process(idfordate,count_list,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
        print "value k in export______________",k

      #  k = header + k

                        
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1")
        i=0
        j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


        
        tmp2 = Source.split('@')
        m1=tmp2[0]
        print "source ka m::::",m1
       
        sheet1.write(i,j,"Report of "+m1 +" for date "+user_date)
        
        if(len(idfordate)!=0):
           sheet1.write(i+2,j,"Requirement ID")
           sheet1.write(i+2,j+1,"Count of Resumes")
                        #sheet1.write(i+2,j,"Build")
                        #sheet1.write(i+3,j,"Module")

        
        if(len(idfordate)!=0):
            
           for m in idfordate:
                  sheet1.write(i+3,j,m)
                  j=0
                  i=i+1
           i=0
           for c in  count_list:
                  sheet1.write(i+3,j+1,c)
                 
                  i=i+1  
                        
##                        sheet1.write(i+1,j,product)
##                        sheet1.write(i+1,j+1,release)
##                        

##                        i=i+6
                   ## Size of cell
                  
        
           i=i+6
        else:
           msg="No Resumes have been found"
           sheet1.write(i+3,j,msg)


            
        for row in k:
               j=0
               for col in row:
                    # sheet1.write(i, j, col)
                     sheet1.col(0).width = 290 * max([len(row[0]) for row in k])
                     sheet1.col(1).width = 100 * max([len(row[0]) for row in k])
                     j=j+1
               i=i+1


       

        tmp2 = Source.split('@')
        m=tmp2[0]
        print "source ka m::::",m   
        name1 = "Report of " + str(m)+ " for "+ str(user_date) + ".xls"
        
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
        file_path =os.getcwd()+'//'+ name1
        book.save(file_path)
        val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
        print "file pth_________",file_path
        file_wrapper = FileWrapper(file(file_path,'rb'))
        print "file wrap____________",file_wrapper
        file_mimetype = mimetypes.guess_type(file_path)
        print "mime type_____________",file_mimetype
        response = HttpResponse(file_wrapper, content_type=file_mimetype )
        response['X-Sendfile'] = file_path
        response['Content-Length'] = os.stat(file_path).st_size
        nameOnly = name1.split('/')
        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
        return response




############ WSR ############

      if status=="WSR":
           count_list=[]
           count=0
           Date1 = request.POST["datepicker"]
           
           Date1=Date1.replace("20","")
           print "new D=====",Date1

           tmp2=''
           count=0
           tmp=Date1
           tmp2 = tmp.split('/')
           tmp2.reverse()
        ##"".join(tmp2)
           
           print "tmp",tmp2
           l=tmp2[0]
           print "l --",l
           m=tmp2[1]
           print "m --",m
           n=tmp2[2]
           flag=0
           user_date=l+'/'+n+'/'+m 
           print "user_date:::" , user_date

           Date2 = request.POST["datepicker1"]
           print "date:::::",Date2

           Date2=Date2.replace("20","")
           print "new D2=====",Date2

           
           tmp2=''
           count=0
           tmp=Date2
           tmp2 = tmp.split('/')
           tmp2.reverse()
                   
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date1=l+'/'+n+'/'+m 
           print "user_date1" , user_date1

           #print "date********",Date2
           status= request.POST["status"]

           Source = request.POST["Source"]
           print "Source:::::",Source
        
           db=DataBase()
           
           sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
           print "system date and time___________",sys_date_time

##           date=Date2.replace ("/", "-")
##           print "new date",date
##           tmp2=''
##           count=0
##           tmp=date
##           tmp2 = tmp.split('-')
##           tmp2.reverse()
##        ##"".join(tmp2)
##           
##           print "tmp",tmp2
##           l=tmp2[0]
##           m=tmp2[1]
##           n=tmp2[2]
##           flag=0
##           user_date1=l+'-'+n+'-'+m 
##           print "new DATE &&&&&&&&&  ",user_date1
           

           endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
        
           startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")

           print "start date________________",startDate

           print "end date_______________",endDate 

           count_list=[]
           date_list=[]
           flag1=0
           
           #incrementing the start date by 1 day untill the end date is reached
           while(1):
             if flag1==0:
               date1 = str(startDate)
               date1 = date1.split(" ")
               date_list.append(date1[0])
               flag1=1
             else:   
               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
               date1 = str(startDate)
               date1 = date1.split(" ") #fetching only the "date" part
               print date1
               date_list.append(date1[0]) #appending the date" part to a list
               if startDate == endDate:
                  break
           print "\nfinal list of dates______________",date_list


################ converts dates to format matching to submission dates#########
           ###################################
           
           datelist=[]
           listofresumedata=[]
           finallist=[]
           flag=0
      
           for i in date_list:
              i=i.replace("20","")
              tmp2=''
          
              tmp=i
              tmp2 = tmp.split('-')
              tmp2.reverse()
              print "tmp",tmp2
              l=tmp2[0]
              m=tmp2[1]
              n=tmp2[2]
              flag=0
              user_date1=m+'/'+l+'/'+n
              datelist.append(user_date1)
           print "\n datelist date n id ::" , datelist

##############  fetch req id as per source name and dates (submission dates)
           ############################################

           dB=DataBase()
           for i in datelist:
              list44 =dB.getReqidBydatename(i,Source)
              print "count \n"
              listofresumedata.append(list44)
        #listofresumedata=dB.getResumedataById(i)

           print "\nlist in date n id ====",listofresumedata

###### since listofresumedata is list of list of list i.e [[[]]] hence list55
           
           list55=[]
           for i in listofresumedata:
               for j in i:
                   for k in j:
                     list55.append(k)
           print "list55\n",list55

  ###### unique ids out of list55###
           
           idfordate = []
           
           for x in list55:
             if x not in idfordate:
                  idfordate.append(x)
           print "\nidfordate__", idfordate
           
          # listresult=set(listofresumedata)
           #idfordate=list(listresult)
           count=0
           count_list=[]
           
   #######  count  no.  of  resumes per id###########

           
           for i in idfordate:
               for j in list55:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
           print "\n c===",count_list
          
        
          ### Lsit of ids for a source          
##           listofid=db.getidbySource(Source)
##           print "\nreturned id list as per source name::",listofid
##
##          ### List of unique ids for a source 
##           output = []
##           for x in listofid:
##             if x not in output:
##                  output.append(x)
##           print "\nout__", output
##
##            #output = set(listofid), output=list(output)
##
##          ### List of unique ids for matching dates for a source 
##
##           idfordate=[]
##           for i in date_list:
##               #print "i========= ",i
##               for j in output:
##                #   print "j",j
##                   if i in j:
##                       idfordate.append(j)
##
##                    
##           print "\nidfordate:::::",idfordate
## 
##          # print "\nlistofids" ,listofid
##              
##           for i in idfordate:
##               print "i=",i
##               for j in listofid:
##                   if i==j:
##                       count=count+1
##                    
##               print "count=====",count
##               count_list.append(count)
##               count=0


               
######            WSR EXCEL SHEET   ###

           print "\ncount_list----",count_list

                           
           server_path_views = os.getcwd()
           print "s:::",server_path_views
                
           dummy1=[]
           dummy2=[]

       # header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
           k = process(idfordate,count_list,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
           print "value k in export______________",k

      #  k = header + k

                        
##                       

           book = xlwt.Workbook(encoding="utf-8")
           sheet1 = book.add_sheet("Sheet 1")
           i=0
           j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


           date=Date1.replace ("/", "-")
           print "new date",date
           tmp2=''
           count=0
           tmp=date
           tmp2 = tmp.split('-')
           tmp2.reverse()
        ##"".join(tmp2)
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date11=l+'-'+n+'-'+m 
           print "new DATE &&&&&&&&&  ",user_date11

               
           date=Date2.replace ("/", "-")
           print "new date",date
           tmp2=''
           count=0
           tmp=date
           tmp2 = tmp.split('-')
           tmp2.reverse()
        ##"".join(tmp2)
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date22=l+'-'+n+'-'+m 
           print "new DATE &&&&&&&&&  ",user_date22

               
                       # sheet1.insert_bitmap('Drawing000.bmp',2,5 )
           tmp2 = Source.split('@')
           m=tmp2[0]
           print "\nsource ka m::::",m

           sheet1.write(i,j,"Report of " + str(m)+ " from "+ str(user_date11) + " to "+str(user_date22))
           
           if(len(idfordate)!=0):
              sheet1.write(i+2,j,"Requirement ID")
              sheet1.write(i+2,j+1,"Count of Resumes")
                        #sheet1.write(i+2,j,"Build")
                        
        
              for m1 in idfordate:
                  sheet1.write(i+3,j,m1)
                  j=0
                  i=i+1
              i=0
              for c in  count_list:
                  sheet1.write(i+3,j+1,c)
                  #j=1
                  i=i+1      

##                        i=i+6
                   ## Size of cell
                  
        
              i=i+6
           
           else:
             msg="Sorry, no Resumes have been found."
             sheet1.write(i+3,j,msg)

           
           for row in k:
                 j=0
                 for col in row:
                    # sheet1.write(i, j, col)
                     sheet1.col(0).width = 281 * max([len(row[0]) for row in k])
                     sheet1.col(1).width = 100 * max([len(row[0]) for row in k])
                     j=j+1
                 i=i+1
##                
##                 user_date22=l+'-'+n+'-'+m

                 
##                 print "new DATE &&&&&&&&&  ",user_date22
##
##               
##                       # sheet1.insert_bitmap('Drawing000.bmp',2,5 )
##           tmp2 = Source.split('@')
##           m=tmp2[0]
##           print "source ka m::::",m
                 
           name1 = "Report of " + str(m)+ " from "+ str(user_date11) + " to "+str(user_date22) +".xls"
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
           file_path =os.getcwd()+'//'+ name1
           book.save(file_path)
           val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
           print "file pth_________",file_path
           file_wrapper = FileWrapper(file(file_path,'rb'))
           print "file wrap____________",file_wrapper
           file_mimetype = mimetypes.guess_type(file_path)
           print "mime type_____________",file_mimetype
           response = HttpResponse(file_wrapper, content_type=file_mimetype )
           response['X-Sendfile'] = file_path
           response['Content-Length'] = os.stat(file_path).st_size
           nameOnly = name1.split('/')
           response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
           return response
 
               
       # global username
        #global username1
        #username1=username
        #print "USERENAMWE IN CREATEUSER",username
        
##        obj_session = shriaccess3.Admin_sessionid()
##        flag=obj_session.session_validation(username)

        
       #
##                        list_run = []
##                        list_run.append(i)
##                        #### "run" method is called
##                        run = obj2.run('fetch',list_run)
##                        if run:
##                                product.append(i)



 
               
       # global username
        #global username1
        #username1=username
        #print "USERENAMWE IN CREATEUSER",username
        
##        obj_session = shriaccess3.Admin_sessionid()
##        flag=obj_session.session_validation(username)
                                 
##                        
##                print "actual product list = ",product


       
      if (status=="WSR"):
##          if( not Date1 and not Status and not Date2):
##             print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
##       
##       return render_to_response('RequirementManagement.html',{"msg":msg,
             return render_to_response('RequirementManagement.html',{'Date1':Date1,'status':status1,'Date2':Date2})
      else:
             return render_to_response('RequirementManagement.html',{'Date1':Date1,'status':status1})


##############################################################################################

###############################################################################################
#to export the data on export_details.html



###################################  NEW EXPORT_TO ##############################
            ################################################################


            

#to go to the page where export options are available
@csrf_exempt
def Export_to(request):
      print "inside export_to:::::::::::::::****************************"
      status1=['DSR','WSR']
      

     ##if status=="DSR:
      
      Date1 = request.POST["datepicker"]
      print "date:::::",Date1
       
      status= request.POST["status"]
      print "status::::",status
      Source = request.POST["Source"]
      print "Source:::::",Source

      print "date",Date1
      print "status",status

      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
      print "\n system date and time___________",sys_date_time

      date=Date1.replace ("/", "-")
      print "\n new date::",date
      tmp2=''
      count=0
      tmp=date
      tmp2 = tmp.split('-')
      tmp2.reverse()
        ##"".join(tmp2)
      print "tmp",tmp2
      l=tmp2[0]
      m=tmp2[1]
      n=tmp2[2]
      flag=0
      user_date=l+'-'+n+'-'+m 
      print "\n new DATE &&&&&&&&&  ",user_date
      
      if status=="DSR":
        print "date1:: ",Date1
        
##    
##              user_date1=m+'/'+l+'/'+n
##              datelist.append(user_date1)
        date=Date1.replace("20","")
        print "\n replaced 20::",date

        
        
        ###########  fetch req id as per source name and dates (submission dates)
           ############################################

        dB=DataBase()
        #for i in datelist:
        list44 =dB.getReqidBydatename(date,Source)
        print "count \n"
              #listofresumedata.append(list44)
        #listofresumedata=dB.getResumedataById(i)

        print "\nlist in date n id ====",list44



        ###### unique ids out of list44###

        idfordate = []
        count=0
        count_list=[]

        for x in list44:
           if x not in idfordate:
                    idfordate.append(x)
           print "\nidfordate__", idfordate

           
     ##   #######  count  no.  of  resumes per id###########      
        for i in idfordate:
               for j in list44:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
        print "\n c===",count_list

###### 
##                 
##        print "\ncount_list" ,count_list
        



        ##################################################################
        ############# EXCEL SHEET for DSR###########
        
        server_path_views = os.getcwd()
                
        dummy1=[]
        dummy2=[]

       # header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
        k = process(idfordate,count_list,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
        print "value k in export______________",k

      #  k = header + k

                        
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1")
        i=0
        j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


        
        tmp2 = Source.split('@')
        m1=tmp2[0]
        print "source ka m::::",m1
       
        sheet1.write(i,j,"Report of "+m1 +" for date "+user_date)
        
        if(len(idfordate)!=0):
           sheet1.write(i+2,j,"Requirement ID")
           sheet1.write(i+2,j+1,"Count of Resumes")
                        #sheet1.write(i+2,j,"Build")
                        #sheet1.write(i+3,j,"Module")

        
        if(len(idfordate)!=0):
            
           for m in idfordate:
                  sheet1.write(i+3,j,m)
                  j=0
                  i=i+1
           i=0
           for c in  count_list:
                  sheet1.write(i+3,j+1,c)
                 
                  i=i+1  
                        
##                        sheet1.write(i+1,j,product)
##                        sheet1.write(i+1,j+1,release)
##                        

##                        i=i+6
                   ## Size of cell
                  
        
           i=i+6
        else:
           msg="No Resumes have been found"
           sheet1.write(i+3,j,msg)


            
        for row in k:
               j=0
               for col in row:
                    # sheet1.write(i, j, col)
                     sheet1.col(0).width = 1300 * max([len(row[0]) for row in k])
                     sheet1.col(1).width = 700 * max([len(row[0]) for row in k])
                     j=j+1
               i=i+1


       

        tmp2 = Source.split('@')
        m=tmp2[0]
        print "source ka m::::",m   
        name1 = "Report of " + str(m)+ " for "+ str(user_date) + ".xls"
        
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
        file_path =os.getcwd()+'//'+ name1
        book.save(file_path)
        val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
        print "file pth_________",file_path
        file_wrapper = FileWrapper(file(file_path,'rb'))
        print "file wrap____________",file_wrapper
        file_mimetype = mimetypes.guess_type(file_path)
        print "mime type_____________",file_mimetype
        response = HttpResponse(file_wrapper, content_type=file_mimetype )
        response['X-Sendfile'] = file_path
        response['Content-Length'] = os.stat(file_path).st_size
        nameOnly = name1.split('/')
        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
        return response




############ WSR ############
    ###############################
    ########################
    

      if status=="WSR":
           count_list=[]
           count=0
           Date1 = request.POST["datepicker"]
           
           Date1=Date1.replace("20","")
           print "new D=====",Date1

           tmp2=''
           count=0
           tmp=Date1
           tmp2 = tmp.split('/')
           tmp2.reverse()
        ##"".join(tmp2)
           
           print "tmp",tmp2
           l=tmp2[0]
           print "l --",l
           m=tmp2[1]
           print "m --",m
           n=tmp2[2]
           flag=0
           user_date=l+'/'+n+'/'+m 
           print "user_date:::" , user_date

           Date2 = request.POST["datepicker1"]
           print "date:::::",Date2

           Date2=Date2.replace("20","")
           print "new D2=====",Date2

           
           tmp2=''
           count=0
           tmp=Date2
           tmp2 = tmp.split('/')
           tmp2.reverse()
                   
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date1=l+'/'+n+'/'+m 
           print "user_date1" , user_date1

           #print "date********",Date2
           status= request.POST["status"]

           Source = request.POST["Source"]
           print "Source:::::",Source
        
           db=DataBase()
           
           sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
           print "system date and time___________",sys_date_time

##          +n+'-'+m 
##           print "new DATE &&&&&&&&&  ",user_date1
           

           endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
        
           startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")

           print "start date________________",startDate

           print "end date_______________",endDate 

           count_list=[]
           date_list=[]
           flag1=0
           
           #incrementing the start date by 1 day untill the end date is reached
           while(1):
             if flag1==0:
               date1 = str(startDate)
               date1 = date1.split(" ")
               date_list.append(date1[0])
               flag1=1
             else:   
               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
               date1 = str(startDate)
               date1 = date1.split(" ") #fetching only the "date" part
               print date1
               date_list.append(date1[0]) #appending the date" part to a list
               if startDate == endDate:
                  break
           print "\nfinal list of dates______________",date_list


################ converts dates to format matching to submission dates#########
           ###################################
           
           datelist=[]
           listofresumedata=[]
           finallist=[]
           flag=0
      
           for i in date_list:
              i=i.replace("20","")
              tmp2=''
          
              tmp=i
              tmp2 = tmp.split('-')
              tmp2.reverse()
              print "tmp",tmp2
              l=tmp2[0]
              m=tmp2[1]
              n=tmp2[2]
              flag=0
              user_date1=m+'/'+l+'/'+n
              datelist.append(user_date1)
           print "\n datelist date n id ::" , datelist

##############  fetch req id as per source name and dates (submission dates)
           ############################################
           
           count1=0
           count_list1=[]
           uniqueid = []
           uniqueid1=[]
           count2=[]
           id1=['None']
           
           dB=DataBase()
           for i in datelist:
              list44 =dB.getReqidBydatename(i,Source)
              print "\n list44:: ",list44
              print "\ncount:: "

              uniqueid = []
              count_list1=[]
              
                  
              for x in list44:
                if x not in uniqueid:
                  uniqueid.append(x)
              print "\nuniqueid ", uniqueid

##              for x in uniqueid:
              if ((len(uniqueid))>=1):
               uniqueid1.append(uniqueid)          
            
              else:
               uniqueid1.append(id1)
            #   uniqueid2.append(id1)
               
              print "\nun1::",uniqueid1
             # print "\nuniqueid2:::", uniqueid2

              
              flag=0
              for i in uniqueid:
               print "\ni",i
               for j in list44:
                   print "\nj:",j
                   if (i==j):
                       count1=count1+1
                       print "\n c=",count1
               count_list1.append(count1)
               print "\nclllll==",count_list1

               count1=0
               flag=1
              if flag==1:
                   count2.append(count_list1)
                   print "\nloop count2:",count2
              
##              count2.append(count_list1)
##              print "\nloop count2:",count2 
               
              if ((len(uniqueid))==0):
                  count1=0
                  count_list1.append(count1)
                  count2.append(count_list1)
              print "\n count_list1===",count_list1
             
              
              listofresumedata.append(list44)
              print "\ncount2{{{{{{{{{ ", count2
        #listofresumedata=dB.getResumedataById(i)

           print "\nlist in date n id ====",listofresumedata

###### since listofresumedata is list of list of list i.e [[[]]] hence list55
           
           list55=[]
           for i in listofresumedata:
               for j in i:
                   for k in j:
                     list55.append(k)
           print "list55\n",list55

  ###### unique ids out of list55###
           
           idfordate = []
           
           for x in list55:
             if x not in idfordate:
                  idfordate.append(x)
           print "\nidfordate__", idfordate
           
          # listresult=set(listofresumedata)
           #idfordate=list(listresult)
           count=0
           count_list=[]
           
   #######  count  no.  of  resumes per id###########

           
           for i in idfordate:
               for j in list55:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
           print "\n c===",count_list


#####################   count of reqids ###################

           countid=[]
           countid1=0
           for i in uniqueid1:
            if (i==" "):
                countid1=0
                countid.append(countid1)
            else:    
                for j in i:
                   countid1=countid1+1
                
            countid.append(countid1)
            countid1=0
           print   "\ncountid::",countid
          
        
      

###############################################################################################

 ##############################################
           
######            WSR EXCEL SHEET   ######################################################

           print "\ncount_list----",count_list

                           
           server_path_views = os.getcwd()
           print "s:::",server_path_views
                
           dummy1=[]
           dummy2=[]

       # header = [('TESTCASES','STATUS (PASS/FAIL)')]

             #####   OLD  K #################                   
         #  k = process(idfordate,count_list,dummy1,dummy2)

         #process takes 4 arguments, so providing two dummy values

           k = process(datelist,count2,uniqueid1,dummy2)
           print "value k in export______________",k

      #  k = header + k
                 
##                       

           book = xlwt.Workbook(encoding="utf-8")
           sheet1 = book.add_sheet("Sheet 1")
           i=0
           j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


           date=Date1.replace ("/", "-")
           print "new date",date
           tmp2=''
           count=0
           tmp=date
           tmp2 = tmp.split('-')
           tmp2.reverse()
        ##"".join(tmp2)
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date11=l+'-'+n+'-'+m 
           print "new DATE &&&&&&&&&  ",user_date11

               
           date=Date2.replace ("/", "-")
           print "new date",date
           tmp2=''
           count=0
           tmp=date
           tmp2 = tmp.split('-')
           tmp2.reverse()
        ##"".join(tmp2)
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date22=l+'-'+n+'-'+m 
           print "new DATE &&&&&&&&&  ",user_date22
               
                       # sheet1.insert_bitmap('Drawing000.bmp',2,5 )
           tmp2 = Source.split('@')
           m=tmp2[0]
           print "\nsource ka m::::",m
           name=str(m)

           sheet1.write(i,j,"Report of " + str(m)+ " from "+ str(user_date11) + " to "+str(user_date22))



#######  d1  r1 r3 r4
 ########    4  4   2

           
           
############ new code #############
           ################################

#########################  DATES in    one column #############

           ######################### j  is  coloumn, i is row #######
           if(len(uniqueid1)!=0):

            j=0
            i=0
            flag=0
            c=['Count of Resumes :']

            for u in datelist:
             if(i==0):
                i=i+2
                sheet1.write(i,j,u)
                sheet1.write(i+1,j,c)
             else:  
                i=i+3
                sheet1.write(i,j,u)
                sheet1.write(i+1,j,c)
                j=0


######################### requirement ids #################

            i=2
            j=1
            for u in uniqueid1:
               for m in u:
                  sheet1.write(i,j,m) 
                  j=j+1
               i=i+3
               j=1


############################## count of resumes ############
               
            i=3
            j=1
##           format=book.add_format()
##           format.set_align('center')
           
            for u in count2:
               for m in u:
                   sheet1.write(i,j,m)
                   j=j+1
               i=i+3
               j=1

           else:
             msg="Sorry, no Resumes have been found."
             sheet1.write(i+3,j,msg)


##########################################################################



####           if(len(idfordate)!=0):
####              sheet1.write(i+2,j,"Requirement ID")
####              sheet1.write(i+2,j+1,"Count of Resumes")
####                        #sheet1.write(i+2,j,"Build")
####                        
####        
####              for m1 in idfordate:
####                  sheet1.write(i+3,j,m1)
####                  j=0
####                  i=i+1
####              i=0
####              for c in  count_list:
####                  sheet1.write(i+3,j+1,c)
####                  #j=1
####                  i=i+1      
######                        i=i+6
####                   ## Size of cell
####                  
####        
####              i=i+6
####           
####           else:
####             msg="Sorry, no Resumes have been found."
####             sheet1.write(i+3,j,msg)

           
           for row in k:
                 j=0
##                 print "\nrow",row
                 for col in row:
##                     print "\ncol",col
                    # sheet1.write(i, j, col)
                     sheet1.col(0).width = 580 * max([len(row[0]) for row in k])
                     sheet1.col(1).width = 1299 * max([len(row[0]) for row in k])
                     sheet1.col(2).width = 1259* max([len(row[0]) for row in k])
                     j=j+1
                 i=i+1
##                
##                 user_date22=l+'-'+n+'-'+m
        
##               
                 
           name1 = "Report of " + name+ " from "+ str(user_date11) + " to "+str(user_date22) +".xls"
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
           file_path =os.getcwd()+'//'+ name1
           book.save(file_path)
           val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
           print "file pth_________",file_path
           file_wrapper = FileWrapper(file(file_path,'rb'))
           print "file wrap____________",file_wrapper
           file_mimetype = mimetypes.guess_type(file_path)
           print "mime type_____________",file_mimetype
           response = HttpResponse(file_wrapper, content_type=file_mimetype )
           response['X-Sendfile'] = file_path
           response['Content-Length'] = os.stat(file_path).st_size
           nameOnly = name1.split('/')
           response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
           return response
          
               
       # global username
        #global username1
        #username1=username
        #print "USERENAMWE IN CREATEUSER",username
        
##        obj_session = shriaccess3.Admin_sessionid()
##        flag=obj_session.session_validation(username)

        
       # global username
        #global username1
        #username1=username
        #print "USERENAMWE IN CREATEUSER",username
        
##        obj_session = shriaccess3.Admin_sessionid()
##        flag=obj_session.session_validation(username)
                                 
##                        
##                print "actual product list = ",product


       
      if (status=="WSR"):
##          if( not Date1 and not Status and not Date2):
##             print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
##       
##       return render_to_response('RequirementManagement.html',{"msg":msg,
             return render_to_response('RequirementManagement.html',{'ids':uniqueid1,'dates':datelist,'count':count2,'Date1':Date1,'status':status1,'Date2':Date2})
      else:
             return render_to_response('RequirementManagement.html',{'ids':uniqueid1,'dates':datelist,'count':count2,'Date1':Date1,'status':status1})


##############################################################################################

###############################################################################################
#to export the data on export_details.html


#############################################end of new export_to #####################################
            ###################################################################


@csrf_exempt
def display_report(request):
    
    if request.POST.has_key('client_response'):
      Date1 = request.POST['client_response']
      Date2 = request.POST['client_response1']
      Source = request.POST['client_response2']
      status = request.POST['client_response3']
      print "date:",Date1
      print "date1",Date2
      print "source",Source
      print "report",status
      
    #  status = request.POST['status']
      
      print "======================================================================="
      print "value from drop print  inside display_report:::::::::::::down==",status
      print "======================================================================="
      print "inside display_report:::::::::::::::****************************"
      #status1=['DSR','WSR']

##      Date1 = request.POST['datepicker']
      print "date:::::",Date1
       
    #  status= request.POST["status4"]
      print "status::::",status
      
##      Date2 = request.POST['datepicker1']
      print "Date2:::::",Date2

     
##      Source= request.POST["Source"]
      print "Source",Source
      

     ##if status=="DSR:
      
      sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
      print "\n system date and time___________",sys_date_time

      date=Date1.replace ("/", "-")
      print "\n new date::",date
      tmp2=''
      count=0
      tmp=date
      tmp2 = tmp.split('-')
      tmp2.reverse()
        ##"".join(tmp2)
      print "tmp",tmp2
      l=tmp2[0]
      m=tmp2[1]
      n=tmp2[2]
      flag=0
      user_date=l+'-'+n+'-'+m 
      print "\n 1.new DATE &&&&&&&&&  ",user_date
      
      if status=="DSR":
        print "date1:: ",Date1
        
##        print "status",status
##
##        sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
##        print "system date and time___________",sys_date_time
##
##        date=Date1.replace ("/", "-")
##        print "new date",date
##        tmp2=''
##        count=0
##        tmp=date
##        tmp2 = tmp.split('-')
##        tmp2.reverse()
##        ##"".join(tmp2)
##        print "tmp",tmp2
##        l=tmp2[0]
##        m=tmp2[1]
##        n=tmp2[2]
##        flag=0
##        user_date=l+'-'+n+'-'+m 
##        print "new DATE &&&&&&&&&  ",user_date

##        i=i.replace("20","")
##              tmp2=''
##          
##              tmp=i
##              tmp2 = tmp.split('-')
##              tmp2.reverse()
##              print "tmp",tmp2
##              l=tmp2[0]
##              m=tmp2[1]
##              n=tmp2[2]
##              flag=0
##              user_date1=m+'/'+l+'/'+n
##              datelist.append(user_date1)
        date=Date1.replace("20","")
        print "\n replaced 20::",date
        
        ###########  fetch req id as per source name and dates (submission dates)
           ############################################

        dB=DataBase()
        #for i in datelist:
        list44 =dB.getReqidBydatename(date,Source)
        print "count \n"
              #listofresumedata.append(list44)
        #listofresumedata=dB.getResumedataById(i)

        print "\nlist in date n id ====",list44



        ###### unique ids out of list44###

        idfordate = []
        count=0
        count_list=[]
        id1=[["None"]]

        for x in list44:
           if x not in idfordate:
                    idfordate.append(x)
        print "\nidfordate__", idfordate

        if  (len(idfordate)==0)   :
            idfordate.append(id1)
     ##   #######  count  no.  of  resumes per id###########      
        for i in idfordate:
               for j in list44:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
        print "\n c===",count_list


############ new code ###
        
 ###### count id for colspan no. on html page ### 
        countid=[]
        countid1=0
        for i in idfordate:
          if (i==" "):
                countid1=0
                countid.append(countid1)
          else:    
                for j in i:
                   countid1=countid1+1
                
        countid.append(countid1)
        countid1=0
        print   "\ncountid::",countid


#################  Report title  ################
        
        tmp2 = Source.split('@')
        m=tmp2[0]
        print "\nsource ka m::::",m
        name1 = "Report of  " + str(m)+ "  of date   "+ str(Date1) 
        print name1


#######  JSON  OBJ  ######

        response_dict={}
         
        response_dict.update({'server_response5': count_list })
        response_dict.update({'server_response6': idfordate })
        response_dict.update({'server_response7': countid })
        response_dict.update({'server_response8': status })
        response_dict.update({'server_response9': name1 })
        response_dict.update({'server_response10':Date1})
        
        
        print "status::",status
        print "status22::",idfordate
        print "cl", count_list
        print  "countid", countid

        if (status=="DSR"):
          
		print "\n last"
                return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
        else:
                return render_to_response('RequirementManagement.html', context_instance=RequestContext(request))


        

###### since listofresumedata is list of list of list i.e [[[]]] hence list55
##           
##           list55=[]
##           for i in listofresumedata:
##               for j in i:
##                   for k in j:
##                     list55.append(k)
##           print "list55\n",list55
##
##  ###### unique ids out of list55###
##           
##           idfordate = []
##           
##           for x in list55:
##             if x not in idfordate:
##                  idfordate.append(x)
##           print "\nidfordate__", idfordate
##           
##          # listresult=set(listofresumedata)
##           #idfordate=list(listresult)
##           count=0
##           count_list=[]
##           
##   #######  count  no.  of  resumes per id###########
##
##           
##           for i in idfordate:
##               for j in list55:
##                   if (i==j):
##                       count=count+1
##               count_list.append(count)
##               count=0
##           print "\n c===",count_list
        
##        db=DataBase()
##        ### IDS from Submit_requir table
##        listId_Submit_requir_table=db.getRequirementID()
##       # print "list of ids from submit_require::: ",listId_Submit_requir_table
##
##        
##       # print listofReqId
##        ### IDS from Submit_resume table
##        listId_Submit_resume_table=db.getRequirementID1()
##      #  print "\nlist of ids from submit_resume:::  ",listId_Submit_resume_table
##
##        listofDetaireq=[]
##        listofid=[]
##        list1= set(listId_Submit_resume_table)
##
##        print "\nunique list of submit resume",list1
##
##        length=len(listId_Submit_resume_table)
##        print "length:::",length
##        count_list=[]
##        count=0
##        list21=[]
##        
##        for id1 in (listId_Submit_requir_table):
##                if(user_date in id1):
##                    
##                    listofDetaireq.append(id1)
##
##          ### Lsit of ids for a source          
##        listofid=db.getidbySource(Source)
##        print "\nreturned list as per source name::",listofid
##        
##        # set(listofid)
##
##
##        
##        ### List of unique ids for a source 
##        output = []
##        for x in listofid:
##             if x not in output:
##                  output.append(x)
##        print "\nout__", output
##
##        
##   #     print "list of submit res:::",listId_Submit_resume_table
##        
####        
##
##        for i in output:
##                   strr=str(i)
##                   d=strr.replace("u","")
##                   d=d.lower()
##                   d=d.lstrip()
##                   d=d.rstrip()
##                   list21.append(d)
##        print "\nlist21====",list21
##
##        ### list5:::: List of unique ids with a particular date of a source 
##        list5=[]
##        for id1 in output:
##                if(user_date in id1):
##                    
##                    list5.append(id1)
##        print "\nlist5=",list5
##
##        
##        
##        for i in list5:
##          #  print "i=",i
##            for j in listofid:
##
##                if i==j:
##                    count=count+1
##            print count
##            count_list.append(count)
##            count=0
##               
##                   #if(j==length-1)
##                 
##        print "\ncount_list" ,count_list
        
        
        ############# EXCEL SHEET for DSR###########
        
     
############ WSR ############

      elif status=="WSR":
           count_list=[]
           count=0
          # Date1 = request.POST['client_response1']
           #Date1 = request.POST['datepicker']
           
           Date1=Date1.replace("20","")
           print "\nnew D=====",Date1

           tmp2=''
           count=0
           tmp=Date1
           tmp2 = tmp.split('/')
           tmp2.reverse()
        ##"".join(tmp2)
           
           print "tmp",tmp2
           l=tmp2[0]
           print "l --",l
           m=tmp2[1]
           print "m --",m
           n=tmp2[2]
           flag=0
           user_date=l+'/'+n+'/'+m 
           print "user_date:::" , user_date

          # Date2 = request.POST['client_response2']
          # Date2 = request.POST['datepicker1']
           
           print "date:::::",Date2

           Date2=Date2.replace("20","")
           print "new D2=====",Date2

           
           tmp2=''
           count=0
           tmp=Date2
           tmp2 = tmp.split('/')
           tmp2.reverse()
                   
           print "tmp",tmp2
           l=tmp2[0]
           m=tmp2[1]
           n=tmp2[2]
           flag=0
           user_date1=l+'/'+n+'/'+m 
           print "\nuser_date1" , user_date1

           #print "date********",Date2
        #   status= request.POST["status"]

           #Source= request.POST["Source"]
           print "Source:::::",Source
        
           db=DataBase()
           
           sys_date_time = strftime("%Y-%m-%d %H:%M:%S")
           print "system date and time___________",sys_date_time

##           date=Date2.replace ("/", "-")
##           print "new date",date
##           tmp2=''
##           count=0
##           tmp=date
##           tmp2 = tmp.split('-')
##           tmp2.reverse()
##        ##"".join(tmp2)
##           
##           print "tmp",tmp2
##           l=tmp2[0]
##           m=tmp2[1]
##           n=tmp2[2]
##           flag=0
##           user_date1=l+'-'+n+'-'+m 
##           print "new DATE &&&&&&&&&  ",user_date1
           

           endDate = datetime.datetime.strptime(user_date1, "%y/%m/%d")
        
           startDate = datetime.datetime.strptime(user_date, "%y/%m/%d")

           print "start date________________",startDate

           print "end date_______________",endDate 

           count_list=[]
           date_list=[]
           flag1=0
           
           #incrementing the start date by 1 day untill the end date is reached
           while(1):
             if flag1==0:
               date1 = str(startDate)
               date1 = date1.split(" ")
               date_list.append(date1[0])
               flag1=1
             else:   
               startDate = startDate + datetime.timedelta(days=1) #Date contains both date AND time
               date1 = str(startDate)
               date1 = date1.split(" ") #fetching only the "date" part
               print date1
               date_list.append(date1[0]) #appending the date" part to a list
               if startDate == endDate:
                  break
           print "\nfinal list of dates______________",date_list


################ converts dates to format matching to submission dates#########
           ###################################
           
           datelist=[]
           listofresumedata=[]
           finallist=[]
           flag=0
      
           for i in date_list:
              i=i.replace("20","")
              tmp2=''
          
              tmp=i
              tmp2 = tmp.split('-')
              tmp2.reverse()
              print "tmp",tmp2
              l=tmp2[0]
              m=tmp2[1]
              n=tmp2[2]
              flag=0
              user_date1=m+'/'+l+'/'+n
              datelist.append(user_date1)
           print "\n datelist date n id ::" , datelist

##############  fetch req id as per source name and dates (submission dates)
           ############################################
           
           count1=0
           count_list1=[]
           uniqueid = []
           uniqueid1=[]
           count2=[]
           id1=[["None"]]
           
           dB=DataBase()
           for i in datelist:
              list44 =dB.getReqidBydatename(i,Source)
              print "\n list44:: ",list44
              print "\ncount:: "

              uniqueid = []
              count_list1=[]
              
                  
              for x in list44:
                if x not in uniqueid:
                  uniqueid.append(x)
              print "\nuniqueid ", uniqueid

##              for x in uniqueid:
              if ((len(uniqueid))>=1):
               uniqueid1.append(uniqueid)
               
             #  uniqueid2=uniqueid[:]
              else:
               uniqueid1.append(id1)
            #   uniqueid2.append(id1)
               
              print "\nun1::",uniqueid1
             # print "\nuniqueid2:::", uniqueid2

              
              flag=0
              for i in uniqueid:
               print "\ni",i
               for j in list44:
                   print "\nj:",j
                   if (i==j):
                       count1=count1+1
                       print "\n c=",count1
               count_list1.append(count1)
               print "\nclllll==",count_list1
##               count2.append(count_list1)
##               print "\nloop count2:",count2
               count1=0
               flag=1
              if flag==1:
                   count2.append(count_list1)
                   print "\nloop count2:",count2
              
##              count2.append(count_list1)
##              print "\nloop count2:",count2 
               
              if ((len(uniqueid))==0):
                  count1=0
                  count_list1.append(count1)
                  count2.append(count_list1)
              print "\n count_list1===",count_list1

              
              
              listofresumedata.append(list44)
              print "\ncount2{{{{{{{{{ ", count2
        #listofresumedata=dB.getResumedataById(i)

           print "\nlist in date n id ====",listofresumedata

###### since listofresumedata is list of list of list i.e [[[]]] hence list55
           
           list55=[]
           for i in listofresumedata:
               for j in i:
                   for k in j:
                     list55.append(k)
           print "list55\n",list55

  ###### unique ids out of list55###
           
           idfordate = []
           
           for x in list55:
             if x not in idfordate:
                  idfordate.append(x)
           print "\nidfordate__", idfordate
           
          # listresult=set(listofresumedata)
           #idfordate=list(listresult)
           count=0
           count_list=[]
           
   #######  count  no.  of  resumes per id###########

           
           for i in idfordate:
               for j in list55:
                   if (i==j):
                       count=count+1
               count_list.append(count)
               count=0
           print "\n c===",count_list
          
        
      


               
######            WSR EXCEL SHEET   ###

           
####            
##           response_dict = {}
##                
##               # if (len(list1)!=0):
##           response_dict.update({'server_response': uniqueid1 })
####                else:
####                    list1=['No IDs are available for this client']
####                    response_dict.update({'server_response': list1 })
####                    
##               # if (len(skill)!=0):
##           response_dict.update({'server_response_datelist': datelist })
####                else:
####                    skill=['No skills are available for this client'] 
####                    response_dict.update({'server_response_skills': skill })
##                    
##              #  if (len(yrexp)!=0):
##           response_dict.update({'server_response_count2': count2 })
####                else:
####                    yrexp=['No years of experiance are available for this client']   
####                    response_dict.update({'server_response_yrexp': yrexp  })
##           print "\ncount2:",count2
##           print "\nuniqueid1",uniqueid1
##           print "\ninside display_report   end:::::::::::::"
##           return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
##    else:
##           return render_to_response('RequirementManagement.html', context_instance=RequestContext(request))

           countid=[]
           countid1=0
           for i in uniqueid1:
            if (i==" "):
                countid1=0
                countid.append(countid1)
            else:    
                for j in i:
                   countid1=countid1+1
                
            countid.append(countid1)
            countid1=0
           print   "\ncountid::",countid

           response_dict={}

           l=[[2,4],[5],[93,4,4,5],[0]]

           tmp2 = Source.split('@')
           m=tmp2[0]
           print "\nsource ka m::::",m
           name1 = "Report of  " + str(m)+ "  from  "+ str(Date1) + " to  "+str(Date2)
           print name1

      
           response_dict.update({'server_response': countid })
           response_dict.update({'server_response1': uniqueid1 })
           response_dict.update({'server_response2': datelist })
           response_dict.update({'server_response3': count2 })
           response_dict.update({'server_response4': name1 })
           response_dict.update({'server_response8': status })

           print "countid:",countid
           print "datelist:",datelist
           print "count2:",count2
           print "uniqueid1:",uniqueid1
          
      
      if (status=="WSR"):
		 
                return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
      else:
                return render_to_response('RequirementManagement.html', context_instance=RequestContext(request))


      if (status=="DSR"):
          
		print "\n last"
                return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
      else:
                return render_to_response('RequirementManagement.html', context_instance=RequestContext(request))
            

            
       
##      if (status=="WSR"):
##             print "end of function"
####          if( not Date1 and not Status and not Date2):
####             print "msg$$$$$$$$$$$$$$$$$$$$$$$$$$$", msg
####           
####       return render_to_response('RequirementManagement.html',{"msg":msg,
##             return render_to_response('RequirementManagement.html',{'countid':countid,'ids':uniqueid1,'dates':datelist,'count':count2,'Date1':Date1,'status':status,'Date2':Date2})
##      else:
##             return render_to_response('RequirementManagement.html',{'countid':countid,'ids':uniqueid1,'dates':datelist,'count':count2,'Date1':Date1,'status':status})
##




        
@csrf_exempt
def Export(request):
        global username
        global username1
        username1=username
        print "USERENAMWE IN CREATEUSER",username
        obj_session = shriaccess3.Admin_sessionid()
        flag=obj_session.session_validation(username)
        print "FLAF VALJISDBH SHNDFONSK FHSOIJDFLSDFS",flag

        
        if (flag):

                ### Green colors are ids in html files
                Product=request.POST["Product"]
                Release=request.POST["release"]
                Build=request.POST['build']
                
                ### for dropdown box of report id is "pdf" , look in html file; id="PDF"
                Export=request.POST["PDF"]  

                product = remove_unary(Product)
                product1=product.lower()
                release = remove_unary(Release)
                build = remove_unary(Build)
                export = remove_unary(Export)
                        
                print "product in export======",product
                print "release in export======",release
                print "build in export======",build
                print "export in export======",export

                list_checkBox = []
                list_checkBox1 = []

                temp = request.POST.getlist('module')
                print "temp in export------------=",temp
                for i in range(len(temp)):
                        temp1 = remove_unary(temp[i])
                        list_checkBox1.append(temp1)

                print "modules checked = ",list_checkBox1
                print "length of list_checkBox1->",len(list_checkBox1)
                if len(list_checkBox1) == 1:
                        list_checkBox1=str(list_checkBox1[0])
                else:
                        list_checkBox1=str(list_checkBox1)

                Module=list_checkBox1
                Module = Module.lower()
                print "Module in export-----------------------------=",Module

                list_run=[]
                list_run.append(product1)
                list_run.append(release)
                list_run.append(build)
                list_run.append(Module)
                print "list_run============================================",list_run

                list_testid = []
                list_testid.append(product)
                list_testid.append(Module)
                list_testid.append(release)
                list_testid.append(build)
                print "list_testid=============================================",list_testid
                        
                #fetching runs for the selected data
                ## testexecution is a class
                
                obj = shriaccess3.testexecution()
                run = obj.run('fetch',list_run)
                run2=sorted(run)
                print "runs fetched for data in export========================",run
                j=len(run)-1
                run_lat = run[j]
                print "latest run___________________",run_lat
                        

                #fetching the status results and testcases for the latest run
                
                run1=[]
                run1.append(run_lat)
                #status
                ##testexecution is a class, status is method
                
                status = obj.status('fetch',run1)
                print "status fetched for latest run in export______________",status

                #testcases

                ##testexecution is a class, testcaseid is method
                tid = obj.testcaseid('fetch',run1)
                print "testcases fetched in export_______________",tid 
                        
                pass_var = 0
                fail_var=0
                exc=0

                for i in status:
                        if i == "pass":
                                pass_var = pass_var+1
                        else:
                                fail_var=fail_var+1

                print "no of pass===========",pass_var
                print "no of fail===========",fail_var

                ## get current working  dir
                server_path_views = os.getcwd()
                
                if (Export=='PDF'):
                        dummy1=[]
                        dummy2=[]

                        header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
                        k = process(tid,status,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
                         ## process is function.. search def process
                        
                        print "value k in export______________",k

                        k = header + k
                                
                        name = "Report_for_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".pdf"
                        print "name====",name
                        doc = SimpleDocTemplate(name,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=60)
                         
                        report = []
                        data = []
                        styles = getSampleStyleSheet()
                        styles.add(ParagraphStyle(name='Bold', fontSize=10, leading = 15, alignment=TA_LEFT))
                        t=Table(k,colWidths=[200,200],hAlign='LEFT')
                        t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                        ('TEXTCOLOR',(1,1),(-2,-2),colors.black),
                        ('VALIGN',(0,0),(0,-1),'TOP'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ]))

                                ########## For Graph##########
                        dr = Drawing(300, 300)
                        graph=Pie()
                        graph.x = 50
                        graph.y = 50
                        graph.width = 225
                        graph.height = 225
                        graph.data = [pass_var,fail_var,exc]
                        graph.labels = ['Pass','Fail','No_Run']
                        dr.add(graph)
                        dr.save(formats=['bmp'],outDir='.',fnRoot=None)

                        im = Image("Drawing000.bmp")
                        im.hAlign = 'LEFT'


                        report.append(Paragraph("Selected Product details.." ,styles["Bold"]))
                        report.append(Paragraph("Product      : "+product,styles["Bold"]))
                        report.append(Paragraph("Module : "+Module,styles["Bold"]))
                        report.append(Paragraph("Release : "+Release,styles["Bold"]))
                        report.append(Paragraph("Build : "+Build,styles["Bold"]))
                        report.append(Paragraph("-------------------------------------------",styles["Bold"]))
                        report.append(Paragraph(" ",styles["Bold"]))
                        report.append(Paragraph("Project Detailed Status ." ,styles["Bold"]))
                        report.append(Paragraph("           ",styles["Bold"]))
                        report.append(t)
                        report.append(Paragraph("-------------------------------------------",styles["Bold"]))
                        report.append(Paragraph("Pie chart." ,styles["Bold"]))
                        report.append(im)

                        # Build Document
                        doc.build(report)
                        val="Converted to Pdf"

                        #download
                        file_path =os.getcwd()+'//'+ name
                        print "file pth_________",file_path
                        file_wrapper = FileWrapper(file(file_path,'rb'))
                        print "file wrap____________",file_wrapper
                        file_mimetype = mimetypes.guess_type(file_path)
                        print "mime type_____________",file_mimetype
                        response = HttpResponse(file_wrapper, content_type=file_mimetype )
                        response['X-Sendfile'] = file_path
                        response['Content-Length'] = os.stat(file_path).st_size
                        nameOnly = name.split('/')
                        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
                        return response

                ##                return render_to_response('thanks.html',{'var':val})
                 
                elif(Export == 'XLS'):
                        dummy1=[]
                        dummy2=[]

                        header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
                        k = process(tid,status,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
                        print "value k in export______________",k

                        k = header + k

                        ########## For Graph##########
                        dr = Drawing(300, 300)
                        graph=Pie()
                        graph.x = 50
                        graph.y = 50
                        graph.width = 225
                        graph.height = 225
                        graph.data = [pass_var,fail_var,exc]
                        graph.labels = ['Pass','Fail','No_Run']
                        dr.add(graph)
                        dr.save(formats=['bmp'],outDir='.',fnRoot=None)

                        im = Image("Drawing000.bmp")
                        im.hAlign = 'LEFT'

                        book = xlwt.Workbook(encoding="utf-8")
                        sheet1 = book.add_sheet("Sheet 1")
                        i=0
                        j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


                        sheet1.write(i,j,"Product")
                        sheet1.write(i+1,j,"Release")
                        sheet1.write(i+2,j,"Build")
                        sheet1.write(i+3,j,"Module")
                                
                        sheet1.write(i,j+1,product)
                        sheet1.write(i+1,j+1,release)
                        sheet1.write(i+2,j+1,build)
                        sheet1.write(i+3,j+1,Module)

                        i=i+6
                   ## Size of cell
                        for row in k:
                                j=0
                                for col in row:
                                        sheet1.write(i, j, col)
                                        sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                                        j=j+1
                                i=i+1


                        sheet1.insert_bitmap('Drawing000.bmp',2,5 )
                        name1 = "Report_for_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
                        file_path =os.getcwd()+'//'+ name1
                        book.save(file_path)
                        val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
                        print "file pth_________",file_path
                        file_wrapper = FileWrapper(file(file_path,'rb'))
                        print "file wrap____________",file_wrapper
                        file_mimetype = mimetypes.guess_type(file_path)
                        print "mime type_____________",file_mimetype
                        response = HttpResponse(file_wrapper, content_type=file_mimetype )
                        response['X-Sendfile'] = file_path
                        response['Content-Length'] = os.stat(file_path).st_size
                        nameOnly = name1.split('/')
                        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
                        return response

                                
                ##                return render_to_response('thanks.html',{'var':val})
                elif(Export =='CVS'):
                        return render_to_response('thanks.html')
                else:
                        return render_to_response('thanks.html')
        else:
                return render_to_response('loginpage.html')
       

#################################################################################################
            #################################  PROCESS method  ################################
                        ##################################################3
length = []
def process(x1,x2,x3,x4):
        
    len_1 = len(x1)
    len_2 = len(x2)
    len_3 = len(x3)
    len_4 = len(x4)
    length.append(len_1)
    length.append(len_2)
    length.append(len_3)
    length.append(len_4)
    
    
    length.sort()
    
    
##    
##        x3.append("EMPTY")
##        
##    itr4 = length[2] - len_4
##    for i in range(itr4):
##        x4.append("EMPTY")
##        

    print "x1 = ",x1
    print "x2 = ",x2
    print "x3 = ",x3
    print "x4 = ",x4
    

    if x4 == [] and x3 == [] and x2 == []:
            print "condition1"
            zipped = zip(x1)

    elif x4 == [] and x3 == []:
            print "condition2"
            zipped = zip(x1,x2)
    elif x4 == []:
            print "condition3"
            zipped = zip(x1,x2,x3)
    else:
            zipped = zip(x1,x2,x3,x4)
    print "zipped = ",zipped
    return zipped

#############################################################Login View  starts here for Arpitha####################################################################################################
@csrf_exempt
def login(request):
    return render_to_response('loginpage.html')

@csrf_exempt
def Login_View(request):
    print ######################################################Hello#########################################################
    global Value
    global Value2
   # Value2=Value
    username = request.POST["Username"]
    password = request.POST["Password"]

    print 'username',username
    print 'password',password

    global Reference_ID
   
    #global Value
   
##    Date1 = request.POST["datepicker"]
##    Date2 = request.POST["datepicker1"]
    dB = DataBase()
    getClient=dB.getClient()
    list3=set(getClient)
    requirementid=dB.getRequirementID1()
    list1=set(requirementid)
       
    getSource=dB.getSource()
    list2=set(getSource)
      
    getSkill=dB.getSkill()
    list4=set(getSkill)
    
##    print "In the bee Value2",Value2
##    print "I am in Value",Value
    
 #   getSource=dB.getSource()
    #list2=set(getSource)
    getyr=dB.getyrofexp()
    list5=set(getyr)

    
##    dB = DataBase()
##    requirementid=dB.getRequirementID()
##    getSource=dB.getSource()
##    getClient=dB.getClient()
##    list3=set(getClient)
##    list2=set(getSource)
    statusofresume1=['Line_up','Internal_Interview','HR_Interview','COL','CI','Joining','CIS','CID','CSD']
    status1 =['Yes','No','Backout','Pending','Offered','Selected','Rejected','On_hold','Did_not_pick_call','Did_not_turn_up']
    
	
    dB=userinfo()
    
        
    tag_value,Value,Reference_ID= dB.database_fetch(username,password)
    print "&&&&&&&&&&&&&&&&&&Value",Value
    print 'tag_value',tag_value
    if tag_value==0:
        return  render_to_response('loginpage.html',{'wrong_user':'Please provide correct username/password'}) ##Please redirect to same login page with a message Username/password is wrong##
    elif tag_value==1:
        return render_to_response('Search.html',{'getSource':list2,'getClient':list3,"msgRed":"","msgBlue":"search click","msgGreen":"",'value':Value,'getSource':list2})
       # return render(request,'resumeSubmit.html',{'getClient':list3,'status123':status1,'statusofresume123':statusofresume1,'getSource':list2})
    else:
        return render_to_response('loginpage.html',{'wrong_password':'The username or password you entered is incorrect ?'}) ##Please redirect to same login page with a message Password is wrong##


def logout(request):
     return render_to_response('loginpage.html')
    
def sign_up(request):
    return render_to_response('signup.html')

@csrf_exempt
def change_password(request):
    return render_to_response('change_password.html')

@csrf_exempt
def changepwd(request):#  UPON CKLICK ON CREATEUSER SUBMIT BUTTON  USER DATA WILL GET SAVED IN DATABASE
        if request.POST.has_key('client_response'):
                Old_PWD = request.POST['client_responseoldpwd']
                New_PWD = request.POST['client_responsenewpwd']
                Cnfrm_PWD = request.POST['client_responsecnfpwd']
                Username = request.POST['client_response']

                print "Old_PWD",Old_PWD
                print "New_PWD",New_PWD
                print "Cnfrm_PWD",Cnfrm_PWD
                print "Username",Username
                flag_1=0
                if (New_PWD == Cnfrm_PWD):
                        print "After password validation"
                        dB=userinfo()
                        flag=dB.chanpwd(Old_PWD,New_PWD,Cnfrm_PWD,Username)
                        print 'flag',flag
                if flag==1:
                        flag_1=1
                elif flag==2:
                        flag_1=2
                elif flag==3:
                        flag_1=3
                response_dict = {}
                response_dict.update({'server_response': flag_1 ,'vale':val,'vale1':val1,'username':username1})
                
                return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
        else:
                return render_to_response('loginpage.html', context_instance=RequestContext(request))





#############################################################################################################################################
