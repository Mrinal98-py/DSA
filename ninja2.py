# Input: "abc"
# Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
# Explanation:
# Permutations of "abc" are "abc", "acb", "bac", "bca", "cab", and "cba"

str = "abc" 

def gen_pern(str):
    if len(str) == 1:
        return [str]
        
    output = []

    for i , char in enumerate(str):
        for perm in gen_pern(str[:i] + str[i+1:]):
            output.append(char + perm)
                
    return output
                
        
        
output = gen_pern(str)
print (output)