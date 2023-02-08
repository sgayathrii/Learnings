class Circle{
    constructor(radius)
     {
        this.radius = radius;
     }

     setDiameter(diameter)
     {
       console.log(diameter);
       this.radius = diameter/2;
     }
     
     getDiameter(){
        return this.radius*2;
     }
     areaofcircle(){
        const pi = 3.1415926535897932;
        let area = pi * Math.pow(this.radius,2);
        return area;
     }

 }
 let circle = new Circle(2);
 console.log(`Radius: ${circle.radius}`);
 console.log(`Diameter: ${circle.getDiameter()}`);
 console.log(`Area: ${circle.areaofcircle()}`);
 circle.setDiameter(1.6);
 console.log(`Radius: ${circle.radius}`);
 console.log(`Diameter: ${circle.getDiameter()}`);
 console.log(`Area: ${circle.areaofcircle()}`);