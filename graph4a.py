import matplotlib.pyplot as plt
import csv

x=[]
y=[]
z=[]

with open('excel.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))


plt.plot(x,y, marker='o')
plt.plot(x,z,marker='o')

plt.title('random value')

plt.xlabel('x')
plt.ylabel('y')

plt.show()

