import { readInput } from "../utils.js";

const lines = readInput("day1/input.txt");

const sum = lines
  .map((line) => line.replace(/\D/g, ""))
  .map((num) => Number(num[0] + num[num.length - 1]))
  .filter((num) => !isNaN(num))
  .reduce((partialSum, a) => partialSum + a, 0);

console.log(sum);
