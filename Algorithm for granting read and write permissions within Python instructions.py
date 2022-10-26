name = input("Enter the name of the file you want to create : ")
name_file= name+ "."+input("inter the extention of the file : ")
type_of_data = input("If you want to read, enter (r), and if you want to write, enter (w), and if you want to write and read, enter (rw) : ")
list = []
r_w_rw = ""
if type_of_data == "r" :
    x =  open(name_file,type_of_data)
    if x.readable():
        print(x.read())

elif type_of_data == "w":
    type_of_data = input("If you want to start writing the file from scratch, press (w). If you want to add text over the old text, press (a) : ")
    if type_of_data == "a":
        x = open(name_file,type_of_data)
        y = input("How many lines do you want to enter If it is one line enter (0) If it is several lines press (1) : "  )
        if y == str(0):
            x.write("\n")
            x.write(input("Enter the line you want to add to the old text : "))
        elif y == str(1):
           n =  int(input("enter the number of elment : "))
           for i in range(n):
            print("enter word " + str(i+1) + " :")
            ele = input()    
            list.append("\n" + ele)
            x.writelines(list)
            print(list)
    elif type_of_data == "w":
        x=open(name_file,type_of_data)
        y = input("how many lines you wnat to input you have lines and one line if one line enter (0) else enter (1) : "  )
        if y==str(0):
            x.write("\n")
            x.write(input("enter your new line to ad to old txet : "))
        elif y==str(1):
           n =  int(input("enter the number of elment : "))
           for i in range(n):
            print("enter word " + str(i+1) + " :")
            ele = input() 
            list.append("\n" + ele)
            x.writelines(list)
           print(list)
           
elif type_of_data == "rw" :
    x=open(name_file,type_of_data)

else:
    print("it must be somethink wrong")

