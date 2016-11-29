#with open('MovieList.txt') as File:
#    Films = sum(1 for line in File if line.rstrip('\n'))
#
#print (Films)

File = open('MovieList.txt', 'r')
Film_Amounts=File.readlines()
print (Film_Amounts)

