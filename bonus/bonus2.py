filename = ["1.listitem..", "2.listitem..", "3.listitem.."]
# filename[0] = filename[0].replace(".","-",1)
# Replace keyword, and 1 for replacing the first occurance only, 2-> replacing two occurances

# Replace create a new string and then we are reassigning the var, modifying strings
for file in filename:
    file = file.replace(".","--",1)
    print(file)

