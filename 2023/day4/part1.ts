import { intersection } from "lodash-es";
import { readInput } from "../utils.js";

const lines = readInput("day4/input.txt");

const convertToNumberArray = (numbers: string) =>
  numbers
    .split(" ")
    .map((num) => Number(num.trim()))
    .filter((item) => item);

const totalCorrect = lines
  .map((line) => {
    const numbers = line.substring(line.indexOf(": ") + 1).split("|", 2);
    const winningNumbers = convertToNumberArray(numbers[0]);
    const selectedNumbers = convertToNumberArray(numbers[1]);

    const numberOfWinning = intersection(
      winningNumbers,
      selectedNumbers
    ).length;

    return numberOfWinning ? 1 * Math.pow(2, numberOfWinning - 1) : 0;
  })
  .reduce((partialSum, item) => partialSum + item, 0);

console.log(totalCorrect);
