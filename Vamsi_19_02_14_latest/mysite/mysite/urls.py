from django.conf.urls import patterns, include, url
from polls.views import *
from django.contrib import admin
from django.conf import settings
#admin.autodiscover()
from polls.views import back

urlpatterns = patterns('',
###########Lavita############################################################
                       url(r'^$',method),

			 url(r'^help1/',help1),
			url(r'^autogen/$',autoskills),
                       url(r'^autogen1/$',autoyearexp1),
                       url(r'^autogen2/$',autombno),
                       #url(r'^$', firstPage),
                       url(r'^passwordkey1/$',changep),
                       url(r'^passwordkey/$',changepassword),
                       url(r'^signup/$',signup),
                       url(r'^logintask/$',loginpage), 
                       url(r'^signupdata/$',signupdata),
                       url(r'^ReportManagementfile/$',ReportManagementfile),
###########################Lavita#############################################
                       url(r'^submt/$', submt),
                       url(r'^query/$', query),
                       url(r'^sub/$', firstPage),
                       url(r'^resunsub/$', resunsub),
                       url(r'^submtResume/$', submtResume),
                       url(r'^submtRrequire/$', submtRrequire),
                       url(r'^requiresub/$', requiresub),
                       url(r'^searchResult/$', searchResult),
                       url(r'^searchResult1/$', searchResult1),
                       url(r'^searchResume/$', searchResume),
                       url(r'^searchRequirements/$', searchRequirements),
                       url(r'^download/(?P<file_name>.+)$', download),
                       url(r'^editMyTask/$',editMyTask),
                       url(r'^editMyRequirement/$',editMyRequirement),
                       url(r'^saveEditResume/$',saveEditResume),
                       url(r'^saveEditRequirement/$',saveEditRequirement),
                        url(r'^saveEditRequirement1/$',saveEditRequirement1),
                       url(r'^Export_to/$',Export_to),
                       url(r'^openstateresume/$',openstateresume),
                       url(r'^searchRequirements1/$',searchRequirements1),
                       url(r'^editMyRequirement1/$',editMyRequirement1),
                       url(r'^RequirementManagement/$',RequirementManagement),

                       url(r'^output/$',selectclient),
                       url(r'^output1/$',selectclient1),
                       url(r'^output2/$',selectclient2),
		       url(r'^display_report',display_report),
                       
                       url(r'^back/$', back),
 ##############################################################Arpitha##################################################################################
                       url(r'^login/$', login),
                       url(r'^Login_View/$', Login_View),
                       url(r'^logout/$', logout),
                      # url(r'^sign_up/$', sign_up),
                       url(r'^change_password/$', change_password),
                       url(r'^changepwd/$', changepwd),
                        ##########################################################################              
    # Examples:
#     url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #===========================================================================
    # url(r'^$', LoginPage),
    # url(r'^login_page/$', login_view),
    # url(r'^myclick/$',myclick ),
    # url(r'^signup/$',signup),
    # url(r'^submit/$',submit),
    # url(r'^taskAsin/$',taskAsin),
    # url(r'^myTask/$',myTask),
    # url(r'^taskAsinSave/$',taskAsinSave),
    # url(r'^taskEditSave/$',taskEditSave),
    # url(r'^editMyTask/$',editMyTask),
    # url(r'^search/$',search),
    # url(r'^Search_new/$',Search_new),
    # url(r'^NEWFORFILE/$',NEWFORFILE),
    # url(r'^AccountSetting/$',AccountSetting),
    # url(r'^saveEditedPersonalDetail/$',saveEditedPersonalDetail),
    # url(r'^saveEditEmailSetting/$',saveEditEmailSetting),
    # url(r'^ValidateEmail/$',ValidateEmail),
    #===========================================================================
)
#urlpatterns.append(url(r'^editMyTask'+'/$',editMyTask))
# conn = sqlite3.connect("database_for_time_manager_tool.sqlite3")
