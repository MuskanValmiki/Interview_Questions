var number = [2, 4, 6, 8, 12, 14];
 
// Normal Way
var sum = number.reduce(function(total, element){
   return total + element;
})
console.log(sum);
 
// es6 way
var sum = number.reduce((total, value) => total + value)
console.log(sum);
