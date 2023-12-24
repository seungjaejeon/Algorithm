import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int count = 0;
        Stack<Integer> bowl = new Stack<>();
        for(int i = 0; i<moves.length; i++){
            for(int j=0; j < board[moves[i]-1].length; j++){
                if(board[j][moves[i]-1]>0){
                    if(!bowl.empty()){
                        if(bowl.peek()==board[j][moves[i]-1]){
                            board[j][moves[i]-1] = 0;
                            bowl.pop();
                            answer += 2;
                            break;
                        }
                    }
                    bowl.push(board[j][moves[i]-1]);
                    board[j][moves[i]-1] = 0;
                    break;
                }
            }
        }
        
        return answer;
    }
}

//1, 5, 3, 5, 1, 2, 1, 4 뽑기
//4, 3, 1, 1, 3, 2, 4 뽑힌 인형
// 0,0 1,0 2,0 3,0
// 0,4 1,4 2,4 3,4 4,4
// 0 1
// 0 0 1
// 