# Here go your api methods.
# Capped at 2 pages for now.
from PCPartPicker_API import pcpartpicker

def CPU_List():
    print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))
    totalPgs = pcpartpicker.lists.total_pages("cpu")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("cpu", x)
        for cpu in info:
            print(cpu["name"], ":", cpu["price"])
        #print(info)

def MOBO_List():
    print("Total MOBO pages:", pcpartpicker.lists.total_pages("motherboard"))
    totalPgs = pcpartpicker.lists.total_pages("motherboard")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("motherboard", x)
        for motherboard in info:
            print(motherboard["name"], ":", motherboard["price"])
        #print(info)

def MEM_List():
    print("Total MEM pages:", pcpartpicker.lists.total_pages("memory"))
    totalPgs = pcpartpicker.lists.total_pages("memory")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("memory", x)
        for memory in info:
            print(memory["name"], ":", memory["price"])
        #print(info)

def GPU_List():
    print("Total GPU pages:", pcpartpicker.lists.total_pages("video-card"))
    totalPgs = pcpartpicker.lists.total_pages("video-card")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("video-card", x)
        #for video-card in info:
           # print(video-card["name"], ":", video-card["price"])
        #print(info)

def PSU_List():
    print("Total PSU pages:", pcpartpicker.lists.total_pages("power-supply"))
    totalPgs = pcpartpicker.lists.total_pages("power-supply")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("power-supply", x)
        #for power-supply in info:
        #    print(power-supply["name"], ":", power-supply["price"])
        #print(info)

def CASE_List():
    print("Total Case pages:", pcpartpicker.lists.total_pages("case"))
    totalPgs = pcpartpicker.lists.total_pages("case")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("case", x)
        for case in info:
            print(case["name"], ":", case["price"])
        #print(info)
def main():
    CPU_List()
    MOBO_List()
    MEM_List()
    GPU_List()
    CASE_List()

main()

