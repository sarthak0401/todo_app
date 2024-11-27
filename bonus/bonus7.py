# A python program, to read the lines from a file and display the freq of each word

def count_freq():
    with open("files/extra.txt",'r') as file:
        data = file.readlines()
    d ={}
    for i in data:
        for k in i.split():
            k = k.lower().strip('.,!?;:"')
            # if k in d.keys():
            #     d[k] +=1
            # else:
            #     d[k] = 1
            d[k] = d.get(k,0) + 1
    return d

print(count_freq())