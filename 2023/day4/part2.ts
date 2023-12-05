import { intersection } from "lodash-es";
import { readInput } from "../utils.js";

const lines = readInput("day4/input.txt");

const cardCopies = Array.from({ length: lines.length }).reduce<
  Record<number, number>
>((acc, _, index) => {
  acc[index] = 1;
  return acc;
}, {});

const convertToNumberArray = (numbers: string) =>
  numbers
    .split(" ")
    .map((num) => Number(num.trim()))
    .filter((item) => item);

lines.map((line, index) => {
  const numbers = line.substring(line.indexOf(": ") + 1).split("|", 2);
  const winningNumbers = convertToNumberArray(numbers[0]);
  const selectedNumbers = convertToNumberArray(numbers[1]);

  const numberOfWinning = intersection(winningNumbers, selectedNumbers).length;
  const curCardCopies = cardCopies[index];
  Array.from({ length: numberOfWinning }).forEach((_, i) => {
    const curIndex = index + 1 + i;
    cardCopies[curIndex] += curCardCopies;
  });
});

const sum = Object.values(cardCopies).reduce(
  (partialSum, a) => partialSum + a,
  0
);

console.log(sum);
