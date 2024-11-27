contents = ['hello this is string 1', 'hello this is string 2', 'hello this is string 3']
filenames = ['docs1.txt', 'docs2.txt', 'docs3.txt']

for content, file in zip(contents, filenames):
    f = open(f"files/{file}",'w')
    f.write(content)
    f.close()
