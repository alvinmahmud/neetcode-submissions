class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagrams = {}; 
        const output = [];

        for (const str of strs) {
            const counter = new Array(26).fill(0);

            for (const char of str) {
                const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
                counter[idx] += 1;
            }

            const ctr = counter.join(',');

            if (!(ctr in anagrams)) {
                anagrams[ctr] = [];
            }

            anagrams[ctr].push(str)
        }

        for (const key in anagrams) {
            output.push(anagrams[key]);
        }

        return output;
    }
}
