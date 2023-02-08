let width_height = ['2', '4', '5', '3']
let area = 0;
let figureArea = 0;
let minWidth = minHeight = 0;

function areaoffigure(width_height)
{
        let w = Number(width_height[0]);
        let h = Number(width_height[1]);
        let W = Number(width_height[2]);
        let H = Number(width_height[3]);          
        area =  (w*h)+(W*H);
        minWidth = Math.min(w,W);
        minHeigth = Math.min(h,H);
        figureArea = area -(minWidth*minHeigth);
        console.log("["+width_height +"]" +"  " +figureArea);     
}
areaoffigure(width_height);





/*
    var input = ['2', '4', '5', '3'];
    function figure(input){

    var w = Number(input[0]);

    var h = Number(input[1]);

    var W = Number(input[2]);

    var H = Number(input[3]);

   

    var rect_A = H*(W-w);

    var rect_B = w*h;

   

    var Area = rect_A + rect_B;

    console.log(Area);

}

figure(input);*/