from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from .models import Pair
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

#
class RaspisanieView(LoginRequiredMixin, UserPassesTestMixin, View):
    
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return render(self.request, 'auth/login.html')

    def get(self, request):
        user = request.user
        group = user.study_group
        pairs = Pair.objects.filter(group=group)
        monday = Pair.objects.filter(day='1', group=group)
        tuesday = Pair.objects.filter(day='2', group=group)
        wednesday = Pair.objects.filter(day='3', group=group)
        thursday = Pair.objects.filter(day='4', group=group)
        friday = Pair.objects.filter(day='5', group=group)
        saturday = Pair.objects.filter(day='6', group=group)
        context = {'pairs': pairs,
                   'monday': monday,
                   'tuesday': tuesday,
                   'wednesday': wednesday,
                   'thursday': thursday,
                   'friday': friday,
                   'saturday': saturday,
                   }
        return render(request, 'raspisanie.html', context)
    
class GroupScheduleView(View):
    def get(self, request, group_number):
        # Retrieve the schedule for the selected group
        pairs = Pair.objects.filter(group=group_number)
        
        monday = pairs.filter(day='1')
        tuesday = pairs.filter(day='2')
        wednesday = pairs.filter(day='3')
        thursday = pairs.filter(day='4')
        friday = pairs.filter(day='5')
        saturday = pairs.filter(day='6')
        
        context = {
            'pairs': pairs,
            'monday': monday,
            'tuesday': tuesday,
            'wednesday': wednesday,
            'thursday': thursday,
            'friday': friday,
            'saturday': saturday,
        }
        return render(request, 'raspisanie.html', context)

class GroupsView(View):
    template_name = 'groups.html'

    def get(self, request):
        # Retrieve the list of unique groups
        group_list = Pair.objects.values_list('group', flat=True).distinct()

        # Get the search query from the request
        group_number = request.GET.get('group_number', '')

        # If a search query is provided, filter the groups
        if group_number:
            group_list = [group for group in group_list if group.startswith(group_number)]

        context = {
            'group_list': group_list,
            'search_query': group_number,  # Pass the search query for pre-filling the form
        }
        return render(request, self.template_name, context)
