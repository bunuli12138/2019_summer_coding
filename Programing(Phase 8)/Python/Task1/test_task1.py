# -*- coding: utf-8 -*-
'''completely find out THREE num that sum up is 0'''
def three_sum(nums):
    res = []
    # Sorted
    nums.sort()
    
    # Check param for stack pop
    if len(nums)==0 or nums[0]>0 or nums[-1]<0:
        return res
    
    
    for k in range(len(nums)):
        if nums[k]>0: 
            break
        if k>0 and nums[k]==nums[k-1]:                  # Repetitive elements are skipped
            continue
        target = 0 - nums[k]                            # Target value of the latter two parameters
        # Binary search
        i = k+1                                         # The forward one of the latter two parameters
        j = len(nums)-1                                 # The latter one of the latter two parameters
        while i < j:
            if nums[i]+nums[j]==target:
                res.append([nums[k], nums[i], nums[j]])
                while i<j and nums[i+1]==nums[i]:            # Repetitive elements are skipped
                    i+=1
                while i<j and nums[j-1]==nums[j]:            # DITTO
                    j-=1
                
                i += 1                                       # Increase naturally
                j -= 1                                       # DITTO
            
            elif nums[i] + nums[j] < target:           # Increase 1 at small end
                i+=1
            else:                                      # Increase 1 at large end
                j-=1
    return res        


'''Majority Element(occurence num more than 50%)'''
def majority_element(nums):
    hash_d = {}
    for num in nums:
        hash_d[num] = hash_d.get(num, 0)
        hash_d[num] += 1
    return sorted(hash_d.items(), key=lambda it:it[1])[-1][0]


def cycle_lined_list(head):
    pass

from array_linked_list import t1_linked_list
if __name__ == '__main__':
    t_1_nums = [-1, 0, 1, 2, -1, -4]
    t_1_target = [[-1, 0, 1],[-1, -1, 2]]
    t_1_result = three_sum(t_1_nums)
    assert len(t_1_result)==len(t_1_target), 'Result has different counts'
    assert sorted(t_1_result)==sorted(t_1_target), 'Result is not true'
    print('Task 1 is Right')
    
    
    t_2_nums = [2,2,1,1,1,2,2]
    t_2_target = 2
    t_2_result = majority_element(t_2_nums)
    assert t_2_result==t_2_target, 'Result is not true'
    print('Task 2 is Right')
    
    data, pos = [3,2,0,-4], 2
    t_3_head = None
    for v in data:
        t_3_head.next = t1_linked_list
    t_3_target = True
    t_3_result = cycle_lined_list(t_3_head, t_3_pos)
    