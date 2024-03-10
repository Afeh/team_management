from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q # For search functionality
from .models import TeamMember
from .forms import TeamMemberForm
from django.shortcuts import redirect

class TeamMemberListView(ListView):
	model = TeamMember
	template_name = 'team_member/list.html' # Set Template name
	paginate_by = 10 #paginate results

	def get_context_data(self, **kwargs):#Get base context data
		context =super().get_context_data(**kwargs)
		query = self.request.GET.get('q', '') #Get search query from URL parameter
		if query: #If a search query is present
			context['search_query'] = query  # Filter team members based on search query (case-insensitive)
			context['object_list'] = self.model.objects.filter(
				Q(first_name__icontains=query) | Q(last_name__icontains=query) |  Q(role__icontains=query)
			)
		return context #return updated context
	

class TeamMemberCreateView(CreateView):
	model = TeamMember
	form_class = TeamMemberForm
	template_name = 'team_member/add.html'
	success_url = reverse_lazy('team_member_list') # Redirection after successful creation

	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add Team Member' #Set Page Title
		return context
	
	def form_invalid(self, form):
		response = super().form_invalid(form) # Perform default invalid form handling
		#Uncomment for debugging
		#print(form.errors)#print errors
		#print(form.data)
		return response #Return response to user
	


class TeamMemberUpdateView(UpdateView):
	model = TeamMember
	form_class = TeamMemberForm
	template_name = 'team_member/edit.html'
	success_url = reverse_lazy('team_member_list')


class TeamMemberDeleteView(DeleteView):
	model = TeamMember
	template_name = 'team_member/teammember_confirm_delete.html'
	success_url = reverse_lazy('team_member_list')

	