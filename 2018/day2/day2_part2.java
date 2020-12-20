package day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.sql.Array;
import java.util.LinkedList;
import java.util.Scanner;
import static java.lang.System.out;

public class day2_part2 {

    public static void main(String[] args) throws FileNotFoundException {

        Scanner scan = new Scanner(new File("C:\\Users\\Sofia\\IdeaProjects\\adventOfCode2018\\src\\day2\\day2_input.txt"));

        LinkedList<String> list = new LinkedList<>();

        while(scan.hasNext()){
            String input = scan.nextLine();
            list.add(input);
        }

        for(int i = 0; i < list.size(); i++){

            for(int j = 0; j < list.size(); j++){
                String currentWord = list.get(i);
                String compareWord = list.get(j);
                if(i != j){
                    for(int k = 0; k < currentWord.length();k++) {
                        StringBuilder sbCurrentWord = new StringBuilder(currentWord);
                        StringBuilder sbCompareWord = new StringBuilder(compareWord);
                        sbCurrentWord.deleteCharAt(k);
                        sbCompareWord.deleteCharAt(k);
                        if (sbCurrentWord.toString().equals(sbCompareWord.toString())){
                            out.println("The matching letters are: " + sbCurrentWord);
                            return;
                        }
                    }
                }

            }
        }

    }
}
