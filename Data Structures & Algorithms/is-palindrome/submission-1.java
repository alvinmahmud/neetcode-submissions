class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replace(" ", "").toLowerCase();

        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            while (left < right && !isAlphaNum(str.charAt(left), str)) left++;
            while (left < right && !isAlphaNum(str.charAt(right), str)) right--;
            
            if (str.charAt(left) != str.charAt(right)) return false;

            left++;
            right--;
        }

        return true;
    }

    public boolean isAlphaNum(char name, String str) {
        return Character.isLetter(name) || Character.isDigit(name);
    }
}
