pbook={}
for i in range(int(input())):
    line=input()
    key,value=line.split()
    pbook[key]=value

while True:
    try:
        name = input()
    except EOFError:
        break
    if name in pbook:
        print("{}={}".format(name,pbook[name]))
    else:
        print("Not found")
