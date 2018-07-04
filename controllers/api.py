# Here go your api methods.
# Capped at 5 pages for now, but that's still a lot. 
from PCPartPicker_API import pcpartpicker

def CPU_List():
    print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))
    totalPgs = pcpartpicker.lists.total_pages("cpu")
    for x in range(1, totalPgs):
        info = pcpartpicker.lists.get_list("cpu", x)
        print(info)

def MOBO_List():
    print("Total MOBO pages:", pcpartpicker.lists.total_pages("motherboard"))
    totalPgs = pcpartpicker.lists.total_pages("motherboard")
    for x in range(1, totalPgs):
        info = pcpartpicker.lists.get_list("motherboard", x)
        print(info)

def MEM_List():
    print("Total MEM pages:", pcpartpicker.lists.total_pages("memory"))
    totalPgs = pcpartpicker.lists.total_pages("memory")
    for x in range(1, 5):
        info = pcpartpicker.lists.get_list("memory", x)
        print(info) 
        
def GPU_List():
    print("Total GPU pages:", pcpartpicker.lists.total_pages("video-card"))
    totalPgs = pcpartpicker.lists.total_pages("video-card")
    for x in range(1, 5):
        info = pcpartpicker.lists.get_list("video-card", x)
        print(info)
    
def PSU_List():
    print("Total PSU pages:", pcpartpicker.lists.total_pages("power-supply"))
    totalPgs = pcpartpicker.lists.total_pages("power-supply")
    for x in range(1, 5):
        info = pcpartpicker.lists.get_list("power-supply", x)
        print(info)
