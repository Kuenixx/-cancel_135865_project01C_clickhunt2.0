from graphics import *
import random
import time



#Start Menu


class Gameplay:
    # Gameplay
    def menu(self):
        self.win = GraphWin("Click Hunt", 600, 600)
        self.win.setBackground("Black")
        startLine = Text(Point(300, 300), "Click Hunt 2.0\nClick to Start!")
        startLine.setFill("Green")
        startLine.draw(self.win)
        self.win.getMouse()
        startLine.undraw()

    def __init__(self):
        # Variable to count the amount of squares clicked
        self.menu()
        Sum = 0
        # Sets the timer
        Timer = 60
        TimerEnd = time.time() + Timer
        BackTime = Text(Point(300, 100), f"You have {Timer} seconds")
        BackTime.setFill("Green")
        BackTime.draw(self.win)

        # Background Text
        clickSquares = Text(Point(300, 50), "Click the Green Squares!")
        clickSquares.setFill("Green")
        clickSquares.draw(self.win)

        #Starts 60 second loop
        while time.time() < TimerEnd:
            Timer = int(TimerEnd - time.time())
            BackTime.undraw()
            BackTime = Text(Point(300, 100), f"You have {Timer} seconds")
            BackTime.setFill("Green")
            BackTime.draw(self.win)


            # Draw orange box
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
            # Check clickable size
            while MpositionX == MpositionY:
                MpositionX = random.randint(50, 550)
                MpositionY = random.randint(100, 550)
            Oposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
            OX = Oposition.getP1()
            OY = Oposition.getP2()
            Oposition.setFill(color_rgb(180, 90, 20))
            Oposition.draw(self.win)

            #Draw red box
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
            #Check clickable size
            while MpositionX == MpositionY:
                MpositionX = random.randint(50, 550)
                MpositionY = random.randint(100, 550)
            Rposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
            RX = Rposition.getP1()
            RY = Rposition.getP2()
            Rposition.setFill(color_rgb(120, 0, 0))
            Rposition.draw(self.win)



            #Draw green box
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
            # Check clickable size
            while MpositionX == MpositionY:
                MpositionX = random.randint(50, 550)
                MpositionY = random.randint(100, 550)
            Mposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
            MX = Mposition.getP1()
            MY = Mposition.getP2()
            Mposition.setFill(color_rgb(0, 120, 0))
            Mposition.draw(self.win)

            #for i in range(50):
                #Mposition.move(5,2)
                #update(50)
                #win.getMouse()

            # Green box location
            check = self.win.getMouse()
            CHECKX1 = check.getX() >= MX.getX()
            CHECKX2 = check.getX() <= MY.getX()
            CHECKY1 = check.getY() >= MX.getY()
            CHECKY2 = check.getY() <= MY.getY()
            CHECKX = CHECKX1 == CHECKX2
            CHECKY = CHECKY1 == CHECKY2

            #Red Box Location
            CHECKRX1 = check.getX() >= RX.getX()
            CHECKRX2 = check.getX() <= RY.getX()
            CHECKRY1 = check.getY() >= RX.getY()
            CHECKRY2 = check.getY() <= RY.getY()
            CHECKRX = CHECKRX1 == CHECKRX2
            CHECKRY = CHECKRY1 == CHECKRY2

            #Orange Box Location
            CHECKOX1 = check.getX() >= OX.getX()
            CHECKOX2 = check.getX() <= OY.getX()
            CHECKOY1 = check.getY() >= OX.getY()
            CHECKOY2 = check.getY() <= OY.getY()
            CHECKOX = CHECKOX1 == CHECKOX2
            CHECKOY = CHECKOY1 == CHECKOY2

            #Variables to loop getMouse
            Sum1 = Sum + 1
            Sum2 = Sum - 1
            # Square Spawner
            while Sum1 != Sum or Sum2 != Sum:

                if (CHECKX == True and CHECKY == True):
                    #Score Point
                    Sum = Sum + 1
                    break
                elif (CHECKRX == True and CHECKRY == True):
                    #Score -1 Point
                    Sum = Sum - 1
                    break
                elif (CHECKOX == True and CHECKOY == True):
                    #Gameover
                    TimerEnd=0
                    break
                else:
                    check = self.win.getMouse()
                    #Check Green box location
                    CHECKX1 = check.getX() >= MX.getX()
                    CHECKX2 = check.getX() <= MY.getX()
                    CHECKY1 = check.getY() >= MX.getY()
                    CHECKY2 = check.getY() <= MY.getY()
                    CHECKX = CHECKX1 == CHECKX2
                    CHECKY = CHECKY1 == CHECKY2
                    # Check Red box location
                    CHECKRX1 = check.getX() >= RX.getX()
                    CHECKRX2 = check.getX() <= RY.getX()
                    CHECKRY1 = check.getY() >= RX.getY()
                    CHECKRY2 = check.getY() <= RY.getY()
                    CHECKRX = CHECKRX1 == CHECKRX2
                    CHECKRY = CHECKRY1 == CHECKRY2
                    # Check Orange box location
                    CHECKOX1 = check.getX() >= OX.getX()
                    CHECKOX2 = check.getX() <= OY.getX()
                    CHECKOY1 = check.getY() >= OX.getY()
                    CHECKOY2 = check.getY() <= OY.getY()
                    CHECKOX = CHECKOX1 == CHECKOX2
                    CHECKOY = CHECKOY1 == CHECKOY2

            # Eliminates the squares
            Mposition.undraw()
            Rposition.undraw()
            Oposition.undraw()

        # Deletes the Text in the Background
        BackTime.undraw()
        # Undraws the background text to showcase Final Score
        clickSquares.undraw()
        # Shows Final Score:
        End = Text(Point(300, 300), f"Final Score:{Sum}")
        End.setFill("Green")
        End.draw(self.win)

        self.win.getMouse()
        self.win.close()
