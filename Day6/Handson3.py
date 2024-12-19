import time
def log_func_name_prints(fun1):
    def wrapper1(*args,**kwargs):
        print(f"\tStrating the fun1...{fun1.__name__}")
        result = fun1(*args,**kwargs)
        print(f"\tending...{fun1.__name__}")
        return result
    return wrapper1

def log_execution_time_print(fun1):
    def wrapper2(*args,**kwargs):
        begin = time.time()

       # print(f"Strating the fun1...{fun1.__name__}")
        print(f"\tStarting time: ",begin)
        result  = fun1(*args,**kwargs)
        time.sleep(5)
        end = time.time()
        print(f"\tennding time: ",end)
        print(f"\tTotal runtime of the program is {end - begin}")
       # print(f"ending...{fun1.__name__}")
        return result

    return wrapper2



#begin = time.time(fun1)
#time.sleep(1)
# end = time.time()




@log_execution_time_print #order is important:  1st runs then 2nd and then back to 1st
@log_func_name_prints
def fun1(argm1):

    print(f"\thi  : {argm1}")

fun1("Hello")