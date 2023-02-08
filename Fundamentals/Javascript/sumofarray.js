let sum = 0;
function sumArr1(array1)
    {
    for(let num in array1)
    {
        var num1 = Number(array1[0]);
        var num2 = Number(array1[1]);
        var num3 = Number(array1[2]);
        sum = num1+num2+num3;
        
    }
    console.log(sum);
    }
    sumArr1(['1.5','1.5','-1'])
    //sumArr1(['2','3','4'])