#user chooses that he wants to calculate:
#mass (m),density (d), or volume(v)

flag = input("what do you want to calculate?. 1.mass 2. Density 3.Volume:")
# if mass is choosen you must ask for density and volume.
# calculate the mass by the formula.
if flag  == 'm':
    d = float(input("Density:"))
    v= float(input("Volume:"))
    result = d * v # mass.
     #if density is choosen you must ask for mass and volume is requested.
elif flag == 'd':
    m = float(input("Mass:"))
    v = float(input("volume:"))
    result = m/v # density
elif flag == 'v':
    m = float(input("Mass:"))
    d = float(input("Density"))
    result = m/d # volume
print("%.2f" % result)
