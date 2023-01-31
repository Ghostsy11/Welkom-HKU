import { Rect } from "./rect.js";

export class GameRenderer{
    constructor(game)
    {
        this. game = game
        this. canvas = document.getElementById("canvas");
        this. g = canvas.getContext("2d");
        this.images = []
        this.playerSprite = new Rect(87, 17, 175, 109);
        this.enemySprite = new Rect(24, 25, 129, 57);
        this.StartScreen = new Rect(0, 0, 800, 400);
        this.enemybeam= new Rect (40, 50, 85, 187)
        this.warningMarkRender= new Rect(656, 79, 619, 1756)
        this.score1_ = new Rect(0, 0, 434, 190)
        this.lose=new Rect(0, 0, this.canvas.clientWidth, this.canvas.clientHeight)
    }   

    loadImages()
    {
        let sources = ["game/img/space_enemy.png", "game/img/player.png", "game/img/StartScreen.png",
        "game/img/beam.png", "game/img/score1.png", "game/img/score2.png", "game/img/endscreen.png",
        "game/img/diffscreen.png", "game/img/warning.jpg", "game/img/lose.png"];
        for (let i = 0; i < sources.length; i++)
        {
            let loaded = 0
            let img = new Image;
            let scope = this

            img.onload = function()
            {   
                if (this.loaded == sources.length)
                {
                scope.game.startGame()
                }
                this.loaded++;
                scope.game.startGame()

            };
            img.src = sources[i];

            this.images.push(img)
        }
    }


    render()
    {
        let g = this.g
        g.fillStyle = "#000000";
        g.fillRect(0, 0, this.canvas.clientWidth, this.canvas.clientHeight);

        this.renderStart()


        if (this.game.doneWithMenu==true)
        {
            this.renderScore()
            this.renderBoss()
            this.renderPlayer()
            this.renderEnd()
        }
    }

    renderStart()
    {
        if (this.game.starter==true)
        {
            this.g.fillStyle = "#000000";
            let sscreen = this.game.sscreen;
            let clip2 = this.StartScreen;
            this.g.drawImage(this.images[2], 
                clip2.x, clip2.y, clip2.w, clip2.h, 
                sscreen.x, sscreen.y, sscreen.w, sscreen.h)
        }   
        

        if (this.game.choice2 == true)
        {
            let sscreen = this.game.sscreen;
            let clip2 = this.StartScreen;
            this.g.drawImage(this.images[7], 
                clip2.x, clip2.y, clip2.w, clip2.h, 
                sscreen.x, sscreen.y, sscreen.w, sscreen.h)
        }
    }

    renderScore()
    {
        //score
        if (this.game.score <= 100)
        {
            this.g.fillStyle = "#008000";
            let sb = this.game.s1;
            let clipS = this.score1_;
            this.g.drawImage(this.images[4], 
                clipS.x, clipS.y, clipS.w, clipS.h, 
                sb.x, sb.y, sb.w, sb.h)
        }
        else if (this.game.score >= 100)
        {
            this.g.fillStyle = "#008000";
            let sb = this.game.s1;
            let clipS = this.score1_;
            this.g.drawImage(this.images[5], 
                clipS.x, clipS.y, clipS.w, clipS.h, 
                sb.x, sb.y, sb.w, sb.h)
        }
    }

    renderBoss()
    {

        //boss
        this.g.fillStyle = "#008000";
        let enemy = this.game.enemy;
        let clip1 = this.enemySprite;
        this.g.drawImage(this.images[0], 
            clip1.x, clip1.y, clip1.w, clip1.h, 
            enemy.x, 20, enemy.w, enemy.h)

        //boss beam
        if(this.game.warning==true)
        {
            this.g.fillStyle = "#008000";
            let beam = this.game.warningMark;
            let clip3 = this.warningMarkRender;
            this.g.drawImage(this.images[8], 
                clip3.x, clip3.y, clip3.w, clip3.h, 
                this.game.beamx, beam.y, beam.w, beam.h)
            console.log("jdkjsjg")
        }
        //cycle 1
        if(this.game.cycle1 == true)
        {
            this.g.fillStyle = "#008000";
            let beam = this.game.enemyBeam;
            let clip3 = this.enemybeam;
            this.g.drawImage(this.images[3], 
                clip3.x, clip3.y, clip3.w, clip3.h, 
                this.game.beamx, beam.y, beam.w, beam.h)
        }
    }

    renderPlayer()
    {
        //player
        this.g.fillStyle = "#357CF1";
        let player = this.game.player;
        let clip = this.playerSprite;
        this.g.drawImage(this.images[1], 
            clip.x, clip.y, clip.w, clip.h, 
            player.x, 275, player.w, player.h)

        //player beam attack
        if (this.game.rectangle == true) 
        { 
            this.g.fillstyle = "#357CF1"
            this.g.fillRect(this.game.player.x, 200, 10, 100)
        }
    }

    renderEnd()
    {
        //end screen
        if (this.game.death13 == true)
        {
            this.g.fillStyle = "#000000";
            let sscreen = this.game.sscreen;
            let clip2 = this.StartScreen;
            this.g.drawImage(this.images[9], 
            clip2.x, clip2.y, clip2.w, clip2.h, 
            sscreen.x, sscreen.y, sscreen.w, sscreen.h)
        }
        if (this.game.endscreen1==true)
        {
            this.g.fillStyle = "#000000";
            let sscreen = this.game.loseEnding;
            let clip2 = this.lose;
            this.g.drawImage(this.images[6], 
            clip2.x, clip2.y, clip2.w, clip2.h, 
            sscreen.x, sscreen.y, this.canvas.clientWidth, this.canvas.clientHeight)
        }
    }

}

//#1
//{      
