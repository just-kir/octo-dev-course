import matplotlib.pyplot as plt

f = open("energy.txt", "r")
a = []

#######
l = f.readline()
l = (l[0:len(l)-1])
l = float(l)
a.append(l)
#######

f.close()  
print a