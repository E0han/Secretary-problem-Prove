#Math_IA testing
#__author__=="0han"
import random
import math
import pygal

fre_dis= pygal.Bar() 
e=math.e
initial=[]
N=input("Input N:")
for k in range(int(N)):
    initial.append(k+1)#create an array called initial includes int numbers from 1 to n
def run(n):
    results_distribution=[]
    for i in range(n):      
        random.shuffle(initial)
        M1=round(float(N)/e)
        M=initial[M1-1]#in python programming, the index of arry start from 0
        before_array=[]
        Max_before_P=None
        final_choose=None
        for j in range(M):
            before_array.append(initial[j])
        Max_before_M=max(before_array)#find the Max number in the range [1,M] 
        for b in range(M,len(initial)-1):#set a range from the position of M (which is M-1) to the end N
            if initial[b]>=Max_before_M:#if any number in the range[M-1,N] bigger than before, 
                final_choose=initial[b]#pick it, assign to final_choose var
            else:#if not, means 10 occurs before the position of M, choose the last one.
                final_choose=initial[len(initial)-1]
        results_distribution.append(final_choose)
    return results_distribution
def frequencies(x):
    results=[]
    for num in range(1, int(N)+1):
        result = x.count(num)
        results.append(result)
    return results
res=run(100000)#repeat 1000 times
frequencies = frequencies(res)
fre_dis.add('distribution', frequencies)  # add the frequencies
fre_dis.x_labels=map(str, range(1,int(N)+1))
fre_dis.x_title = 'Size number of diamonds'
fre_dis.y_title = 'Times for each size of diamond be chosen'
fre_dis.title = 'Frequency of running 10,0000 times for choosing diamond'
fre_dis.render_to_file('bar_chart.svg')
