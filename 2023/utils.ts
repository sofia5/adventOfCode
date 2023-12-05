import { readFileSync } from "fs";

export const readInput = (filePath: string): string[] => {
  const file = readFileSync(filePath, "utf8");
  return file.split(/\r\n/);
};

export const sumNumbers = (numbers: number[]) =>
  numbers.reduce((partialSum, a) => partialSum + a, 0);
