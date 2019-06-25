from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing_page,name='home'),
    url('^edit/$',views.edit_profile,name="edit_profile"),
    url('^profile/(\d+)',views.profile, name="profile"),
]

