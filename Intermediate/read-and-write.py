fw = open('file.txt', 'w')

fw.write('''
    Bird is the word.
    Bird is not the word.
    Hello, My Name is Khan.
''')

fw.close()

fr = open('file.txt', 'r')
text = fr.read()
print(text)