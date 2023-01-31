export class GameLogic
{
    constructor(game)
    {
    this.game = game;
    }

    mouseMoved(event)
    {
        this.game.player.x = event.offsetX;
        this.game.y = event.offsetY;
    }

    //mouse click inputs
    mouseClick(event)
    {
        //this part dictates the first 2 menus and starts the game + diff
        if(this.game.starter==true)
        {
            this.game.choice1=true;
            this.game.starter=false;
        }
        if (this.game.choice2 == true && this.game.y > 183 && this.game.y < 255)
        {
            this.game.diff = 1;
            this.game.choice2 = false;
            this.game.doneWithMenu=true;
        }
        else if (this.game.choice2 == true && this.game.y > 298 && this.game.y < 380)
        {
            this.game.diff = 2;
            this.game.choice2 = false;
            this.game.doneWithMenu=true;
        }
        //affor mentioned part ends here


        if (this.game.doneWithMenu == true)
        {
            if (this.game.player.x >= 50 && this.game.player.x <= 538)
            {
                this.game.score+=1
            }
            this.game.rectangle=true;

        }

    }

    mainGame()
    {
        if (this.game.doneWithMenu==true)
        {
            this.bossSec()
            this.cycles()
            this.beamCheck()
            this.colCheck()
            this.reset()
        }
        if(this.game.choice1==true)
        {
            this.game.wfc+=1
            if(this.game.wfc>=20)
            {
                this.game.choice2=true
                this.game.choice1=false
            }
        }
    }

    bossSec()
    {
        if(this.game.diff==1)
        {
            this.game.gcount+=1
        }
        else if(this.game.diff==2)
        {
            this.game.gcount+=2
        }
    }

    cycles()
    {
        //cycle1
        if(this.game.gcount>=0 && this.game.gcount <= 100)
        {
            if (this.game.cfa == 0)
            {
                this.game.beamx=Math.random()*600
                this.game.cfa+=1
            }
            this.game.warning=true;
        }
        if (this.game.gcount >= 100 && this.game.gcount <= 200)
        {
            this.game.cycle1=true;
            this.game.warning=false;
        }
        if (this.game.gcount >= 200)
        {
            this.game.cfa = 0;
            this.game.cycle1=false;
        }

        //cycloop
        if (this.game.gcount >= 300)
        {
            this.game.gcount = 0
            this.game.cycle3 = true;
            this.game.cycle2 = false;
            this.game.cycle1=false;
        }
    }



    colCheck()
    {
        //beam#1
        if (this.game.cycle1 == true
            && this.game.player.x <= (this.game.beamx + 50))
        {
            this.game.death13 = true;

        }

        if(this.game.score>=50)
        {
            this.game.endscreen1=true;
        }
    }

    

    beamCheck()
    {
        //So that beam disappears
        if (this.game.rectangle == true)
        {
            this.game.beam++
        }
        if (this.game.beam >= 50)
        {
            this.game.rectangle = false
            this.game.beam=0;
        }
        
    }

    reset()
    {
        if(this.game.endscreen1==true || this.game.death13==true)
        {
            this.game.dcount++
            if(this.game.dcount==200)
            {
                this.game.rectangle=false;
                this.game.starter=true;
                this.game.beam = 0;
                this.game.score=0;
                this.game.genc=0;
                this.game.gcount=0;
                this.game.dcount=0;
                this.game.endscreen1=false;
                this.game.res=false;
                this.game.death=false;
                this.game.boss=false;
                this.game.cycle1=false;
                this.game.cycle2=false;
                this.game.cycle3=false;
                this.game.end=false;
                this.game.control=false;
                this.game.choice1=false;
                this.game.choice2=false;
                this.game.warning=false;
                this.game.wfc=0;
                this.game.beamx=0;
                this.game.diff=0;
                this.game.cfa=0;
                this.game.death13=false;
                this.game.doneWithMenu=false;
            }
        }
    }

    logic()
    {
        this.mainGame()
    }

}