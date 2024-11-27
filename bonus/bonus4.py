# member  = input("Enter the new member: ") + "\n"
# file = open("hello.txt", "r")
# todos = file.readlines()
# file.close()

# todos.append(member)

# file2 = open("hello.txt","w")
# file2.writelines(todos)
# file2.close()




# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for item in filenames:
#     file = open(item, 'w')
#     file.write("hello")
#     file.close()




l = ['a.txt','b.txt','c.txt']
for i in l:
    file = open(f"{i}",'r')
    print(file.read())
    file.close()