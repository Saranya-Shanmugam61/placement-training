def find_median_sorted_arrays():
    nums1 = list(map(int, input("Enter the first sorted array (space-separated): ").split()))
    nums2 = list(map(int, input("Enter the second sorted array (space-separated): ").split()))
    nums = sorted(nums1 + nums2)
    length = len(nums)
    
    if length % 2 == 0:
        median = (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        median = nums[length // 2]

    print(f"The median is: {median}")

find_median_sorted_arrays()
