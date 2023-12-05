import { readInput } from "../utils.js";

const lines = readInput("day5/input.txt");

const filterUndefined = (line: string) => line.trim();
const convertToNumber = (num: string) => Number(num);

const groupedSeeds = lines
  .join(",")
  .split(",,")
  .map((line) => line.split(/[:,|,]/g).filter(filterUndefined));

const [seeds, ...steps] = groupedSeeds;

const seedNumbers = seeds[1]
  .split(" ")
  .filter(filterUndefined)
  .map(convertToNumber);

type StepMap = Record<string, number[][]>;

const stepMap = steps.reduce<StepMap>((stepMap, step) => {
  const [stepName, ...stepTransformations] = step;
  const transformations = stepTransformations.map((transformation) =>
    transformation.split(" ").map(convertToNumber)
  );

  stepMap[stepName] = transformations;

  return stepMap;
}, {});

const transformedNumbers = seedNumbers.map((originalNum) => {
  let num = originalNum;

  Object.values(stepMap).forEach((steps) =>
    steps.find((step) => {
      const [to, from, range] = step;
      if (num >= from && num <= from + range) {
        num = num + to - from;
        return true;
      }

      return false;
    })
  );

  return num;
});

const smallestTransformedNumber = Math.min(...transformedNumbers);

console.log(smallestTransformedNumber);
