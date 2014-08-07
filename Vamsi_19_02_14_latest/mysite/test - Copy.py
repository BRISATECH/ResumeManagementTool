import sqlite3
conn = sqlite3.connect("sqlit3_LOCAL.db")
Mobile_Number="9986146542"

RequirementID="1"
Client="2"
name="3"
skills="4"
Yearsofexperience="5"
CURRENT_LOCATION="6"
lOCATION_OF_INTEREST="7"
CTC="8"
ECTC="9"
Notice_Period="10"

Email="12"
Source="13"
Date_of_birth="14"
PANCARD_NO="15"
dateOfSub="16"
Note="17"

##q= "SELECT Mobile_Number from Submit_resume where Mobile_Number = "+'"'+str(Mobile_Number)+'"'
#### RequirementID,Client,name,skills,Yearsofexperience,CURRENT_LOCATION,lOCATION_OF_INTEREST,CTC,ECTC,Notice_Period,Mobile_Number,Email,Source,Date_of_birth,PANCARD_NO,dateOfSub,Note
##q="UPDATE Submit_resume SET RequirementID="+'"'+str(RequirementID)+'"' +"where Mobile_Number = "+'"'+str(Mobile_Number)+'"'
##
##cursor=conn.execute(q)
##print cursor.fetchall()

conn = sqlite3.connect("sqlit3_LOCAL.db")
print "IN UpdateAll function data ::::::::",RequirementID
##cursor=conn.execute("UPDATE Submit_resume SET RequirementID="+'"'+str(RequirementID)+'"' WHERE Mobile_Number = "+'"'+str(Mobile_Number)+'"')
q = "UPDATE Submit_resume SET RequirementID = '" + str(RequirementID) + "' WHERE Mobile_Number = '"+ str(Mobile_Number) + "'"
print "q= ",q
cursor=conn.execute(q)
conn.commit()
print cursor.fetchall()
