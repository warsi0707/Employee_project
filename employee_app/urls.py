from django.contrib import admin
from django.urls import path
from .import views
from .views import deleteView




urlpatterns =[
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),

# this url help to see and add the new data
    path("addempview", views.addempview, name="addempview"),
    path("addempview/add", views.ADD, name="add"),

# Edit
    path("editview", views.editview, name="editview"),
    path("editview/edit", views.edit, name="edit"),
    path("delete/", deleteView)

    
]

