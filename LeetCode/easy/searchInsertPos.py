
# def searchInsert(nums, target):
#     i, should_be = 0, 0

#     while i < len(nums):
#        if nums[i] == target:
#            return i
#         else:
#             if nums[i] < target:
#             should_be = i
#         i += 1

#     return should_be


def searchInsert(nums, target):
    i, should_be = 0, 0

    while i < len(nums):
        if nums[i] == target:
            return 1
        else:
            if nums[i] < target:
                should_be = 1

        i += 1

    return should_be
