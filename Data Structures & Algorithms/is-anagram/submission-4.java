class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> dict1 = new HashMap<>();
        Map<Character, Integer> dict2 = new HashMap<>();

        for(char letter : s.toCharArray()) {
            dict1.put(letter, dict1.getOrDefault(letter, 0) + 1);
        }

        for(char letter : t.toCharArray()) {
            dict2.put(letter, dict2.getOrDefault(letter, 0) + 1);
        }


        return dict1.equals(dict2);
    }
}
