def fillheight(input, i , height): 
	
	
	if height[i] != 0: 
		return
	
	
	if input[i] == -1: 
		height[i] = 1
		return

	 
	if height[input[i]] == 0: 
		fillheight(input, input[i] , height) 

	
	height[i] = height[input[i]] + 1

 
def findNodes(input): 
	n = len(input) 
	 
	height = [0 for i in range(n)] 

	
	for i in range(n): 
		fillheight(input, i, height) 

	 
	ht = height[0] 
	for i in range(1,n): 
		ht = max(ht, height[i]) 

	return ht 


input = [-1 , 0, 4, 0, 3] 
print(findNodes(input))

