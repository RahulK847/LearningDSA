arr = [10,10,29, 10,20,20]
di = {}
for i in arr:
    if i in di:
        di[i]+=1
    else:
        di[i] = 1
for key, val in di.items():
    print(f"{key} : {val}")
