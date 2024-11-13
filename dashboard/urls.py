from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('menuitems',views.menuitems, name ='menuitems'),
    path('createmainmenu',views.mainmenu, name ='createmainmenu'),
    path('usermessages', views.usermessages, name='usermessages'),
    path('updatemenuitems/<title>',views.updatemenuitems,name='updatemenuitems'),
    path('deleteitems/<title>',views.deleteitems,name='deleteitems'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name='logout'),
   #ajout du nouveau path
   path('edit/menu/<int:id>/', views.update_menu, name='updatemenu'),
   path('delete/menu/<int:id>/', views.delete_menu, name='deletemenu'),

]


