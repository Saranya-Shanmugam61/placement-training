class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists():
    def build_list(nums):
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def print_list(node):
        while node:
            print(node.val, end=" -> " if node.next else "\n")
            node = node.next

    nums1 = list(map(int, input("Enter the first sorted list (space-separated): ").split()))
    nums2 = list(map(int, input("Enter the second sorted list (space-separated): ").split()))

    l1 = build_list(nums1)
    l2 = build_list(nums2)

    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    print("Merged sorted list:")
    print_list(dummy.next)

merge_two_sorted_lists()
