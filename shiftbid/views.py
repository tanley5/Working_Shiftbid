from multiprocessing import context
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import Shiftbid
from .forms import ShiftbidCreateForm

# handle file upload import

class ShiftbidIndexView(ListView):
    template_name = 'shiftbid/index.html'
    model = Shiftbid

class ShiftbidCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {'form': ShiftbidCreateForm()}
        return render(request,'shiftbid/create.html', context=context)

    def post(self,request,*args,**kwargs):
        form = ShiftbidCreateForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            shiftbid_name = data['shiftbid_name']
            shiftbid = Shiftbid.objects.create(shiftbid_name=shiftbid_name)
            # handle file upload 
            
            shiftbid.save()
            return HttpResponseRedirect(reverse_lazy('shiftbid_index'))
        return render(request, 'shiftbid/create.html', {'form': form})
