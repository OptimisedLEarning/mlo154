def do_add(a:int,b:int):
    return a+b
# substraction
def  do_sub(a:int,b:int):
    return a-b 
def do_div(a,b):
    try:
        return a/b
    except ZeroDivisionError as r:
        return "cant divide by 0"