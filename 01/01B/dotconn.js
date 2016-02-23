/* Checking if javascript imported */
console.log("Begin");



/* Getting elements and setting variables */
var clear = document.getElementById("clear");
var increase = document.getElementById("increase");
var decrease = document.getElementById("decrease");
var pink = document.getElementById("pink");
var green = document.getElementById("green");
var blue = document.getElementById("blue");
var purple = document.getElementById("purple");
var playground = document.getElementById("playground");
var canvas = playground.getContext("2d");
var oldx = -1; // Variable for connecting the dots
var oldy = -1; // Variable for connecting the dots
var r = 4; // Variable for increasing and decreasing dot size
var color = "#FFD1C1";



/* INCREASING DOT SIZE */
increase.addEventListener("click", function(){
    if(r<12){
        r = r + 0.5;
        console.log("increase dot size");
        // Uncomment these to clear canvas when dot size changes
        //canvas.clearRect(0, 0, 538, 538);
        //oldx = -1;
        //oldy = -1;
    } else{
        console.log("max dot size reached");
    }
});
/* DECREASING DOT SIZE */
decrease.addEventListener("click", function(){
    if(r>2){
        r = r - 0.5;
        console.log("decrease dot size");
        // Uncomment these to clear canvas when dot size changes
        //canvas.clearRect(0, 0, 538, 538);
        //oldx = -1;
        //oldy = -1;
    } else{
        console.log("min dot size reached");
    }
});



/* CHANGE CHALK COLOR TO PINK */
pink.addEventListener("click", function(){
    color = "#FFD1C1";
});
/* CHANGE CHALK COLOR TO GREEN */
green.addEventListener("click", function(){
    color = "#CAFFB0";
});
/* CHANGE CHALK COLOR TO BLUE */
blue.addEventListener("click", function(){
    color = "#D6E4FF";
});
/* CHANGE CHALK COLOR TO PURPLE */
purple.addEventListener("click", function(){
    color = "#EAD5FF"; 
});



/* CLEARING CANVAS */
clear.addEventListener("click", function(){
    // Clear out a rectangle in the canvas (or in this case the entire canvas)
    canvas.clearRect(0, 0, 538, 538);
    // Next dot IS the first dot
    oldx = -1;
    oldy = -1;
    console.log("clear!");
});



/* ADDING AND CONNECTING DOTS */
playground.addEventListener("click", function(){
    var rect = playground.getBoundingClientRect(); // Dimensions of canvas
    var x = event.clientX - rect.left; // To account for coordinates in canvas, not of entire document
    var y = event.clientY - rect.top;  // To account for coordinates in canvas, not of entire document
    console.log(x + "," + y);

    if (oldx != -1 && oldy != -1){ // If this is not the first dot, connect the dots by their centers
        canvas.beginPath();
        canvas.moveTo(oldx, oldy);
        canvas.lineTo(x, y);
        canvas.stroke();
        canvas.closePath();
    }
    
    // Make a dot
    canvas.fillStyle = color;
    canvas.strokeStyle = color;
    canvas.beginPath();
    canvas.moveTo(x, y);
    canvas.arc(x, y, r, 0, 2*Math.PI);
    canvas.fill();
    canvas.closePath();
    
    // Update oldx and oldy to say that the next dot is NOT the first dot
    oldx = x;
    oldy = y;
    console.log("dot!");
});



/* Checking that file ran smoothly */
console.log("End");
