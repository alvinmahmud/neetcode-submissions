class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let l = 0;
        let r = numbers.length - 1;

        while (l < r) {
            const added = numbers[l] + numbers[r];

            if (added == target) {
                return [l + 1, r + 1]
            } else if (added < target) {
                l++;
            } else {
                r--;
            }
        }

        return [];
    }
}
