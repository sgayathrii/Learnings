const personAge = {minAge:'12', name1:'John', age1:'15', name2:'Alfred', age2: '9'};
function findAge(personAge)
{
          
     if (personAge.age1 >= personAge.minAge)
       {
         console.log(personAge.age1);
         console.log("Name: " + personAge['name1'] + " , " + "Age: " + personAge.age1);
       }
       else if (personAge.age2 >= personAge.minAge)
       {
         console.log("Name: " + personAge['name2'] + " , " + "Age: " + personAge.age2);
       }
       else
       {
         return;
       }
}

findAge(personAge);