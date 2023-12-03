class ListNode:

    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution():

    def addTwoNumbers(l1,l2):
        
        def single_digit_sum(v1,v2,previous_carry):
            curr_sum = v1 + v2 + previous_carry
            carry = 0

            if curr_sum > 9:
                curr_sum-=10
                carry = 1
            
            return curr_sum,carry
        
        def sumNodes_recursive(l1,l2,carryover=0):
            
            sum_val,carry = single_digit_sum(l1.val,l2.val,previous_carry=carryover)
            curr_node = ListNode(sum_val)

            if not (l1.next or l2.next):
                if carry:
                    curr_node.next = ListNode(carry)
                return curr_node
            
            l1.next = ListNode(0) if not l1.next else l1.next
            l2.next = ListNode(0) if not l2.next else l2.next
            curr_node.next = sumNodes_recursive(l1.next,l2.next,carryover=carry)

            return curr_node
        
        def sumNodes_iterative(l1,l2):
            
            curr_1,curr_2 = l1,l2
            prev_carry = 0
            head = None
            curr_node = None

            while True:
                
                curr_sum,prev_carry = single_digit_sum(curr_1.val,curr_2.val,previous_carry=prev_carry)
                if curr_node:
                    curr_node.next = ListNode(curr_sum)
                    curr_node = curr_node.next
                if not head:
                    head = ListNode(curr_sum)
                    curr_node = head

                end_of_list = not (curr_1.next or curr_2.next)
                if end_of_list:
                    if prev_carry:
                        curr_node.next = ListNode(prev_carry)
                    break
                
                curr_1.next = ListNode(0) if not curr_1.next else curr_1.next
                curr_2.next = ListNode(0) if not curr_2.next else curr_2.next

                curr_1 = curr_1.next
                curr_2 = curr_2.next

            return head


            
        return sumNodes_iterative(l1,l2)#sumNodes_recursive(l1,l2)
         
    
def lst_2_lnkd(obj):
    head = ListNode(obj[0])
    curr_obj = head
    for i in range(1,len(obj)):
        curr_obj.next = ListNode(obj[i])
        curr_obj = curr_obj.next

    return head

def iter_lnkd(head):

    print(head.val,end='')
    if not head.next:
        return
    return iter_lnkd(head.next)

l1_list = [9,9,9,9,9,9,9]#[2,4,3]
l1 = lst_2_lnkd(l1_list)

l2_list = [9,9,9,9]#[5,6,4]
l2 = lst_2_lnkd(l2_list)

test = getattr(Solution,'addTwoNumbers')

result = test(l1,l2)

iter_lnkd(result)
