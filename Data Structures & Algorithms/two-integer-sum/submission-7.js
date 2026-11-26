class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const complement = new Map();

        for (let i = 0; i < nums.length; i++) {
            const find = target - nums[i];

            if (complement.has(find)) {
                return [complement.get(find), i]
            }

            complement.set(nums[i], i);
        }

        return [];
    }
}
