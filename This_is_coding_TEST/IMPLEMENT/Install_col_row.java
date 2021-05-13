import java.util.*;

class Command implements Comparable<Command>{
    int x;
    int y;
    int kind;

    public Command(int x, int y, int kind) {
        this.x = x;
        this.y = y;
        this.kind = kind;
    }
    @Override
    public boolean equals(Object o) {
       if(!(o instanceof Command)) return false;
       Command c = (Command)o;
       return c.x == this.x && c.y == this.y && c.kind == this.kind;
    }
    @Override
    public int compareTo(Command other){
        if (this.x == other.x && this.y == other.y) {
            return Integer.compare(this.kind, other.kind);
        }
        if (this.x == other.x) {
            return Integer.compare(this.y, other.y);
        }
        return Integer.compare(this.x, other.x);
    }
}

class Install_col_row {
    public int[][] solution(int n, int[][] build_frame) {
        int[][] answer = {};
        List<Command> list = new ArrayList<>();
        for (int[] frame : build_frame) {
            Command command = new Command(frame[0], frame[1], frame[2]);
            
            if (frame[3] == 0) { // 제거시
                list.remove(command);
                if (!check(list)) {
                    list.add(command);
                }
            } else if (frame[3] == 1) { // 설치시
                list.add(command);
                if (!check(list)) {
                    list.remove(command);
                }
            }
        
        }
        Collections.sort(list);
        answer = new int[list.size()][];
        for (int i = 0; i < list.size(); i++) {
            Command c = list.get(i);
            answer[i] = new int[] { c.x, c.y, c.kind };
            
        }
        
        return answer;
    }

    public boolean check(List<Command> list) {
        for (Command command : list) {
            if (command.kind == 0) { // 기둥인경우
                if (command.y == 0 || (list.contains(new Command(command.x - 1, command.y, 1)))
                        || (list.contains(new Command(command.x, command.y, 1)))
                        || (list.contains(new Command(command.x, command.y - 1, 0)))) {
                        
                    continue;
                }
                
                return false;
            } else if (command.kind == 1) { // 보인경우
                if (list.contains(new Command(command.x, command.y - 1, 0))
                        || list.contains(new Command(command.x + 1, command.y - 1, 0))
                        || (list.contains(new Command(command.x - 1, command.y, 1))
                                && list.contains(new Command(command.x, command.y, 1)))) {
                                    
                    continue;
                }
                
                return false;
            }
        }
        
        return true;
    }
}
