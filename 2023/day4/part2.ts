import { intersection } from "lodash-es";
import { readInput } from "../utils.js";

const lines = readInput("day4/testInput.txt");

const convertToNumberArray = (numbers: string) =>
  numbers
    .split(" ")
    .map((num) => Number(num.trim()))
    .filter((item) => item);

for (let i = 0; i <= lines.length; i++) {
  const numbers = lines[i].substring(lines[i].indexOf(": ") + 1).split("|", 2);
  const winningNumbers = convertToNumberArray(numbers[0]);
  const selectedNumbers = convertToNumberArray(numbers[1]);

  const numberOfWinning = intersection(winningNumbers, selectedNumbers).length;
}
