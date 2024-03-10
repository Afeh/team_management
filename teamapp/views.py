from django.forms.forms import BaseForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Profile, Role, User
from .forms import TeamMemberForm
from django.shortcuts import redirect


class TeamMemberListView(ListView):
    model = User
    template_name = 'team_member/list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        qset = self.model.objects.all().order_by(
            'first_name').prefetch_related('profile', 'profile__role')
        if query:
            qset = qset.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
                    profile__role__role__icontains=query) | Q(email__icontains=query)
            )
        return qset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', None)
        return context


class TeamMemberCreateView(FormView):
    form_class = TeamMemberForm
    template_name = 'team_member/add.html'
    success_url = reverse_lazy('team_member_list')
    initial = {
        'first_name': '',
        'last_name': '',
        'email': '',
        'phone_number': '',
        'role': '',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        context['title'] = 'Add Team Member'
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class TeamMemberUpdateView(FormView):
    form_class = TeamMemberForm
    template_name = 'team_member/edit.html'
    success_url = reverse_lazy('team_member_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance = User.objects.get(id=self.kwargs.get('pk'))
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        return context

    def get_initial(self):
        initial = super().get_initial()
        instance = User.objects.get(id=self.kwargs.get('pk'))
        initial = {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'email': instance.email,
            'phone_number': instance.profile.phone_number,
            'role': instance.profile.role.id,
        }
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class TeamMemberDeleteView(DeleteView):
    model = User
    template_name = 'team_member/teammember_confirm_delete.html'
    success_url = reverse_lazy('team_member_list')
