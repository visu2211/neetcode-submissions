class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix[0].length - 1;
        int lo = 0;
        int hi = matrix.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (matrix[mid][0] <= target && matrix[mid][n] >= target) {
                for (int i = 0; i <= n; i++) {
                    if (matrix[mid][i] == target)
                        return true;
                }
                return false;
            }
            else if (matrix[mid][0] > target)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        return false;
    }
}
