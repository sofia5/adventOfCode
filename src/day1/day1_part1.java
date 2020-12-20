package day1;

import static java.lang.System.out;

import java.io.File;
import java.util.*;
import java.io.FileNotFoundException;

public class day1_part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scan = new Scanner(new File("C:\\Users\\Sofia\\IdeaProjects\\adventOfCode2018\\src\\day1\\day1_input.txt"));
        int answer = 0;
        while(scan.hasNext()) {
            String input = scan.nextLine();
            if(input.substring(0,1).equals("-")){
                answer -= Integer.parseInt(input.substring(1));
            }
            else if(input.substring(0,1).equals("+")){
                answer += Integer.parseInt(input.substring(1));
            }
        }

        out.println(answer);
    }
}