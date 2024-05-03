from cal_f import   do_add, do_sub

def main():
    print ("welcome to my claculator")
    print(""" enter  option 
          "1" = add
          "2" = sub 
          
           """)
    option= input("select the fuction ")
    
    a = int(input("enter a number "))
    b = int(input("enter b "))
    
    
    if option  =="1":
        res = do_add(a,b)
        
    elif option =="2":
        res = do_sub(a,b)   
    
    print("result",res)
    
if __name__=="__main__":
    main()
            
        