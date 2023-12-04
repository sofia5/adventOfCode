import { readInput } from "../utils";

type Number = {
    number: number;
    colIndexStart: number;
    colIndexAfter: number;
    rowIndex: number;
}

const lines = readInput("day3/input.txt") 
const gearSymbol = '*'

const getSymbols = (lines: string[]) => {
    const rowMap = new Map()

    lines.forEach((line, index) => {
        const symbolMatches = [...line.matchAll(/[^.\d]+/g)];

        if (symbolMatches.length > 0) {
            const colMap = new Map()
            symbolMatches.forEach(match => colMap.set(match.index, match[0]))
            rowMap.set(index, colMap);
        }
    });

    return rowMap;
}

const getNumbers = (lines: string[]): Number[] => {
    return lines.flatMap((line, index) => {
        const numberMatches = [...line.matchAll(/\d+/g)]
        return numberMatches.map(match => ({number: Number(match[0]), colIndexStart: match.index ?? 0, colIndexAfter: (match.index ?? 0) + match[0].length, rowIndex: index}))
    })
}

const symbols = getSymbols(lines)
const numbers = getNumbers(lines)

const symbolIndexWithNumberMap = new Map<string, Number[]>()

numbers.forEach((number) => {   
    const {rowIndex, colIndexStart, colIndexAfter} = number
    let symbolIndex = undefined

    if(symbols.get(rowIndex)?.get(colIndexStart - 1) === gearSymbol) {
        symbolIndex = `${rowIndex}-${colIndexStart - 1}`
    }  
    
    if(symbols.get(rowIndex)?.get(colIndexAfter) === gearSymbol) {
        symbolIndex = `${rowIndex}-${colIndexAfter}`
    }

    for(let i = colIndexStart - 1; i <= colIndexAfter; i++) {
        if(symbols.get(rowIndex - 1)?.get(i) === gearSymbol) {
            symbolIndex = `${rowIndex - 1}-${i}`
        }
            
        if(symbols.get(rowIndex + 1)?.get(i) === gearSymbol) {
            symbolIndex = `${rowIndex + 1}-${i}`
        }   
    }

    if(symbolIndex) {
        const numArr = symbolIndexWithNumberMap.get(symbolIndex) ?? []
        symbolIndexWithNumberMap.set(symbolIndex, numArr.concat(number))
    }

})

const sum = Array.from(symbolIndexWithNumberMap.values())
    .filter((arr) => arr.length === 2)
    .map((arr) => arr.reduce((partialSum, item) => partialSum * item.number, 1))
    .reduce((partialSum, item) => partialSum + item, 0)

console.log(sum)