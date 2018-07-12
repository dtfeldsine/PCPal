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

