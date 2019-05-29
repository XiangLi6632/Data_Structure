# -*-coding:utf-8-*-
"""
author：Li Xiang
date: 2019-05-29
configuration: VScode, Python 3.6.5
"""

def merge(nums1, nums1_size, nums2, nums2_size):
    """
    type nums1: List[int]
    type nums1_size: int
    type nums2: List[int]
    type nums2_size: int
    """
    nums1 += nums2
    end = nums1_size + nums2_size - 1
    nums1_size -= 1
    nums2_size -= 1
    while(nums1_size >= 0 and nums2_size >= 0):
        if nums1[nums1_size] > nums2[nums2_size]:
            nums1[end] = nums1[nums1_size]
            nums1_size -= 1
        else:
            nums1[end] = nums2[nums2_size]
            nums2_size -= 1
        end -= 1
    if nums2_size >= 0:
        nums1[:end + 1] = nums2[:nums2_size + 1]

if __name__ == "__main__":
    NUMS1 = [1, 3, 5, 9]
    NUMS2 = [2, 3, 4, 10]
    merge(NUMS1, 4, NUMS2, 4)
    print(NUMS1)
    