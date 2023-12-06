import { readInput } from "../utils.js";

const lines = readInput("day6/input.txt");

const [time, record] = lines.map(
  (line) =>
    line
      .replace(/\s/g, "")
      .split(":")
      .map((num) => Number(num))[1]
);

const beatenRecordSum = Array.from({ length: time })
  .map((_, i) => i * (time - i))
  .filter((num) => num > record).length;

console.log(beatenRecordSum);
