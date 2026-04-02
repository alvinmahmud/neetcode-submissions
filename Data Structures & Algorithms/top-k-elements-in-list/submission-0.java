class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        List<int[]> keys = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            keys.add(new int[] {entry.getValue(), entry.getKey()});
        }
        
        keys.sort((a, b) -> b[0] - a[0]);

        int[] result = new int[k];
        for(int i = 0; i < k; i++) {
            result[i] = keys.get(i)[1];
        }

        return result;
    }
}
