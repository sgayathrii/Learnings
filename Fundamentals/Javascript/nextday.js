const dateinput = ['2016', '9', '30'];
let dd = dateinput[2];
let mm = dateinput[1];
let yy = dateinput[0];
const d = 86400000;
let datenow = new Date(dateinput);
let nowdate = datenow.getMilliseconds();
//datenow.setDate(datenow.getDate() + 2);
//console.log(datenow.toLocaleDateString());
datenow.setMilliseconds(datenow.getMilliseconds()+ 86400000);
console.log(datenow.toLocaleDateString());



/* syntax shared by Sowjanya
var date = new Date(year, month - 1, day);
var oneDay = 24 * 60 * 60 * 1000;//86 400 000 milliseconds in one day
var nextDate = new Date(date.getTime() + oneDay); */








