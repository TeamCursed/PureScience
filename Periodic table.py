ce_number = int(input())
ce_name = "str"
atomic_mass = 0
ce_period = 0
ce_group = 0 
ce_subgroup = "str"

if ce_number == 1:
    ce_name = "Hydrogen"
    atomic_mass = 1.00797
    ce_period = 1
    ce_group = 1
    ce_subgroup = "A"
elif ce_number == 2:
    ce_name = "Helium"
    atomic_mass = 4.0026
    ce_period = 1
    ce_group = 18
    ce_subgroup = "A"

print('Theres some info about this Chemical element:\nNumber of the element: ',ce_number,'\nName: ',ce_name,'\nRelative atomic mass: ',atomic_mass,'\nPeriod: ',ce_period,'\nGroup: ',ce_group,'\nSubgroup: ',ce_subgroup)