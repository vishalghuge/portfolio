from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.getBlogs, name='blogs'),
    path('<slug>', views.getBlog, name='post'),
    # path('blog', views.getBlog),
]