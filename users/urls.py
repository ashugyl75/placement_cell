from django.urls import path
from . import views

urlpatterns = [
    path('', views.signInUp, name='signInUp'),
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('signOut', views.signOut, name='signOut'),

]
# urlpatterns = [
#     path('activate/<uidb64>/<token>', views.activate, name='activate'),
#
# ]