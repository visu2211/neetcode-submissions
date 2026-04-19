class Solution {
    public int leastInterval(char[] tasks, int n) {
       HashMap<Character, Integer> freqList = new HashMap<>();

        for (char t: tasks)
            freqList.put(t, freqList.getOrDefault(t, 0) + 1);
        PriorityQueue<Integer> maxHeap = new PriorityQueue(Collections.reverseOrder());

        maxHeap.addAll(freqList.values());

        int time = 0;

        Deque<int[]> queue = new ArrayDeque<>();
        while (!maxHeap.isEmpty() || !queue.isEmpty()) {
            if (!queue.isEmpty() && time >= queue.peek()[1])
                maxHeap.offer(queue.poll()[0]);
            if (!maxHeap.isEmpty()) {
                int cnt = maxHeap.poll() - 1;
                if (cnt > 0)
                    queue.offer(new int[]{cnt, time + n + 1});
            }
            time++;
        }
        return time;
    }
}