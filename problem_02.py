def find_common_elements(nums1, nums2):
    index_received = []
    result = []
    for ele1 in nums1:
        for i, ele2 in enumerate(nums2):
            if ele1 == ele2 and i not in index_received:
                result.append(ele1)
                index_received.append(i)
                break
    return result

# Case 1
nums1_case1 = [1, 2, 2, 1]
nums2_case1 = [2, 2]
print(find_common_elements(nums1_case1, nums2_case1))

# Case 2
nums1_case2 = [4, 9, 5]
nums2_case2 = [9, 4, 9, 8, 4]
print(find_common_elements(nums1_case2, nums2_case2))
