from typing import Optional 

class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value

class Solution:
    def detectCycle(self, head: Optional[ListNode]):
        visited_dictionary = {}
        current_node = head
        
        while current_node:
            if visited_dictionary.get(current_node, False):
                return current_node
            visited_dictionary[current_node] = True
            current_node = current_node.next
            
        return None


node1 = ListNode('3')
node2 = ListNode('2')
node3 = ListNode('0')
node4 = ListNode('-4')

node1.next = node2
node2.next= node3
node3.next = node4
node4.next = node2

sol = Solution()
res = sol.detectCycle(node1)
if res:
    print('True')
else:
    print('False')
