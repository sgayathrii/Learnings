class PointDistance{
        constructor (XCoordinate, YCoordinate){
            this.XCoordinate = XCoordinate;
            this.YCoordinate = YCoordinate;
            
        }
            
        static distance(x,y){
            let x_coor = Math.pow((x.XCoordinate-y.XCoordinate),2);
            let y_coor = Math.pow((x.YCoordinate-y.YCoordinate),2);
            let distance = Math.sqrt((x_coor+y_coor));
            return distance;
        }         
}

let p1 = new PointDistance(5,5);
let p2 = new PointDistance(9,8);
console.log(PointDistance.distance(p1,p2));
