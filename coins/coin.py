def makeChange(values,chgAmount, count, coinTypes):
	for i in range (chgAmount+1):
		coin = 1
		currentCount = i
		for j in [c for c in values if c <= i]:
	 		if (count[i-j] + 1) < currentCount:
				currentCount = count[i-j]+1
				coin = j
			count[i] = currentCount
			coinTypes[i] = coin
	return count[chgAmount]


#main

