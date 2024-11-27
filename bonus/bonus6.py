def get_avg():
    with open("files/data2.txt", 'r') as file:
        data = file.readlines()
    
    val = data[1:]
    val = [float(i) for i in val]

    avg = sum(val) / len(val)
    # print(val)
    # print(avg)

    return avg


avg_value = get_avg()
print(avg_value)

print(float('5\n '))