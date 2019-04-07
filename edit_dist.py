array = []

def diff(a,b):
	if a == b:
		return 0

	else:
		return 1

def minimum(a,b,c):
	if a<=b and a<=c:
		return a

	if b<=a and b<=c:
		return b

	else:
		return c

def edit_dist(str1,str2,i,j,array):
	if i <= 0 and j<=0:
		return 0

	if array[i][j]!=0:
		return array[i][j]

	array[i][j] = minimum( edit_dist(str1,str2,i-1,j-1,array)+diff(str1[i-1],str2[j-1]), edit_dist(str1,str2,i-1,j,array)+1, edit_dist(str1,str2,i,j-1,array)+1)
	return array[i][j]	
		

print(array)
str1 = "SUNNY"
str2 = "SNOWY"
array = [[ 0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
print(array)
for i in range(1,len(str1)+1):
	array[i][0] = i
for i in range(1,len(str2)+1):
	array[0][i] = i
print("min dist = ",edit_dist(str1,str2,len(str1),len(str2),array ) )