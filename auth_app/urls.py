from django.urls import path
from auth_app.views import registerView, loginView, logoutView

urlpatterns = [
    path('reg/', registerView, name='register_urls'),
    path('log/', loginView, name='login_urls'),
    path('logout/', logoutView, name='logout_urls'),
]