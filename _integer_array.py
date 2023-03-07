def find_pairs(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

# Example 
arr = [2, 4, 6, 8, 10]
target_sum = 12
result = find_pairs(arr, target_sum)
print(result)  
   