from django.urls import path,include
from.import views
from .views import customer_api_view
from .views import item_api_view


    



    


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('creditnote',views.creditnote,name='creditnote'),
    path('api/customers/<str:name>/', customer_api_view),
    path('api/items/<str:name>/', item_api_view),
    
    path('checkformgst',views.checkformgst,name='checkformgst'),
    path('mytemplate',views.mytemplate,name='mytemplate'),
    path('credit_note',views.credit_note,name='credit_note'),
    path('check',views.check,name='check'),
    path('notedetails',views.notedetails,name='notedetails'),

    

    
]