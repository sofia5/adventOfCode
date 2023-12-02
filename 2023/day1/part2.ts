import { readInput } from "../utils"

const mapNumbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

const updateLine = (line: string) => {
    Object.keys(mapNumbers).forEach(key => {
        line = line.replaceAll(key, match => match + mapNumbers[match as keyof typeof mapNumbers] + match)
    });
    return line
}

const lines = readInput("day1/input.txt") 

const sum = lines
  .map((line) => updateLine(line)) 
  .map((line) => line.replace(/\D/g, ''))
  .map((num) => Number(num[0] + num[num.length - 1]))
  .filter((num) => !isNaN(num))
  .reduce((partialSum, a) => partialSum + a, 0)

console.log(sum)
