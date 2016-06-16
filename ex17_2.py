from sys import argv
print(argv[0])
print(argv[1])
print(argv[2])
open(argv[2], 'w').write(open(argv[1]).read())

