def simple_deco(fun1):
    def wrappe(*args,**kwargs):
        print(f"Function Starting {fun1.__name__}.....")
        result  = fun1(*args,**kwargs)
        print(f"Finished {fun1.__name__}.....")
        return result
    return wrappe
### decorator without  arguments
@simple_deco
def greet(name):
    print(f"Hello, {name}!!")
greet("Alice")