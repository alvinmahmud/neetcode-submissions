class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const n = s.length;
        if (n !== t.length) return false;

        const ctS = {};
        const ctT = {};

        for (let i = 0; i < n; i ++) {
            ctS[s[i]] = (ctS[s[i]] || 0) + 1;
            ctT[t[i]] = (ctT[t[i]] || 0) + 1;
        }

        for (const key in ctS) {
            if (ctS[key] !== ctT[key]) return false;
        }

        return true;
    }
}
