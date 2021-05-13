import java.util.ArrayList;
import java.util.List;

public class test {
    public static void main(String[] args){
        int[][] build_frame = {
            {1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}
        };
        int[][] build_frame2 = {
            {0, 0, 0, 1}, {2, 0, 0, 1}, {4, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 1, 1}, {2, 1, 1, 1}, {3, 1, 1, 1}, {2, 0, 0, 0}, {1, 1, 1, 0}, {2, 2, 0, 1}
        };
        Install_col_row i = new Install_col_row();
        int[][] result = i.solution(5, build_frame2);

        for(int j = 0; j<result.length; j++){
            System.out.println(result[j][0] + "" + result[j][1] +"" +result[j][2]);
        }
    }
}
