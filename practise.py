from django.template.defaultfilters import length

p="palle kishore"
result=""
for o in p:
    result=o+result
print(result)
#----------------------------------------------------------------------------#
f="reddy palle"
print(" ".join(f.split()[::-1]))

#------------------------------------------------------------------------------#
x="awesome"
def func():
    x="fantastic"
    return x
Hello=func()
print("value of x is",Hello)#----this will print fantastic
#print("value of x is",x)----this will print awesome

#-------------------------------------------------------------------------------#

l="kishore"
for i in range(len(l)-1, -1, -1):
    print(l[i],end="")
print()
#-----------------------------------------------------------------------------------#

x=2+4j
print(x.imag)
print(x.real)
#------------------------------------------------------------------------------------#

x=complex(2,-4)
print(x)
print(type(x))

#--------------------------------------------------------------------------------------#

