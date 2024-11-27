import glob

filepath = glob.glob("files/*.txt")

for i in filepath:
    with open(i, "r") as file:
        print(file.read().upper())
