let coordinates = ['2', '4', '5', '0'];
let x_coor = 0;
let y_coor = 0;
let distance = 0;
function calcoordinates(coordinates) {
    x_coor = Math.pow((coordinates[2]-coordinates[0]),2);
    y_coor = Math.pow((coordinates[3]-coordinates[1]),2);
    distance = Math.sqrt((x_coor+y_coor));
    console.table({[coordinates]: distance})
}  
calcoordinates(coordinates);
