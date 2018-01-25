Change(d, k, n)
C[0] ← 0
for p ← 1 to n
	min ← ∞
	for i ← 1 to k
		if d[i] ≤ p then
			if 1 + C[p − d[i]] < min then
			min ← 1 + C[p − d[i]]
 			coin ← i
 			C[p] ← min
			S[p] ← coin
 return C and S
