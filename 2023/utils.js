"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.readInput = void 0;
const fs_1 = require("fs");
const readInput = (filePath) => {
    const file = (0, fs_1.readFileSync)(filePath, 'utf8');
    return file.split('\n');
};
exports.readInput = readInput;
