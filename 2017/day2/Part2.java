package Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("checksum.txt"));

        int sum = 0;

        while(input.hasNextLine()){
            String line = input.nextLine();
            String[] numbers = line.split("\t");


            for(int i = 0; i < numbers.length; i++){

                for(int j = 0; j < numbers.length; j++){

                    if(parseInt(numbers[i]) % parseInt(numbers[j]) == 0 && parseInt(numbers[i]) / parseInt(numbers[j]) != 1) {
                        sum = sum + parseInt(numbers[i]) / parseInt(numbers[j]);
                    }
                }

            }
        }
        System.out.print(sum);
    }
}
