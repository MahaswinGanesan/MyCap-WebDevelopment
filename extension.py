ext=["py","c","cpp","txt"]
x=input("Enter the filename:")
t=x.split(".")
if t[-1]==ext[0]:
    print("Python")
elif t[-1]==ext[1]:
    print("C")
elif t[-1]==ext[2]:
    print("C++")
elif t[-1]==ext[3]:
    print("Text")
