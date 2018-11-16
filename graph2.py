import matplotlib.pyplot as plt
left=[1,2,3,4,5,6,7,8,9,10]
height=[5,10,30,40,50,30,60,20,90,100]
tick_label=['one','two','three','four','five','six','seven','eight','nine','ten']
plt.bar(left,height,tick_label=tick_label,width=0.8,color=['red','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('MY bar graph')
plt.show()