def Knapsack(W,wt,val):
	array = []
	for i in range((len(val)+1)):
		temp = []
		for j in range(W+1):
			temp.append(0)

		array.append(temp)

	for i in range(1,len(val)+1):
		for j in range(1,W+1):
			if wt[i-1] > j:
				array[i][j] = array [i][j-1]

			else:
				array[i][j] = max( (val[i-1]+array[i-1][j-wt[i-1]]) , array[i-1][j] )


	print("Knapsack weight: ",array[len(val)][W])



W = 50
val = [60,100,120]
wt = [10,20,30]

Knapsack(W,wt,val)



