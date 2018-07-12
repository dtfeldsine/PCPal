from django.contrib import admin
from PCPartPicker_API import pcpartpicker

# Register your models here.

from django.contrib import admin
from .models import CPU
from .models import MOBO
from .models import RAM
from .models import GPU
from .models import HDD

class cpu_admin(admin.ModelAdmin):
    def cpu_list(self):
        html = ""
        list = pcpartpicker.lists.get_list('cpu', 1)
        for cpu in list:
            html += '%s, '%cpu["name"]
            html += '%s, '%cpu["price"]
            html += '%s, '%cpu["speed"]
            html += '\n' 
        return html
#    list_display = ['cpu_name', cpu_list] 
    list_display = ['cpu_name', 'cpu_price', 'cpu_speed'] 
admin.site.register(CPU, cpu_admin)

class mobo_admin(admin.ModelAdmin):
    def mobo_list(self):
        html = ""
        list = pcpartpicker.lists.get_list('motherboard', 1)
        for motherboard in list:
            html += '%s, '%motherboard["name"]
            html += '%s, '%motherboard["price"]
            html += '%s, '%motherboard["max-ram"]
            html += '\n'
        return html
    list_display = ['mobo_name', 'mobo_price', 'mobo_ram']
admin.site.register(MOBO, mobo_admin)
 
class ram_admin(admin.ModelAdmin):
    def ram_list(self):
        html = ""
        list = pcpartpicker.lists.get_list('memory', 1)
        for memory in list:
            html += '%s, '%memory["name"]
            html += '%s, '%memory["price"]
            html += '%s, '%memory["size"]
            html += '\n'
        return html
    list_display = ['ram_name', 'ram_price', 'ram_size']
admin.site.register(RAM, ram_admin)

class gpu_admin(admin.ModelAdmin):
    def gpu_list(self):
        html = ""
        list = pcpartpicker.lists.get_list('video-card', 1)
        for videocard in list:
            html += '%s, '%videocard["name"]
            html += '%s, '%videocard["price"]
            html += '%s, '%videocard["memory"]
            html += '\n'
        return html
    list_display = ['gpu_name', 'gpu_price', 'gpu_mem']
admin.site.register(GPU, gpu_admin)

class hdd_admin(admin.ModelAdmin):
    def hdd_list(self):
        html = ""
        list = pcpartpicker.lists.get_list('internal-hard-drive', 1)
        for hdd in list:
            html += '%s, '%hdd["name"]
            html += '%s, '%hdd["price"]
            html += '%s, '%hdd["capacity"]
            html += '\n'
        return html
    list_display = ['hdd_name', 'hdd_price', 'hdd_cap']
admin.site.register(HDD, hdd_admin)



