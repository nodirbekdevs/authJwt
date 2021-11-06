from django.urls import path
from .views import *

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user'),
]
