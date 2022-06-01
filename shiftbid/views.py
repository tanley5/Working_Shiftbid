from multiprocessing import context
from typing import List
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View
from django.shortcuts import render

from .models import Shiftbid, Seniority,Shift
from .forms import ShiftbidCreateForm, ShiftbidResponseForm

# handle file upload import
from utils.shiftbid.filehandlers import handleSeniorityFile, handleShiftFile
from utils.shiftbid.responsehandler import handle_response_submission

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
            shiftbid.save()
            # handle file upload 
            handleShiftFile(shiftBid=shiftbid,file=request.FILES['shift_file'])
            handleSeniorityFile(shiftBid=shiftbid, file=request.FILES['seniority_file'])
            
            return HttpResponseRedirect(reverse_lazy('shiftbid_index'))
        return render(request, 'shiftbid/create.html', {'form': form})

class ShiftbidDeleteView(DeleteView):
    model = Shiftbid
    success_url = reverse_lazy('shiftbid_index')

class ShiftbidDisplayView(View):
    model1 = Shiftbid
    model2 = Seniority
    model3 = Shift
    
    def get(self,request,*args,**kwargs):
        sb = self.model1.objects.get(pk = kwargs['pk'])
        shifts = self.model3.objects.filter(shiftbid = sb)
        seniorities = self.model2.objects.filter(shiftbid = sb)
        context = {
            "shifts": shifts,
            "seniorities": seniorities
        }
        return render(request,'shiftbid/shiftbid_display.html',context=context)

class ShiftbidChangeStateView(UpdateView):
    model = Shiftbid
    fields = ["shift_status"]
    success_url = reverse_lazy('shiftbid_index')
    template_name = 'shiftbid/shiftbid_change.html'

class ShiftbidResponseFormView(View):
    template_name = 'shiftbid/response_collection.html'

    def get(self, request, *args, **kwargs):
        sb_pk = self.kwargs["pk"]
        form = ShiftbidResponseForm(pk=sb_pk)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        sb_pk = self.kwargs["pk"]
        print(sb_pk)
        form = ShiftbidResponseForm(data=request.POST,
                            pk=sb_pk)
        context = {'form': form}
        
        if form.is_valid():
            shift_chosen = form.cleaned_data["Shiftbid"][0].pk
            email = form.cleaned_data["agent_email"]
            handle_response_submission(shift_chosen, email, sb_pk)
            form = ShiftbidResponseForm(pk=sb_pk)
            return render(request, 'shiftbid/response_thanks.html', context)
        return render(request, self.template_name, context)