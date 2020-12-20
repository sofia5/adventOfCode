package day2;

import static java.lang.System.out;

import java.io.File;
import java.util.*;
import java.io.FileNotFoundException;

public class day2_part1 {

    public static void main(String[] args) throws FileNotFoundException {

            Scanner scan = new Scanner(new File("C:\\Users\\Sofia\\IdeaProjects\\adventOfCode2018\\src\\day2\\day2_input.txt"));
            String temp;
            int count_two_identical_letters = 0;
            int count_three_identical_letters = 0;

            while(scan.hasNext()){
                temp = scan.nextLine();
                String [] temp_letter = new String[temp.length()];
                boolean flag_two_identical_letters = false;
                boolean flag_three_identical_letters = false;

                for(int i = 0; i < temp.length();i++){
                    temp_letter[i] = temp.substring(i, i + 1);
                }

                for(int i = 0; i < temp.length();i++){
                    int count = 0;

                    for (int j = 0; j < temp.length();j++){
                        if(temp_letter[i].equals(temp_letter[j])){
                            count++;
                        }
                    }
                    if(count == 2 && !flag_two_identical_letters){
                        flag_two_identical_letters = true;
                        count_two_identical_letters++;
                    }
                    if(count == 3 && !flag_three_identical_letters){
                        flag_three_identical_letters = true;
                        count_three_identical_letters++;
                    }
                }

            }
            out.println(count_two_identical_letters);
            out.println(count_three_identical_letters);
            out.println("Sum of identical letters: " + count_two_identical_letters * count_three_identical_letters);

    }
}