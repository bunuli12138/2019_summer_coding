# Sliding Window Maximum
def slid_win(nums, k):
    if not len(nums):
            return []
    return [max(nums[i-k:i]) for i in range(k, len(nums)+1)]

# Sqrt(x)
def sq(x):
    if x<2:
        return x
    n = x
    while n > x // n:
        print(n, '\t', x // n)
        n = (n + x // n) // 2
    return n

if __name__ == "__main__":
    t_1_nums, t_1_k = [1,3,-1,-3,5,3,6,7], 3
    t_1_target = [3,3,5,5,6,7]
    assert slid_win(t_1_nums, t_1_k)==t_1_target, 'slid_win is not true'
    # t_2_x = 2147395599
    # t_2_target = 46339
    t_2_x = 16
    t_2_target = 4
    assert sq(t_2_x)==t_2_target, 'sq is not true'
    print('ALL tests passed')
    pass