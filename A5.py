#A5.  Smallest and Largest Resistor
R1=int(input("enter value of R1"))
R2=int(input("enter value of R2"))
R3=int(input("enter value of R3 "))
if R1>R2 and R1>R3:
    greater="R1"
elif R2>R1 and R2>R3:
    greater="R2"
elif R3>R1 and R3>R2:
    greater="R3"
if R1<R2 and R1<R3:
    smallest="R1"
elif R2<R1 and R2<R3:
    smallest="R2"
elif R3<R1 and R3<R2:
    smallest="R3"
print("smallest  is ",smallest)
print("greatest is ",greater)
        
