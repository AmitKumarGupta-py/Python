def uniquealpha():

    txt = input("Enter a paragraph :  ")
    lis1 = []
    lis1 = txt.split()
    print(lis1)
    set1 = set(lis1)
    print(set1)
    lis2 = []
    lis2 = list(set1)
    print(lis2)
    lis3 = sorted(lis2)
    print(lis3)
uniquealpha()