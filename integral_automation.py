from math import *

low_lim=int(input("Enter lower limit : "))
up_lim=int(input("Enter upper limit : "))

x_vals=[]
for i in range(low_lim,up_lim+1):
	x_vals.append(i)
	
print(f"x : {x_vals}\n")


y_vals=list(map(lambda x:(log10(pow(x,2)))/(sqrt(cosh(x))),x_vals))
print(f"y : {y_vals}\n")

ends=y_vals[0::len(y_vals)-1]
#print(f"Ends are {ends}")

evens=[]
for i in range(1,len(y_vals)-1):
	if i%2==0:
		evens.append(y_vals[i])
	
#print(f"Evens are {evens}")

odds=[]
for i in range(1,len(y_vals)-1):
		if i%2!=0:
			odds.append(y_vals[i])
			
#print(f"Odds are {odds}")

h= (up_lim-low_lim)/(len(x_vals)-1)
#print(f"Step length, h = {h}")

sum_of_ends = 0 
for i in range(len(ends)):
	sum_of_ends+=ends[i]
#print(f"Sum of ends is : {sum_of_ends}")


sum_of_evens = 0 
for i in range(len(evens)):
	sum_of_evens+=evens[i]
#print(f"Sum of evens is : {sum_of_evens}")


sum_of_odds = 0 
for i in range(len(odds)):
	sum_of_odds+=odds[i]
#print(f"Sum of odds is : {sum_of_odds}")

integral=(h/3)*(sum_of_ends + 2*(sum_of_evens) + 4*(sum_of_odds))

print(f"Integral is : {integral}")



