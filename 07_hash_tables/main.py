from hash_table_constructor import HashTable


my_hash_table = HashTable()

my_hash_table.set_item("botls", 1400)
my_hash_table.set_item("washers",50)
my_hash_table.set_item("lumber", 70)



# o(n)
def items_in_common(list1: list, list2: list) -> bool:
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


# o(n^2)
def items_in_common2(list1: list, list2: list) -> bool:
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# Solution 1:
def find_duplicates1(nums) -> list:
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates


# Solution 2:
def find_duplicates2(nums) -> list:
    my_dict = {}
    dups = []
    for i in nums:
        if i not in my_dict:
            my_dict[i] = True
        else:
            dups.append(i)
    return [i for i in set(dups)]


def first_non_repeating_char(string: str) -> str:
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
        print(char_counts[char])
    
    for char in string:
        if char_counts[char] == 1:
            return char
            
    return None

def group_anagrams(strings: list) -> list:
    '''
    Parameters:
    strings: list: A list of strings to check.

    Checks a list of strings will return a list of lists
    grouping anagramable words.
    '''
    anagram_group = {}
    for word in strings:
        # Sort the word in alpha order
        canonical = ''.join(sorted(word))
        if canonical in anagram_group:
            # If the canonical exist, append a list of 
            # the word as a list to the dictionary
            anagram_group[canonical].append(word)
        else:
            # If the alpha is not a key, 
            # Create it and add the word as an item to
            # the dictionary
            anagram_group[canonical] = [word]
    return list(anagram_group.values())

def two_sum(nums, target):
    '''
    Parameters:
    nums: list of intergers.
    target: interger to compare.

    Returns the index position of the items in 
    the array that make up the target, else Returns
    empty list.
    '''
    num_map = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], idx]
        num_map[num] = idx
    return []


def subarray_sum(nums, target):
    sum_map = {0: -1}
    current_sum = 0
    for idx, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_map:
            return [sum_map[current_sum - target] + 1, idx]
        sum_map[current_sum] = idx
    return []
