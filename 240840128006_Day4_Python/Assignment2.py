def dict2item():
    dict1 = {'Alice':85,'Bob':92,'Charlie':78,'David':65}
    dict2 = {x:y+5 for x,y in dict1.items() if y > 80 }
    print(dict2)
dict2item()
