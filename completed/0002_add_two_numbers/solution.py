from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# with this solution we are reusing existing list to store values
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = l1
        head = l

        v = 0
        while True:
            if l1 is not None:
                v += l1.val
                l1 = l1.next

            if l2 is not None:
                v += l2.val
                l2 = l2.next

            l.val = v % 10
            v = v // 10
            
            if l1 is None:
                if l2 is None:
                    if v > 0:
                        l.next = ListNode(v)

                    break
                else:
                    l.next = l2
                    l = l.next
            
            else:
                l.next = l1
                l = l.next
        
        return head


# this is a simple naive solution where we have to allocate extra memory for the new elements
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l = ListNode()
#         h = l

#         v = 0
#         while True:
#             if l1 is not None:
#                 v += l1.val
#                 l1 = l1.next

#             if l2 is not None:
#                 v += l2.val
#                 l2 = l2.next

#             l.val = v % 10
#             v = v // 10
            
#             if l1 is None and l2 is None:
#                 if v > 0:
#                     l.next = ListNode(v)

#                 break

#             l.next = ListNode()
#             l = l.next
        
#         return h
    
def create_list_node(l: list) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    list_node = ListNode(l[0])
    head = list_node

    i = 1
    while i < len(l):
        head.next = ListNode(l[i])
        head = head.next
        i += 1

    return list_node

def print_list_node(l: Optional[ListNode]):
    res = []

    while l is not None:
        res.append(l.val)
        l = l.next

    print(res)

def main():
    # l1 = create_list_node([2, 4, 3])
    # l2 = create_list_node([5, 6, 4])

    # l1 = create_list_node([0])
    # l2 = create_list_node([0])

    # l1 = create_list_node([9,9,9,9,9,9,9])
    # l2 = create_list_node([9,9,9,9])

    l1 = create_list_node([9,9,9,9])
    l2 = create_list_node([9,9,9,9,9,9,9])
    
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    print_list_node(res)

if __name__ == "__main__":
    main()
