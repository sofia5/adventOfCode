import { readInput } from "../utils.js";

type CubeColor = "red" | "green" | "blue";
const cubeColors = ["red", "green", "blue"];

const lines = readInput("day2/input.txt");

const isCubeColor = (color: string): color is CubeColor =>
  cubeColors.includes(color.trim());

const updateMinCubeValue = (
  maxPerColor: Map<CubeColor, number>,
  numberOfCubes: number,
  cubeColor: CubeColor
) => {
  const currentMax = maxPerColor.get(cubeColor) ?? 0;
  if (numberOfCubes > currentMax) {
    maxPerColor.set(cubeColor, numberOfCubes);
  }

  return maxPerColor;
};

const getMinForGameSet = (
  gameSet: string,
  maxPerColor: Map<CubeColor, number>
) => {
  const cubesDrawn: [number, CubeColor][] = gameSet
    .split(", ")
    .map((cube) => {
      const cubeArr = cube.split(" ");
      return [Number(cubeArr[0]), cubeArr[1]] as [number, string];
    })
    .filter(
      (cube): cube is [number, CubeColor] =>
        !isNaN(Number(cube[0])) && isCubeColor(cube[1])
    );

  cubesDrawn.forEach(
    (cube) =>
      (maxPerColor = updateMinCubeValue(maxPerColor, Number(cube[0]), cube[1]))
  );

  return maxPerColor;
};

const gameSetValues = lines.map((line) => {
  let maxPerColor = new Map<CubeColor, number>();
  cubeColors.filter(isCubeColor).forEach((color) => maxPerColor.set(color, 0));

  const row = line.split(": ");
  const gameSets = row[1].split("; ");

  gameSets.forEach(
    (gameSet) => (maxPerColor = getMinForGameSet(gameSet, maxPerColor))
  );

  return [...maxPerColor.values()].reduce((a, b) => a * b, 1);
});

const sum = gameSetValues.reduce(
  (partialSum, a) => (partialSum ?? 0) + (a ?? 0),
  0
);

console.log(sum);
