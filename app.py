from cal_f import   do_add, do_sub,do_div

#  multiply 
from mul import do_mul
from area import area_rec
def main():
    print ("welcome to my claculator")
    print(""" enter  option 
          "1" = add
          "2" = substraction 
          "3" = multiply 
          "4" = division
          
           """)
    option= input("select the fuction ")
    
    a = int(input("enter a number "))
    b = int(input("enter b "))
    
    
    if option  =="1":
        res = do_add(a,b)
        
    elif option =="2":
        res = do_sub(a,b)   
        
    elif option =="3":
        res = do_mul(a,b)   
    elif option =="4":
        res = do_div(a,b)
    
    print("result",res)

if __name__=="__main__":
    main()
            
        