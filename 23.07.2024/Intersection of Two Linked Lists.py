class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection_node():
    def build_list(nums, intersection=None):
        if not nums:
            return intersection
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        if intersection:
            current.next = intersection
        return head

    def find_intersection(headA, headB):
        if not headA or not headB:
            return None

        a_pointer, b_pointer = headA, headB

        while a_pointer != b_pointer:
            a_pointer = a_pointer.next if a_pointer else headB
            b_pointer = b_pointer.next if b_pointer else headA

        return a_pointer

    nums1 = list(map(int, input("Enter the first linked list (space-separated): ").split()))
    nums2 = list(map(int, input("Enter the second linked list (space-separated): ").split()))
    intersection_nums = list(map(int, input("Enter the intersection list (space-separated): ").split()))

    intersection = build_list(intersection_nums)
    headA = build_list(nums1, intersection)
    headB = build_list(nums2, intersection)

    intersection_node = find_intersection(headA, headB)

    if intersection_node:
        print(f"Intersection node value: {intersection_node.val}")
    else:
        print("No intersection node found")

get_intersection_node()
