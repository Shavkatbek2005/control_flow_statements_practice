def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    
    return max(a,b,c)
print(find_max(2,3,6))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    if a>b and a>c:
        return 1
    if b>a and b>c:
        return 2
    if c>a and c>b:
        return 3
print(find_max_idx(2,3,8))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2