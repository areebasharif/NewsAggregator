from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    login,
    feedback,
    home,
    bbc,
    cnn,
    newscategory,
    espn,
    register,
    logout_view,
)

urlpatterns = [
    path("", login, name="login"),
    path("home", home, name="home"),
    path("bbc", bbc, name="BBC"),
    path("cnn", cnn, name="CNN"),
    path("newscategory", newscategory, name="newscategory"),
    path("feedback", feedback, name="feedback"),
    path("espn", espn, name="ESPN"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout_view, name="logout_view"),
     path('reset-password/', auth_views.PasswordResetView.as_view(template_name="reset-password.html"), name="reset_password"),
    path('reset-link-sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset-sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset-form.html"), name="password_reset_confirm"),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset-done.html"), name="password_reset_complete"),
]
