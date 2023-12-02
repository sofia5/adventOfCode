"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const utils_1 = require("../utils");
const lines = (0, utils_1.readInput)("day1/input.txt");
const sum = lines
    .map((line) => line.replace(/\D/g, ''))
    .map((num) => Number(num[0] + num[num.length - 1]))
    .filter((num) => !isNaN(num))
    .reduce((partialSum, a) => partialSum + a, 0);
console.log(sum);
