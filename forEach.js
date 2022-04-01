const myMarks= [1,4,6,8,10]
 
//traditional way
for(var i=0;i<myMarks.length;i++){
   console.log(myMarks[i])
}
console.log('-------------------------');
 
//by forEach method and arrow function inside it
myMarks.forEach((e) => console.log(e))
 
 
//by forEach method and normal function inside it
myMarks.forEach(function(e){
   console.log(e)
});
