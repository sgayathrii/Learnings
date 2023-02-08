class Person{
    constructor(firstName,lastName,age,email){
        this.firstName= firstName;
        this.lastName= lastName;
        this.age = age;
        this.email = email;
        this.toString = function(){
            //return this.fname +" "+this.lname +" "+ "(age: "+ this.age +", email: "+this.email +")"
            //Apt way
            return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
        }

        }
    }

let personDetail = new Person('Maria', 'Petterson', 22, 'mp@gmail.com')
console.log(personDetail.toString());

//Other Way
//console.log(''+personDetail);


