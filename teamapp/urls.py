from django.urls import path
from . import views

#Define URL patterns for the TeamMember app
urlpatterns = [
    path("", views.TeamMemberListView.as_view(), name="team_member_list"),
    path("add/", views.TeamMemberCreateView.as_view(), name="team_member_add"),
	path("edit/<int:pk>/", views.TeamMemberUpdateView.as_view(), name="team_member_edit"),
	path("delete/<int:pk>/", views.TeamMemberDeleteView.as_view(), name="team_member_delete"),
]
