'''his problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.'''
class trappedWater
{
  
    public static int trap(int[] bars)
    {
        int n = bars.length;
        
        
        if (n <= 2) {
            return 0;
        }
 
        int water = 0;
 
       
        int[] left = new int[n-1];
        left[0] = Integer.MIN_VALUE;
 
       
        for (int i = 1; i < n - 1; i++) {
            left[i] = Integer.max(left[i - 1], bars[i - 1]);
        }
 
       
        int right = Integer.MIN_VALUE;
 
       
        for (int i = n - 2; i >= 1; i--)
        {
            right = Integer.max(right, bars[i + 1]);
 
         
            if (Integer.min(left[i], right) > bars[i]) {
                water += Integer.min(left[i], right) - bars[i];
            }
        }
 
        return water;
    }
 
    public static void main(String[] args)
    {
        int[] heights = { 3,0,1,3,0,5 };
 
        System.out.print(trap(heights));
    }
}

