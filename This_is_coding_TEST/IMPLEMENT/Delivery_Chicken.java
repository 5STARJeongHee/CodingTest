import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Delivery_Chicken {
    public static void main(String[] args){
        int N,M;
        int[][] input;

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
    

        input = new int[N][N];

        for(int i = 0; i < N; i++ ){
            for(int j = 0; j<N; j++){
                input[i][j] = sc.nextInt();
            }
        }
        sc.nextLine();

        // for(int i = 0; i < N; i++ ){
        //     for(int j = 0; j<N; j++){
        //         System.out.print(input[i][j] +" ");
        //     }
        //     System.out.println();
        // }
        
        solution(N,M,input);
        sc.close();
    }

    public static int solution(int N, int M, int[][] input){
        Queue<Integer> que = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i = 0; i<N; i++){
            for(int j = 0; j<N; j++){
                if(input[i][j] == 2){
                    int temp = 0;
                    
                    for(int k = 0; k<N;k++){
                        for(int t = 0; t<N; t++){
                            if(input[k][t] == 1){
                                temp+= Math.abs(i-k) + Math.abs(j-t);
                            }
                        }
                    }
                    que.add(temp);
                    temp = 0;
                }
            }
        }
        while(que.size() != M){
            System.out.println(que.poll());
        }
        return 0;
    }
}

class data {
    int x;
    int y;
    int length;
}
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2