import django
django.setup()

from PCPal.models import MOBO
from PCPal.models import CPU
from PCPal.models import RAM
from PCPal.models import GPU
from PCPal.models import HDD
from PCPal.models import PSU
from PCPal.models import TWR

CPU.objects.all().delete()   
MOBO.objects.all().delete()
RAM.objects.all().delete()
GPU.objects.all().delete()
HDD.objects.all().delete()
PSU.objects.all().delete()
TWR.objects.all().delete()

cpu = CPU(cpu_name="default_cpu")
mobo = MOBO(mobo_name="default_mobo")
ram = RAM(ram_name="default_ram")
gpu = GPU(gpu_name="default_gpu")
hdd = HDD(hdd_name="default_hdd")
psu = PSU(psu_name="default_psu")
twr = TWR(twr_name="default_twr")

cpu.update()
mobo.update()
ram.update()
gpu.update()
hdd.update()
psu.update()
twr.update()
