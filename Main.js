let input = require('fs').readFileSync("ex.txt").toString().split("\n");

let N = parseInt(input[0])

input.shift();

input = new Set(input);
input = Array.from(input);

let result = ""

input.sort((a, b) => {
  let aLength = a.trim().length;
  let bLength = b.trim().length;

  if(aLength != bLength){
      if(aLength > bLength){
        return 1;
      }
      else if(aLength < bLength){
        return -1;
      }
  }

  for(let i=0; i<aLength; i++){
    if(a.charAt(i) > b.charAt(i)){
      return 1;
    }
    else if(a.charAt(i) < b.charAt(i)){
      return -1;
    }
  }    
}).forEach(input => {
  result += input.replace("\r","");
});

console.log(result.trim()+result.length);
