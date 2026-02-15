from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("add/", views.add_job, name="add_job"),
    path("edit/<int:id>/", views.edit_job, name="edit_job"),
    path("delete/<int:id>/", views.delete_job, name="delete_job"),
]
