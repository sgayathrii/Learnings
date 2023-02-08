let count=0;
function letterinStr(str1){
for(let x in str1.word)
{
    if(str1.word[x]== str1.letter)
         {
            count++;
         }
 }
 console.log(str1.word +" , " + str1.letter + " " + " : " + count);
}
letterinStr({word:"Hello", letter:"H"})




