# -*- coding: utf-8 -*-

'''Stack(1-3)'''
def validBrackets(s):
    lft_bra = ['[','(','{']
    stack_lst = []
    for c in s:
        # left bracket
        if c in lft_bra:
            stack_lst.append(c)
        # right bracket
        else:
            if c==')' and lft_bra[-1]!='(' or \
                    c == ']' and lft_bra[-1]!='[' or \
                        c == '}' and lft_bra[-1]!='{':
                    return False
            return True
        
        
def longestValBracket(s):
    longest_len = 0
    stack_lst = []
    for c in s:
        # left bracket
        if c=='(':
            stack_lst.append(c)
        # right bracket
        else:
            if len(stack_lst)==1:
                stack_lst.pop()
                longest_len += 2
            stack_lst = 0
    return longest_len


def reversePolish(l):
    num_stack, symbol_stack = [], []
    symbol = ['+','-','*','/']
    for v in l:
        # number
        if v not in symbol:
            num_stack.append(v)
    
            
if __name__ == '__main__':
    assert validBrackets('{}[()]'), 'validBrackets is not true'
    assert longestValBracket(')()())')==4, 'longestValBracket is not true'
    print('Task 1-2 is failed')
    t_3_tokens = ["2", "1", "+", "3", "*"]
    t_3_target = 9
    assert reversePolish(t_3_tokens)==t_3_target, 'reversePolish is not true'
    # print('ALL test is true')