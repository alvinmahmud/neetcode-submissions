class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        // const ans = [];

        const ans = [...nums, ...nums];
        return ans;
    }
}
