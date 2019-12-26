from django.urls import path
from intel import views
from intel.views import home,add,comme,pose

urlpatterns = [
	path('',views.home),
	path('add',views.add),
	path('comment',views.comme),
	path('pose',views.pose),
    
]
