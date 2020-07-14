from django.conf.urls import url

from . import views

urlpatterns = [
    #main page
    url(r'^$', views.index, name='index'),
    #sign up page
    url(r'^signup/$', views.signup, name='signup'),
    #add user
    url(r'^addUser/$', views.addUser, name='addUser'),
    #sign in page
    url(r'^signin/$', views.signin, name='signin'),
    #log in
    url(r'^login/$', views.login, name='login'),
    #edit page
    url(r'^edit/$', views.edit, name='edit'),
    #edit user 
    url(r'^editProfile/$', views.editProfile, name='editProfile'),
    #sports page
    url(r'^sports/$', views.sports, name='sports'),
    #business page
    url(r'^business/$', views.business, name='business'),
    #technology page
    url(r'^technology/$', views.technology, name='technology'),
    #science page
    url(r'^science/$', views.science, name='science'),
    #travel page
    url(r'^travel/$', views.travel, name='travel'),
    #adding a comment
    url(r'^addComment/$', views.addComment, name='addComment'),
    #logging out
    url(r'^logout/$', views.logout, name='logout'),
    # Ajax: check if user exists
    url(r'^logCheckUser/$', views.logCheckUser, name='logCheckUser'),
]
