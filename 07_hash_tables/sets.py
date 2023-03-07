def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs


def has_unique_chars1(string):
    comp = list(set(string))
    cont = [char for char in string]
    comp.sort()
    cont.sort()
    if comp == cont:
        return True
    return False
    

def has_unique_chars2(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num -1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1 
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
            
    return longest_sequence
