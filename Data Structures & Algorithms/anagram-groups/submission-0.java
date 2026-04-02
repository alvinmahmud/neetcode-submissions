class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> answer = new HashMap<>();

        for (String str : strs) {
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String sorted = new String(array);

            answer.putIfAbsent(sorted, new ArrayList<>());
            answer.get(sorted).add(str);
        }

        return new ArrayList<>(answer.values());
    }
}
