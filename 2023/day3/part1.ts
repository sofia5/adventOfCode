import { readInput } from "../utils.js";

const lines = readInput("day3/input.txt");

const getSymbols = (lines: string[]) => {
  const rowMap = new Map();

  lines.forEach((line, index) => {
    const symbolMatches = [...line.matchAll(/[^.\d]+/g)];

    if (symbolMatches.length > 0) {
      const colMap = new Map();
      symbolMatches.forEach((match) => colMap.set(match.index, match[0]));
      rowMap.set(index, colMap);
    }
  });

  return rowMap;
};

const getNumbers = (lines: string[]) => {
  return lines.flatMap((line, index) => {
    const numberMatches = [...line.matchAll(/\d+/g)];
    return numberMatches.map((match) => ({
      number: Number(match[0]),
      colIndexStart: match.index ?? 0,
      colIndexEnd: (match.index ?? 0) + match[0].length,
      rowIndex: index,
    }));
  });
};

const symbols = getSymbols(lines);
const numbers = getNumbers(lines);

const validNumbers = numbers.filter((number) => {
  const { rowIndex, colIndexStart, colIndexEnd } = number;

  if (
    symbols.get(rowIndex)?.get(colIndexStart - 1) ||
    symbols.get(rowIndex)?.get(colIndexEnd)
  ) {
    return true;
  }

  for (let i = colIndexStart - 1; i <= colIndexEnd; i++) {
    if (
      symbols.get(rowIndex - 1)?.get(i) ||
      symbols.get(rowIndex + 1)?.get(i)
    ) {
      return true;
    }
  }

  return false;
});

const sum = validNumbers.reduce(
  (partialSum, item) => partialSum + item.number,
  0
);
console.log(sum);
