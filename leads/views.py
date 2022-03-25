from audioop import reverse
from email import message
from django.core.mail import send_mail
import imp
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead,Agent
from django.views import generic
from .forms import LeadForm, LeadModelForm
# Create your views here.

def landing_page(request):
    return render(request, "landing.html")

def lead_list(request):
    leads =  Lead.objects.all()
    context= {
        "leads":leads
    }
    return render(request,"leads/lead_list.html",context)

# This function will give the detail of selected lead
def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context={
        "lead":lead
    }
    return render(request,"leads/leads_detail.html",context)


# this will create the Lead
class LeadCreateView(generic.CreateView):
    template_name="leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead_list")

    def form_valid(self,form):
        send_mail(
            subject="A lead has been Created",
            message="go check the lead",
            from_email="test@gmail.com",
            recipient_list=["test2@gmail.com "]
        )
        return super(LeadCreateView,self).form_valid(form)



def lead_create(request):
    form = LeadModelForm()
    if request.method=="POST":
        form =LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context={
        "form":form
    }
    return render(request,"leads/lead_create.html",context)


# this is to update single instance with modelForm
def lead_update(request,pk):

    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method=="POST":
        form =LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context={
        "lead":lead,
        "form":form
    }
    return render(request,"leads/lead_update.html",context)


def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# def lead_update(request,pk):

#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method =="POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()
#             return redirect("/leads")
#     context={
#         "form":form,
#         "lead":lead
#     }
#     return render(request,"leads/lead_update.html",context)
