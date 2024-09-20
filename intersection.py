def intersection (setA, setB)
    if setA is None or setB is None:
        return []
for i in range(len(setA))
    if setA[i] in setA[:1]
       return []
    
   
    for i in range(len(setB)):
        if setB[i] in setB[:i]:  
            return []
    
    result = []
    for item in setA:
        if item in setB and item not in result:  
            result.append(item)
    
    return result