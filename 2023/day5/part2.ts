import { chunk, reverse } from "lodash-es";
import { readInput } from "../utils.js";

const lines = readInput("day5/input.txt");

const start = performance.now();

const filterUndefined = (line: string) => line.trim();
const convertToNumber = (num: string) => Number(num);

const groupedSeeds = lines
  .join(",")
  .split(",,")
  .map((line) => line.split(/[:,|,]/g).filter(filterUndefined));

const [seeds, ...steps] = groupedSeeds;

const validNumbers = chunk(
  seeds[1].split(" ").filter(filterUndefined).map(convertToNumber),
  2
);

const valueNumbers = validNumbers.map(([start]) => start);
const valueMax = Math.max(...valueNumbers);

type StepArray = number[][][];

const stepArray = reverse(
  steps.reduce<StepArray>((stepMap, step) => {
    const [, ...stepTransformations] = step;
    const transformations = stepTransformations.map((transformation) =>
      transformation.split(" ").map(convertToNumber)
    );

    stepMap.push(transformations);

    return stepMap;
  }, [])
);

let isFinished = false;
let i = 0;
const validReturnedNumbers = [];

while (!isFinished) {
  let num = i;
  Object.values(stepArray).forEach((steps) => {
    steps.find((step) => {
      const [to, from, range] = step;
      if (num >= to && num <= to + range) {
        num = num - to + from;
        return true;
      }

      return false;
    });
  });

  if (i === valueMax) {
    isFinished = true;
  }

  if (num >= 0 && num <= valueMax * 2) {
    if (
      validNumbers.find(
        ([start, range]) => num >= start && num <= start + range
      )
    ) {
      isFinished = true;
      validReturnedNumbers.push(i);
    }
  }

  i++;
}

const smallestTransformedNumber = Math.min(...validReturnedNumbers);

const end = performance.now();
console.log(smallestTransformedNumber, end - start);
