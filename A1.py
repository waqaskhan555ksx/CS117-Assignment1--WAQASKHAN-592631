# A1: Fuse Check (Ohm's Law)
voltage=int(input("enter voltage in volts"))
resistance=int(input("enter resistance in ohms"))
if resistance>0:
    current=voltage/resistance
    if current>2:
        print("fuse will blow")
    else:
        print("circuit is safe")
else:
    print("invalid resistance")
