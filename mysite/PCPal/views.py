from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

from .models import CPU
# Create your views here.

def cpu_index(request):
    latest_cpu_list = CPU.objects.order_by('-cpu_name')[:100]
    template = loader.get_template('PCPal/index.html')
    context = {
        'latest_cpu_list': latest_cpu_list,
    }
    return HttpResponse(template.render(context, request))
    
def gpu_index(request):
    latest_gpu_list = GPU.objects.order_by('-gpu_name')[:100]
    template = loader.get_template('PCPal/index.html')
    context = {
        'latest_gpu_list': latest_gpu_list,
    }
    return HttpResponse(template.render(context, request))
    
def ram_index(request):
    latest_ram_list = RAM.objects.order_by('-ram_name')[:100]
    template = loader.get_template('PCPal/index.html')
    context = {
        'latest_ram_list': latest_ram_list,
    }
    return HttpResponse(template.render(context, request))
    
def mobo_index(request):
    latest_mobo_list = MOBO.objects.order_by('-mobo_name')[:100]
    template = loader.get_template('PCPal/index.html')
    context = {
        'latest_mobo_list': latest_mobo_list,
    }
    return HttpResponse(template.render(context, request))
    
def hdd_index(request):
    latest_hdd_list = HDD.objects.order_by('-hdd_name')[:100]
    template = loader.get_template('PCPal/index.html')
    context = {
        'latest_hdd_list': latest_hdd_list,
    }
    return HttpResponse(template.render(context, request))

