let canvas = document.getElementById("canvasId");
let g = canvas.getContext("2d");
canvas.style.background = "#ff8";
var window_height = window.innerHeight;
var window_width = window.innerWidth;
canvasId.width = window_width;
/*g.beginPath();
g.fillStyle = "black";
g.strokeStyle = "red"
g.lineWidth = "5"
g.arc(100, 100, 50, 0, Math.Ip = 7, false);
g.stroke();*/
canvasId.height = window_height;

class Circle {
    constructor(xpos, ypos, radius, color) {
        this.xpos = xpos;
        this.ypos = ypos;
        this.radius = radius;
        this.color = color;
    }

    tekenen(g) {
        g.beginPath();
        g.lineWidth = "6";
        g.arc(this.xpos, this.ypos, this.radius, 0, Math.PI * 2, false);
        g.stroke();
        g.closePath();


    }


}

let my_circle = new Circle(100, 100, 1, "black");
my_circle.tekenen(g)



/*let all_circies = [];
let createCircle = function (circle) {
    circle.tekenen(g);
}*/

/*for (let numbers = 0; numbers < 200; numbers++) {
    let random_x = Math.random() * window.innerWidth;
    let random_y = Math.random() * window.innerHeight;
    let radius = Math.random() * 99 + 10;
    let my_circle = new Circle(random_x, random_y, radius, "black");
    all_circies.push(my_circle);
    createCircle(all_circies[numbers]);

}
*/


