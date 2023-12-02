class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        String num;
        for(int i =0; i + p.length() <= t.length(); i++){
            num = t.substring(i, i+p.length());
            if(Long.parseLong(num) <= Long.parseLong(p))    answer += 1;
            
        }
        return answer;
    }
}