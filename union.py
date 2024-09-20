def union(setA, setB):
   
    if len(setA) != len(list(setA)) or len(setB) != len(list(setB)):
        return []

    result = setA[:]
    for item in setB:
        if item not in result:
            result.append(item)
    return result
