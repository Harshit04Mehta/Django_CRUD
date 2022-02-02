from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.InsertPageView, name="Insertpage"),
    path("insert/", views.InsertData, name="Insert"),
    path("showpage/", views.ShowPage, name="Showpage"),
    path("editpage/<int:pk>", views.EditPage, name="Editpage"),
    path("update/<int:pk>", views.UpdateData, name="Update"),
    path("delete/<int:pk>", views.DeleteData, name="Delete"),
    path("", views.Add, name="Add"),
]