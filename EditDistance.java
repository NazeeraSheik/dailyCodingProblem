
public class EditDistance {
	public static int minMax(int a,int b,int c) {
		return Math.min(a,Math.min(b, c));
	}
  public static int calculateDistance(String s1,int m,String s2,int n){
	  int cost=0;
	  if(m==0) {
		  return n;
	  }
	  if(n==0) {
		  return m;
	  }
	  if(s1.charAt(m-1)==s2.charAt(n-1)) {
		  cost=0;
	  }
	  else {
		  cost=1;
	  }
	  return minMax(
		  
		  calculateDistance(s1,m-1,s2,n)+1,
		  calculateDistance(s1,m,s2,n-1)+1,
		  calculateDistance(s1,m-1,s2,n-1)+cost

	  );

	  
		  
	  

	  
  }
  public static void main(String args[]) {
	  String str1="Horse";
	  String str2="Rose";
	  int k=calculateDistance(str1,str1.length(),str2,str2.length());
	  System.out.print(k);
	  
  }

}
