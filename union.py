def union(setA, setB):
   for i in range(len(setA)):
      if setA[i] in setA[:1]:
            return []
        
   for i in range(len(setB)):
      if setB[i] in setB[:i]:
            return []
           
   result = setA[:]
    
   for item in setB:
      if item not in result:
            result.append(item)

   return result
  
