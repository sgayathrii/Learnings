const vat = 0.2;
let total = 0;
let sum = 0;
let vatofsum = 0;
function sumofelement(arrVal){
    for (let x in arrVal)
    {
        sum += Number(arrVal[x]);
    }
     return sum;
}
function sumvattot(arrVal)
 {
    sum = sumofelement(arrVal);
    vatofsum = sum*vat;
    total = sum+vatofsum;
    console.log("Sum = "+ sum);
    console.log("VAT = "+vatofsum);
    console.log("Total = "+ total);
 }
 sumvattot(['1.20', '2.60', '3.50'])
 
 /* sumvattot(['3.12', '5', '18', '19.24', '1953.2262', 
 '0.001564', '1.1445']) */
