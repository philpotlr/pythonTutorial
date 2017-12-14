# open a file
fo = open('test.txt', 'w')


# Get some info
print('name: ', fo.name)
print('is closed: ', fo.closed)
print('opening mode: ', fo.mode)
#write to file
fo.write('I love python')
fo.write(' and JavaScript')
#close file
fo.close()


# open to append
fo = open('test.txt', 'a')
fo.write('I also like PHP')
fo.close()

# read from file 
fo = open('test.txt', 'r+')
text = fo.read()
print(text)
fo.close()


# create a file
fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close()