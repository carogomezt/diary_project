from django.urls import path
from . import views

urlpatterns = [
    path("", views.entry_list, name="entry-list"),
    path("entry/<int:id>/", views.entry_detail, name="entry-detail"),
    path("entry/new/", views.entry_create, name="entry-create"),
    path("entry/<int:id>/update", views.entry_update, name="entry-update"),
    path("entry/<int:id>/delete", views.entry_delete, name="entry-delete"),
]
