class Solution {
    public boolean isAnagram(String s, String t) {
        char[] Array1 = s.toCharArray();
        char[] Array2 = t.toCharArray();

        Arrays.sort(Array1);
        Arrays.sort(Array2);

        return Arrays.equals(Array1, Array2);
    }
}
