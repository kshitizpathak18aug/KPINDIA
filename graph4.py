import  matplotlib.pyplot as plt
import  csv
dateOfx=[]
open_price_y1=[]
close_price_y2=[]

with open('E:\\Project\Data set\\apple.csv','r') as csvfile:
    plots =csv.reader(csvfile,delimiter=',')
    for column in plots:
        dateOfx.append(int(column[1]))
        open_price_y1.append(int(column[2]))
        close_price_y2.append(int(column[4]))

plt.plot(dateOfx,open_price_y1,close_price_y2 ,label='Loaded from file!')
plt.xlabel('Date')
plt.ylabel('Open')
plt.ylabel('Close')

plt.title('Share Market Price')
plt.legend()
plt.show()