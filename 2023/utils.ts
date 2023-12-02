import {readFileSync} from 'fs';

export const readInput = (filePath: string) => {
    const file =readFileSync(filePath,'utf8');
    return file.split('\r')
}