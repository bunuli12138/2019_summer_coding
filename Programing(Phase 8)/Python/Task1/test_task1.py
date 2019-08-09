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
    # null linked list
    if head==None:
        return False
    # ergodic, 'val' not null mean never done
    while head.next and head.val!=None:
        head.val = None                     # set 'val' to null, it mean that this 'val' done
        head = head.next
    # no cicle
    if head.next==None:
        return False
    return True

def merge_linked_list(loll):
    print("***Task 6 'merge linked list' FAILED***")
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
    
    data, pos = [3,2,0,-4], 1
    head, node_lst = None, []
    t_4_head = None
    # initialize
    for v in data:
        node_lst.append(t1_linked_list(v))
    node_lst[-1].next = node_lst[pos]
    for i in range(len(node_lst)-1):
        node_lst[i].next = node_lst[i+1]
    t_4_head = node_lst[0]
    t_4_target = True
    t_4_result = cycle_lined_list(t_4_head)
    assert t_4_result==t_4_target, 'Result is not true'
    print('Task 4 is Right')
    
    
    total_l = [[1,4,5], [1, 3, 4], [2, 6]]
    t_5_lists = []
    for l in total_l:
        n_l = []
        for v in l:
            n_l.append(t1_linked_list(v))
        for i in range(len(n_l)-1):
            n_l[i].next = n_l[i+1]
        t_5_lists.append(n_l[0])
    t_5_result = merge_linked_list(t_5_lists)
    t_5_target_l = [1, 1, 2, 3, 4, 4, 5, 6]
    n_l = []
    for i in range(len(l)):
        assert t_5_result.val==t_5_target_l[i], '%d Result is not true'%i
        t_5_result = t_5_result.next
    print('Task 5 is Right')
