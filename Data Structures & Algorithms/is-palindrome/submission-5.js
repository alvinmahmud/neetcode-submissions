class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const alphanum = '0123456789abcdefghijklmnopqrstuvwxyz';

        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            while (l < r && !alphanum.includes(s[l].toLowerCase())) l++;
            while (l < r && !alphanum.includes(s[r].toLowerCase())) r--;

            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
}
