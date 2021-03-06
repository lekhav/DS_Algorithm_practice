# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 1 STACK SOLUTION
    # O[2N] time; O[N] space
    def reverseList(self, head):
        if not head:
            return None
        
        st = []
        result = dummy = ListNode(-1)
        while head != None:
            st.append(head.val)
            head = head.next
        
        while st != []:
            dummy.next = ListNode(st.pop())
            dummy = dummy.next
        return result.next

    # ITERATIVE 3 POINTER APPROACH 
    # O(N) time ; O(1) space
    def reverseList(self, head):
        if not head:
            return 
            
        slow = None    
        current = head
        fast = head.next
        
        while current.next != None:
            current.next = slow
            slow = current
            current = fast
            fast = fast.next
        current.next = slow
        return current
        
    
    # RECURSIVE APPROACH
    # O(N) time ; O(1) extra space O(N) recursive callstack 
    def reverseList2(self, head):
        if head == None:
            return
        return self.reverseLL(head)
    
    def reverseLL(self, head):
        # BASE CASE
        if head.next == None:
            return head
        
        # LOGIC
        r = self.reverseLL(head.next)     # recursively for for every node r is created 
        head.next.next = head             # create the new reversed LINK
        head.next = None                  # BREAK the previous next LINK
        return r
        
        
        
