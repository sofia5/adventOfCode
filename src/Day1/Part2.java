package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part2 {

    static int code = 0;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("code.txt"));
        String answer = input.nextLine();

        int steps = answer.length() / 2;

        for(int i = 0; i < answer.length() - 1; i++){

            if(i + steps > answer.length() - 1){
                int newSteps = i + steps - answer.length();
                if(answer.charAt(i) == answer.charAt(newSteps)){
                    code = code + answer.charAt(i) - '0';
                }
            }
            else if(answer.charAt(i) == answer.charAt(i + steps)){
                code = code + answer.charAt(i) - '0';

            }
        }
        System.out.print(code);
    }
}
