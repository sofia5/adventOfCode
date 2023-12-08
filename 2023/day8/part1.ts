import { readInput } from "../utils.js";

const lines = readInput("day8/input.txt");

const [instructions, , ...directions] = lines[0].split("\n");
let i = 1;
let currentPosition = "AAA";
const endPosition = "ZZZ";
let isFinished = false;

const map = directions.reduce<Record<string, [string, string]>>(
  (acc, direction) => {
    const [start, leftRight] = direction.replaceAll(/[(\s+)]/g, "").split("=");
    const [left, right] = leftRight.split(",");

    acc[start] = [left, right];
    return acc;
  },
  {}
);

while (!isFinished) {
  Array.from(instructions).every((instruction) => {
    const [left, right] = map[currentPosition];
    currentPosition = instruction === "L" ? left : right;
    if (currentPosition === endPosition) {
      console.log(i);
      isFinished = true;
      return false;
    }
    i++;
    return true;
  });
}
