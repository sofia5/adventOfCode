package day3;

import static java.lang.System.out;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class day3_part2 {
    public static void main(String[] args) throws FileNotFoundException {

        Scanner scan = new Scanner(new File("C:\\Users\\Sofia\\IdeaProjects\\adventOfCode2018\\src\\day3\\day3_input.txt"));
        Map<String, List<Integer>> map = new HashMap<>();
        Map<Integer, Boolean> id_map = new HashMap<>();

        int count = 0;

        while(scan.hasNext()){
            String input = scan.nextLine();
            input = input.replace(" ","");
            int id = Integer.parseInt(input.substring(1, input.indexOf("@")));
            int position_x = Integer.parseInt(input.substring(input.indexOf("@") + 1,input.indexOf(",")));
            int position_y = Integer.parseInt(input.substring(input.indexOf(",") + 1,input.indexOf(":")));
            int area_x = Integer.parseInt(input.substring(input.indexOf(":") + 1,input.indexOf("x")));
            int area_y = Integer.parseInt(input.substring(input.indexOf("x") + 1));

            int cur_x = position_x;
            id_map.put(id, true);

            for(int i = 0; i < area_x; i++){
                int cur_y = position_y;
                for(int j = 0; j < area_y; j++) {

                    String position = cur_x + "," + cur_y;
                    if(map.containsKey(position) && map.get(position).size() >= 1){
                        List<Integer> id_list = map.get(position);
                        id_list.add(id);
                        map.put(position, id_list);
                        for (int current_id : id_list) {
                            id_map.put(current_id, false);
                        }
                    }

                    else if(!map.containsKey(position)){
                        List<Integer> id_list = new ArrayList<>();
                        id_list.add(id);
                        map.put(position, id_list);
                    }

                    cur_y++;
                }
                cur_x++;
            }
        }

        for (Map.Entry<Integer, Boolean> entry : id_map.entrySet()){
            if(entry.getValue()) {
                out.println("The ID which is not overlapping is: " + entry.getKey());
            }
        }
    }
}
