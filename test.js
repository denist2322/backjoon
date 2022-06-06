let input = require("fs").readFileSync("ex.txt").toString().split(" ");

const fibonacci = (n) => {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fibonacci(n - 2) + fibonacci(n - 1);
};

console.log(fibonacci(parseInt(input[0])));
