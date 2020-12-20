package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part1 {
    static int code = 0;
    static int sum = 0;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("code.txt"));
        String answer = input.nextLine();

        for(int i = 0; i <= answer.length() - 1; i++){
            if(i == answer.length() - 1){
                if(answer.charAt(answer.length() - 1) == answer.charAt(0)){
                    sum = sum + (answer.charAt(answer.length() - 1) - '0');
                }
            }
            else if(answer.charAt(i) == answer.charAt(i + 1)){
                sum = sum + (answer.charAt(i) - '0');

                if(i <= answer.length() - 3 && (answer.charAt(i + 1) != answer.charAt(i + 2))){
                    code = code + sum;
                    sum = 0;
                }
            }
        }
        code = code + sum;
        System.out.print(code);
    }
}
