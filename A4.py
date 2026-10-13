#A4.  Logic Gates
A=int(input("enter 0 or 1 "))
B=int(input("enter 0 or 1 "))

if A==0 and B==0:
    XOR=0
    AND=0
    OR=0
   
elif A==1 and B==0:
    XOR=1
    AND=0
    OR=1
    
elif A==0 and B==1:
    XOR=1
    AND=0
   
elif A==1 and B==1:
    XOR=0
    AND=1
    OR=1
   
else:
    print("bits must be 0 or 1")
print("xor is :", XOR, "AND is :", AND,"OR is :",OR)
