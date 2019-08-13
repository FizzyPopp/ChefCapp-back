from django.conf.urls import url

from .views import UserDetailView

urlpatterns = [
    url(r'^users/?$', UserDetailView.as_view(), name='user_api'),
]

