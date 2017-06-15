from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from teamapp import views

urlpatterns = [
    url(r'^team/$', views.TeamMemberList.as_view()),
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamMemberDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
