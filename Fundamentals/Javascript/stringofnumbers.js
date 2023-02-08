let concatnum = ['11'];
let stringnum = [];
function numadd(concatnum){
    for(let x of concatnum)
      {
        for(i=0;i<=x;i++){
            stringnum += i;
            }
      }
      console.log("'"+stringnum+"'");
}
numadd(concatnum);