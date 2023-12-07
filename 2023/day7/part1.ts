import { readInput, sumNumbers } from "../utils.js";

const lines = readInput("day7/input.txt");

type CardMap = Record<string, number>;

const cardValue: CardMap = {
  T: 10,
  J: 11,
  Q: 12,
  K: 13,
  A: 14,
} as const;

const getCardCombination = (cards: CardMap) => {
  const cardTotals = Object.values(cards);
  const max = Math.max(...cardTotals);
  const maxIndex = cardTotals.indexOf(max);
  const secondMax = Math.max(...cardTotals.filter((_, i) => i !== maxIndex));

  switch (max) {
    case 5:
      return 6;
    case 4:
      return 5;
    case 3:
      return secondMax === 2 ? 4 : 3;
    case 2:
      return secondMax === 2 ? 2 : 1;
    default:
      return 0;
  }
};

const getStrength = (cardArr: string[]) => {
  const cardMap = cardArr.reduce<CardMap>((map, val) => {
    map[val] = (map[val] ?? 0) + 1;
    return map;
  }, {});

  return getCardCombination(cardMap);
};

const getHandValue = (cardArr: string[]) => {
  return cardArr.map((card) => {
    const cardAsNum = Number(card);
    return isNaN(cardAsNum) ? cardValue[card as keyof CardMap] : cardAsNum;
  });
};

const sortedWinners = lines
  .map((line) => {
    const parts = line.split(" ");
    const cardArr = Array.from(parts[0]);

    return {
      bet: Number(parts[1]),
      strength: getStrength(cardArr),
      handValues: getHandValue(cardArr),
    };
  })
  .sort((a, b) => {
    if (b.strength !== a.strength) {
      return a.strength - b.strength;
    }

    const index = b.handValues.findIndex((val, i) => val !== a.handValues[i]);
    return b.handValues[index] < a.handValues[index] ? 1 : -1;
  });

const sumOfSortedWinners = sumNumbers(
  sortedWinners.map((res, i) => res.bet * (i + 1))
);

console.log(sumOfSortedWinners);
