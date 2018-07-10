# Here go your api methods.
# Capped at 2 pages for now.
from PCPartPicker_API import pcpartpicker

def CPU_List():
    print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))
    print("CPU List")
    cpu_list = []
    totalPgs = pcpartpicker.lists.total_pages("cpu")
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("cpu", x)
        for cpu in info:
            part = dict(
                cpu_name = cpu["name"],
                cpu_price = cpu["price"],
                cpu_speed = cpu["speed"],
                cpu_ratings = cpu["ratings"],
                cpu_cores = cpu["cores"],
            )
            cpu_list.append(part)
            
    return response.json(dict(cpu_list=cpu_list,
    ))
            
        #print(info)
        
    #return response.json(dict(
    #    parts = parts,
    #))
#def insert_pc():
    #db.

def MOBO_List():
    print("Total MOBO pages:", pcpartpicker.lists.total_pages("motherboard"))
    print("MOBO List")
    totalPgs = pcpartpicker.lists.total_pages("motherboard")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("motherboard", x)
        for motherboard in info:
            part = dict(
                motherboard_name = motherboard["name"],
                motherboard_price = motherboard["price"],
                motherboard_ratings = motherboard["ratings"],
                motherboard_socket = motherboard["socket"],
                motherboard_ram = motherboard["max-ram"],
            )
            parts.append(part)
            print(part["motherboard_name"], " ", part["motherboard_price"]  + ' ' + part["motherboard_ratings"] + ' ' + part["motherboard_ram"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def RAM_List():
    print("Total RAM pages:", pcpartpicker.lists.total_pages("memory"))
    print("RAM List")
    totalPgs = pcpartpicker.lists.total_pages("memory")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("memory", x)
        for memory in info:
            part = dict(
                memory_name = memory["name"],
                memory_price = memory["price"],
                memory_speed = memory["speed"],
                memory_size = memory["size"],
                memory_price_gb = memory["price/gb"],
            )
            parts.append(part)
            print(part["memory_name"], " ", part["memory_price"] + ' ' + part["memory_speed"] + ' ' + part["memory_size"] + part["memory_price_gb"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def GPU_List():
    print("Total GPU pages:", pcpartpicker.lists.total_pages("video-card"))
    print("GPU List")
    totalPgs = pcpartpicker.lists.total_pages("video-card")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("video-card", x)
        for videocard in info:
            part = dict(
                GPU_name = videocard["name"],
                GPU_price = videocard["price"],
                GPU_memory = videocard["memory"],
                GPU_chipset = videocard["chipset"],
            )
            parts.append(part)
            print(part["GPU_name"], " ", part["GPU_price"] + ' ' + part["GPU_memory"] + ' ' + part["GPU_chipset"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def PSU_List():
    print("Total PSU pages:", pcpartpicker.lists.total_pages("power-supply"))
    print("PSU List")
    totalPgs = pcpartpicker.lists.total_pages("power-supply")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("power-supply", x)
        for powersupply in info:
            part = dict(
                powersupply_name = powersupply["name"],
                powersupply_price = powersupply["price"],
                powersupply_watts = powersupply["watts"],
                powersupply_series = powersupply["series"],
                powersupply_efficiency = powersupply["efficiency"]
            )
            parts.append(part)
            print(part["powersupply_name"], " ", part["powersupply_price"] + " " + part["powersupply_watts"] + " " + part["powersupply_efficiency"] + " " + part["powersupply_series"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def CASE_List():
    print("Total Case pages:", pcpartpicker.lists.total_pages("case"))
    print("Case List")
    totalPgs = pcpartpicker.lists.total_pages("case")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("case", x)
        for case in info:
            part = dict(
                case_name = case["name"],
                case_price = case["price"],
                case_type = case["type"],
            )
            parts.append(part)
            print(part["case_name"], " ", part["case_price"] + ' ' + part["case_type"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def HDD_List():
    print("Total HDD pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))
    print("HDD List")
    totalPgs = pcpartpicker.lists.total_pages("internal-hard-drive")
    parts = []
    for x in range(1, 2):
        info = pcpartpicker.lists.get_list("internal-hard-drive", x)
        for hdd in info:
            part = dict(
                hdd_name = hdd["name"],
                hdd_price = hdd["price"],
                hdd_capacity = hdd["capacity"],
                hdd_series = hdd["series"],
                hdd_type = hdd["type"],
                hdd_price_gb = hdd["price/gb"],
            )
            parts.append(part)
            print(part["hdd_name"], " ", part["hdd_price"] + " " + part["hdd_capacity"] + " " + part["hdd_series"] + " " + part["hdd_type"])
        #print(info)
    #return response.json(dict(
    #    parts = parts,
    #))
def main():
    CPU_List()
    MOBO_List()
    RAM_List()
    GPU_List()
    PSU_List()
    CASE_List()
    HDD_List()

main()
