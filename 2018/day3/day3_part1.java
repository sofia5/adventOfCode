package day3;

import static java.lang.System.out;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;

public class day3_part1 {
    public static void main(String[] args) throws FileNotFoundException {

        Scanner scan = new Scanner(new File("C:\\Users\\Sofia\\IdeaProjects\\adventOfCode2018\\src\\day3\\day3_input.txt"));
        HashMap<String,Boolean> map = new HashMap<>();
        int count = 0;

        while(scan.hasNext()){
            String input = scan.nextLine();
            input = input.replace(" ","");
            int position_x = Integer.parseInt(input.substring(input.indexOf("@") + 1,input.indexOf(",")));
            int position_y = Integer.parseInt(input.substring(input.indexOf(",") + 1,input.indexOf(":")));
            int area_x = Integer.parseInt(input.substring(input.indexOf(":") + 1,input.indexOf("x")));
            int area_y = Integer.parseInt(input.substring(input.indexOf("x") + 1));

            int cur_x = position_x;

            for(int i = 0; i < area_x; i++){
                int cur_y = position_y;
                for(int j = 0; j < area_y; j++) {

                    String position = cur_x + "," + cur_y;
                    if(map.containsKey(position) && map.get(position)){
                        map.put(position, false);
                        count++;
                    }
                    else if(!map.containsKey(position)){
                        map.put(position, true);
                    }
                    cur_y++;
                }
                cur_x++;
            }
        }
        out.print("The total number of duplicate positions are: " + count);
    }
}
