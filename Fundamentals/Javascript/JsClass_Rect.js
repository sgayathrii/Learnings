class Rectangle{
    constructor(recWidth,recHeight,recColor){
        this.width= recWidth;
        this.height= recHeight;
        this.color= recColor;
    }
    calcArea()
    {
        let areaRec = this.width*this.height ;
        return areaRec;
    }
}
let rec = new Rectangle(4,5,"violet");
//document.writeln("Area of the Rectangele is: " + rec.calcArea());
console.log(rec.width);
console.log(rec.height);
console.log(rec.color);
console.log(rec.calcArea());

//console.log(`Area: ${rec.calcArea()}`);
