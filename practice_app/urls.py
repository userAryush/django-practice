from django.urls import path,include
from practice_app.views import all_app

urlpatterns = [
    path('all/', all_app, name='all_home'),


]