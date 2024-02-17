import java.io.*;

public class Main{
   static int N;
   static int [] stock;
   public static void main(String[] args) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      N = Integer.parseInt(br.readLine());
      String [] strs = br.readLine().split(" ");
      
      stock = new int [14]; 
      
      for(int i=0;i<14;i++)
         stock[i]=Integer.parseInt(strs[i]);
      
      int sumA = solutionBNP(N,stock);
      int sumB = solutionTIMING(N,stock);
      String answer = sumA > sumB ? "BNP" : (sumA < sumB ? "TIMING" : "SAMESAME");
      System.out.println(answer);
   }
   
   public static int solutionBNP(int n, int[] stock) {
      int num = 0; // 주식의 양
      for(int i=0;i<14;i++) {
         if(n/stock[i]>=1) { // 주식을 살만큼 돈이 있다면,
            num += n/stock[i];
            n = n%stock[i];
         }
      }
      return num*stock[13]+n;
   }
   public static int solutionTIMING(int n, int[] stock) {
      int num = 0;
      int upcnt =0, downcnt =0;
      for(int i=1;i<14;i++) {
         if(stock[i]>stock[i-1]) { //주식 증가
            upcnt++; //증가 카운트 ++
            downcnt=0; //감소 카운트는 그럼 0
         }   
         else if(stock[i]<stock[i-1]) { //주식 감소
            downcnt++; // 감소 카운트 ++
            upcnt=0; //그럼 증가 카운트 0
            
         }
         
         if(upcnt>=3) { // 증가 카운트가 3번이상이면
            n = num*stock[i]+n;
            num =0;  
         }
         
         if(downcnt>=3) {
            num += n/stock[i];
            n = n%stock[i];
         }
      }
      return num*stock[13]+n;
   }
}