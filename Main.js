let input = require("fs").readFileSync("ex.txt").toString().trim().split("\n");

let NM = input[0].split(" ").map(Number);
input.shift();

let whoIs = new Object();
names = [];
result = [];
cnt = 0;

for (let i = 0; i < NM[0]; i++) {
 whoIs[input[i].trim()] = 1;
}

for (let j = NM[0]; j < NM[0] + NM[1]; j++) {
 names.push(input[j].toString().trim());
}

for (let val of names) {
 if (whoIs[val] > 0) {
  cnt++;
  result.push(val);
 }
}
console.log(cnt);
console.log(result.sort((a, b) => a - b).join("\n"));
