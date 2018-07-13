from django.db import models
from PCPartPicker_API import pcpartpicker

# Create your models here.

class CPU(models.Model):
    cpu_name = models.CharField(max_length = 200)
    cpu_price = models.CharField(max_length = 200)
    cpu_speed = models.CharField(max_length = 200, default = 'def val')
    def update(self):
        list = pcpartpicker.lists.get_list('cpu', 1) 
        for cpu in list:
            cpu_entry = CPU(cpu_name=cpu["name"],
                            cpu_price=cpu["price"],
                            cpu_speed=cpu["speed"])
                #cpu_ratings=cpu["ratings"],
                #cpu_cores=cpu["cores"])
            cpu_entry.save()

    def __str__(self):
       # self.update()
        return self.cpu_name
   
class MOBO(models.Model):
    mobo_name = models.CharField(max_length = 200)
    mobo_price = models.CharField(max_length = 200)
    mobo_ram = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('motherboard', 1)
        for motherboard in list:
            mobo_entry = MOBO(mobo_name=motherboard["name"],
                              mobo_price=motherboard["price"],
                              mobo_ram=motherboard["max-ram"])
            mobo_entry.save()

    def __str__(self):
        return self.mobo_name
            
class RAM(models.Model):
    ram_name = models.CharField(max_length = 200)
    ram_price = models.CharField(max_length = 200)
    ram_size = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('memory', 1)
        for memory in list:
            ram_entry = RAM(ram_name=memory["name"],
                            ram_price=memory["price"],
                            ram_size=memory["size"])
            ram_entry.save()

    def __str__(self):
        return self.ram_name

class GPU(models.Model):
    gpu_name = models.CharField(max_length = 200)
    gpu_price = models.CharField(max_length = 200)
    gpu_mem = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('video-card', 1)
        for videocard in list:
            gpu_entry = GPU(gpu_name=videocard["name"],
                            gpu_price=videocard["price"],
                            gpu_mem=videocard["memory"])
            gpu_entry.save()

    def __str__(self):
        return self.gpu_name

class HDD(models.Model):
    hdd_name = models.CharField(max_length = 200)
    hdd_price = models.CharField(max_length = 200)
    hdd_cap = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('internal-hard-drive', 1)
        for hdd in list:
            hdd_entry = HDD(hdd_name=hdd["name"],
                            hdd_price=hdd["price"],
                            hdd_cap=hdd["capacity"])
            hdd_entry.save()

    def __str__(self):
        return self.hdd_name


class PSU(models.Model):
    psu_name = models.CharField(max_length = 200)
    psu_price = models.CharField(max_length = 200)
    psu_watts = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('power-supply', 1)
        for powersupply in list:
            psu_entry = PSU(psu_name=powersupply["name"],
                            psu_price=powersupply["price"],
                            psu_watts=powersupply["watts"])
            psu_entry.save()

    def __str__(self):
        return self.psu_name

class TWR(models.Model):
    twr_name = models.CharField(max_length = 200)
    twr_price = models.CharField(max_length = 200)
    twr_type = models.CharField(max_length = 200)
    def update(self):
        list = pcpartpicker.lists.get_list('case', 1)
        for case in list:
            case_entry = TWR(twr_name=case["name"],
                            twr_price=case["price"],
                            twr_type=case["type"])
            case_entry.save()

    def __str__(self):
        return self.twr_name
