def decor1(fucn1):
    def wrapper1(*args,**kwargs):
        print(f"Strating the fucn1...{fucn1.__name__}")
        result = fucn1(*args,**kwargs)
        print(f"ending...{fucn1.__name__}")
        return result
    return wrapper1

@decor1
def fucn1(argm1):
    print(f"hi'''{argm1}")
fucn1("Hello")