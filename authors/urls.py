from django.urls import path
from authors.views import *

urlpatterns = [
    path('<int:author_id>', profile, name="author_profile"),
]
