class Person{
    static personInfo = [];
    constructor(firstname,lastname=" ",age=" ",email=" "){
        this.firstname= firstname;
        this.lastname= lastname;
        this.age = age;
        this.email = email;
        Person.personInfo.push(this);

        }
                  
                
    }
let person1 = new Person('Maria', 'Petterson', 22, 'mp@gmail.com')
let person2 = new Person('Lexicon')
let person3 = new Person('Stefan', 'Larsson', 28)
let person4 = new Person('Peter', 'Jansson', 24, 'ptr@live.com')
console.table(Person.personInfo);





