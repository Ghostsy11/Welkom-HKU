import {GameRenderer} from "./gameRenderer.js"
import {GameLogic} from "./gameLogic.js"
import {Rect} from "./rect.js"  
class Game
{
    constructor()
    {
        this.logic = new GameLogic(this);
        this.renderer = new GameRenderer(this);
        this.x = 0;
        this.y = 0;
        this.rectangle=false;
        this.starter=true;
        this.beam = 0;
        this.score=0;
        this.genc=0;
        this.gcount=0;
        this.dcount=0;
        this.endscreen1=false;
        this.res=false;
        this.death=true;
        this.boss=false;
        this.cycle1=false;
        this.cycle2=false;
        this.cycle3=false;
        this.end=false;
        this.control=false;
        this.choice1=false;
        this.choice2=false;
        this.warning=false;
        this.wfc=0;
        this.beamx=0;
        this.diff=0;
        this.cfa=0;
        this.death13=false;
        this.doneWithMenu=false;
        this.player = new Rect(0, 0, 24, 24)
        this.warningMark = new Rect(0, 230, 40, 80)
        this.enemy=new Rect(200, 50, 350, 100)
        this.sscreen=new Rect(0, 0, 800, 400)
        this.enemyBeam= new Rect (40, 120, 76, 190)
        this.s1 = new Rect(200, 250, 434, 190)
        this.loseEnding=new Rect(0, 0, 800, 400)
    }

    init()
    {
        this.renderer.loadImages();
    }
    startGame()
    {
        let scope = this;
        
        this.renderer.canvas.addEventListener("mousemove", function(event) 
        {
            scope.logic.mouseMoved(event)
        })
        let _this = this;

        this.renderer.canvas.addEventListener('click', canvasClicked, false);
        function canvasClicked(event) 
        {
            scope.logic.mouseClick(event);  
             
        }
        this.cycle1 = false;
        console.log(this.end)
        setInterval(function () {scope.doGameFrame()}, 33); 
    }

    doGameFrame()
    {
        this.logic.logic();
        this.renderer.render();
    }
}

let game = new Game()
game.init();