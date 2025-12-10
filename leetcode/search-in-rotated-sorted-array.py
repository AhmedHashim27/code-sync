class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        # Initialize the right pointer to the end of the array
        r = len(nums) - 1

        # Standard Binary Search loop condition
        while l <= r:
            # Calculate the middle index to avoid potential overflow (in other languages)
            # In Python, (l + r) // 2 is fine, but l + (r - l) // 2 is safer habit.
            mid = (l + r) // 2
            
            # Check if we found the target immediately
            if nums[mid] == target:
                return mid
            
            # Now we need to figure out which part of the array is sorted.
            # Case 1: The Left half is sorted.
            # We know this because the start value is less than or equal to the mid value.
            if nums[l] <= nums[mid]:
                # If Left is sorted, check if target is inside this range.
                # Target must be greater than or equal to Left AND less than Mid.
                if nums[l] <= target < nums[mid]:
                    # Target is in the left side, so we discard the right side.
                    r = mid - 1
                else:
                    # Target is NOT in the left side, so it must be in the right side.
                    l = mid + 1
            
            # Case 2: The Right half is sorted.
            # If the left wasn't sorted, the right MUST be sorted.
            else:
                # If Right is sorted, check if target is inside this range.
                # Target must be greater than Mid AND less than or equal to Right.
                if nums[mid] < target <= nums[r]:
                    # Target is in the right side, so we discard the left side.
                    l = mid + 1
                else:
                    # Target is NOT in the right side, so it must be in the left side.
                    r = mid - 1
        
        # If we exit the loop, the target was not found.
        return -1