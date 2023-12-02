import { readInput } from "../utils";

type CubeColor = 'red' | 'green' | 'blue'
type Cube = {
    [key in CubeColor]: number;
};

const cube: Cube = {
    red: 12,
    green: 13,
    blue: 14
}

const cubeColors = Object.keys(cube)


const lines = readInput("day2/input.txt") 

const validateCubeNumber = (numberOfCubes: number, cubeColor: CubeColor) => {
    if(isNaN(numberOfCubes) || !cubeColors.includes(cubeColor)) {
        return false;
    }

    return numberOfCubes <= cube[cubeColor]
}

const validateGameSet = (gameSet: string) => {
    const cubesDrawn = gameSet.split(', ').map((cube) => cube.split(' '))
    
    return cubesDrawn.every((cube) => validateCubeNumber(Number(cube[0]), cube[1] as CubeColor))
}

const validGameIds = lines.map((line) => {
    const row = line.split(': ')
    const gameId = Number(row[0].replace(/\D/g, ''))
    const gameSets = row[1].split('; ')

    const isValid = gameSets.every((gameSet) => validateGameSet(gameSet))

    return isValid ? gameId : undefined
})

const sum = validGameIds.reduce((partialSum, a) => (partialSum ?? 0) + (a ?? 0), 0)

console.log(sum)