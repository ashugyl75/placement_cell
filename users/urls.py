from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),

]
# urlpatterns = [
#     path('activate/<uidb64>/<token>', views.activate, name='activate'),
#
# ]