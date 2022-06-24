public class RGB_sactter {
    public static char[] partition(char [] arr) {
  
        int low=0;
        int mid =0;
        int high = arr.length-1;
        
        while(mid<=high) {
         if(arr[mid] == 'R') {
          char temp = arr[mid];
          arr[mid] = arr[low];
          arr[low] = temp;
          low++;
          mid++;
         }
         else if(arr[mid] == 'G') {
          mid++;
         }
         else {
          char temp = arr[high];
          arr[high] = arr[mid];
          arr[mid] = temp;
          high--;
         }
        }
        return arr;
      
       }
       public static void main(String args[]){
        char[] JavaCharArray = {'G', 'B', 'R', 'R', 'B', 'R', 'G'};
        char[] result=partition(JavaCharArray);
        for(int i=0;i<result.length;i++){
            System.out.println(result[i]);
        }

       }
      
    
}
