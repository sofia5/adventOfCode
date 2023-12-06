import { readInput } from "../utils.js";

const lines = readInput("day6/input.txt");

const [times, records] = lines.map((line) =>
  line
    .split(/\s+/)
    .slice(1)
    .map((num) => Number(num))
);

const allBeatenRecordsMultiplied = times
  .map(
    (time, index) =>
      Array.from({ length: time })
        .map((_, i) => i * (time - i))
        .filter((num) => num > records[index]).length
  )
  .reduce((a, b) => a * b, 1);

console.log(allBeatenRecordsMultiplied);
