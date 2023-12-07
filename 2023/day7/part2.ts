import { readInput, sumNumbers } from "../utils.js";

const lines = readInput("day7/input.txt");

type CardMap = Record<string, number>;

const joker = "J";

const cardValue: CardMap = {
  J: 0,
  T: 10,
  Q: 12,
  K: 13,
  A: 14,
} as const;

const getMax = (cardTotals: number[]) =>
  cardTotals.length > 0 ? Math.max(...cardTotals) : 0;

const getCardCombination = (cards: CardMap) => {
  const jokerTotal = joker in cards ? cards[joker] : 0;
  const cardTotals = Object.entries(cards)
    .filter(([k]) => k !== joker)
    .map(([_, v]) => v);

  const cardMax = getMax(cardTotals);
  const max = cardMax + jokerTotal;
  const maxIndex = cardTotals.indexOf(cardMax);
  const secondMax = getMax(cardTotals.filter((_, i) => i !== maxIndex));

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
