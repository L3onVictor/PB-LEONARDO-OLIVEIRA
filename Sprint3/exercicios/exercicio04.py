for i in range(1,101):
    if i <= 1:
        continue
    primo = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            primo = False
    if primo:
        print(i)
        

