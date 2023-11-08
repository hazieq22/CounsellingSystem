from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("booking",views.booking,name="booking"),
    path("appointment",views.appointment,name="appointment"),
    path("home",views.home,name="home"),
    path("appointment2",views.appointment2,name="appointment2"),
    path('delete/<int:sessionID>', views.delete, name='delete'),
    path('update/<int:sessionID>/', views.update, name='update'),
    path('update/update_data/<int:sessionID>/', views.update_data, name='update_data'),
    path('update2/<int:sessionID>/', views.update2, name='update2'),
    path('update2/update_data2/<int:sessionID>/', views.update_data2, name='update_data2'),
]