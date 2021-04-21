from django.urls import path
from .import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('found/', views.found, name='found'),
    path('lost/', views.lost, name='lost'),
    path('sent_mail/<int:id>/', views.mail, name='mail'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('register', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('request/', views.requestItem, name='request_item'),
    path('lostitem/', views.lostItem, name='lostitem'),
    path('profile/edit', views.editprofile, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    path('claim/<int:id>/', views.claim, name='claim'),
    path('resolved_found/', views.resfound, name='resolvedfound'),
    path('resolved_lost/', views.reslost, name='resolvedlost'),
    path('contact/', views.contact, name='contact'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

]