/* Checking if javascript imported */
console.log("begin");

/* Getting variables */
var circle = document.getElementById("circle");
var stop = document.getElementById("stop");
var can = document.getElementById("canvas");
var canvas = can.getContext("2d");
canvas.fillStyle = "#FFD1C1";

/* Setting variables */
var grow = true;
var x = can.width / 2;
var y = can.height / 2;
var r = 1;
var animation;

/* Animated Circle */
circle.addEventListener("click", function(){
    animation = setInterval(function(){
        console.log("circle!");
        canvas.clearRect(0, 0, 538, 538);
        canvas.beginPath();
        canvas.moveTo(x, y);
        canvas.arc(x, y, r, 0, 2*Math.PI);
        canvas.fill();
        canvas.closePath();
        if(grow){
            if(r<269){
                r++;
            } else{
                grow = false;
                r--;
            }
        } else{
            if(r>1){
                r--;
            } else{
                grow = true;
                r++;
            }
        }
    }, 5);
});

/* Stop button */
stop.addEventListener("click", function(){
    console.log("clear");
    clearInterval(animation);
});

/* Checking that program ran through file */
console.log("end");