package Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("checksum.txt"));

        int sum = 0;

        while(input.hasNextLine()){
            String line = input.nextLine();
            String[] numbers = line.split("\t");
            int min = parseInt(numbers[0]);
            int max = parseInt(numbers[0]);
            for(int i = 0; i < numbers.length; i++){
                if(parseInt(numbers[i]) < min){
                    min = parseInt(numbers[i]);
                }
                if(parseInt(numbers[i]) > max){
                    max = parseInt(numbers[i]);
                }

            }
            sum = sum + (max-min);
        }
        System.out.print(sum);
    }
}
