#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        templ1 = l1
        templ2 = l2
        while templ1 != None:
            num1+= str(templ1.val)
            templ1=templ1.next
            
        while templ2 != None:
            num2+= str(templ2.val)
            templ2=templ2.next
            
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        
        ans_str = str(num1 + num2)
        ans_list = list(reversed(ans_str))
        head = ListNode(int(ans_list[0]))
        temp = head
        for i in range(len(ans_list) - 1):
            i+=1
            temp.next=ListNode(int(ans_list[i]))
            temp = temp.next
        return head

solution=Solution()
l1 = ListNode(243)
l2 = ListNode(564)
node = solution.addTwoNumbers(l1,l2)
while node:
    print(node.val)
    node = node.next

    