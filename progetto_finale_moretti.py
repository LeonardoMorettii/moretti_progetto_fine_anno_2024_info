import time
import turtle

# finestra di gioco
schermo = turtle.Screen()
schermo.title("Pong game")
schermo.bgcolor("black")
schermo.setup(width=800, height=600)
schermo.tracer(0)

# giocatore 1
giocatore_1 = turtle.Turtle()
giocatore_1.speed(0)
giocatore_1.shape("square")
giocatore_1.color("white")
giocatore_1.shapesize(stretch_wid=6, stretch_len=1)
giocatore_1.penup()
giocatore_1.goto(-350, 0)

# giocatore 2
giocatore_2 = turtle.Turtle()
giocatore_2.speed(0)
giocatore_2.shape("square")
giocatore_2.color("white")
giocatore_2.shapesize(stretch_wid=6, stretch_len=1)
giocatore_2.penup()
giocatore_2.goto(350, 0)

# palla
palla = turtle.Turtle()
palla.speed(40)
palla.shape("square")
palla.color("white")
palla.penup()
palla.goto(0, 0)
palla.dx = 0.2
palla.dy = -0.2

# punti
punti_a = 0
punti_b = 0

# tabella punteggio
tabella_punteggio = turtle.Turtle()
tabella_punteggio.speed(0)
tabella_punteggio.color("white")
tabella_punteggio.penup()
tabella_punteggio.hideturtle()
tabella_punteggio.goto(0, 260)
tabella_punteggio.write("giocatore 1: 0  giocatore 2: 0", align="center", font=("Courier", 24, "normal"))

# funzioni per il movimento dei giocatori
def giocatore_1_su():
    y = giocatore_1.ycor()
    if y < 250:
        y += 20
    giocatore_1.sety(y)

def giocatore_1_giù():
    y = giocatore_1.ycor()
    if y > -240:
        y -= 20
    giocatore_1.sety(y)

def giocatore_2_su():
    y = giocatore_2.ycor()
    if y < 250:
        y += 20
    giocatore_2.sety(y)

def giocatore_2_giù():
    y = giocatore_2.ycor()
    if y > -240:
        y -= 20
    giocatore_2.sety(y)

# tasti giocatori
schermo.listen()
schermo.onkeypress(giocatore_1_su, "w")
schermo.onkeypress(giocatore_1_giù, "s")
schermo.onkeypress(giocatore_2_su, "Up")
schermo.onkeypress(giocatore_2_giù, "Down")

# loop del gioco
while True:
    schermo.update()

    # Movimento palla
    palla.setx(palla.xcor() + palla.dx)
    palla.sety(palla.ycor() + palla.dy)

    # bordi
    if palla.ycor() > 290:
        palla.sety(290)
        palla.dy *= -1

    if palla.ycor() < -290:
        palla.sety(-290)
        palla.dy *= -1

    if palla.xcor() > 390:
        palla.goto(0, 0)
        palla.dx *= -1
        punti_a += 1
        tabella_punteggio.clear()
        tabella_punteggio.write("giocatore 1: {}  giocatore 2: {}".format(punti_a, punti_b), align="center", font=("Courier", 24, "normal"))

    if palla.xcor() < -390:
        palla.goto(0, 0)
        palla.dx *= -1
        punti_b += 1
        tabella_punteggio.clear()
        tabella_punteggio.write("giocatore 1: {}  giocatore 2: {}".format(punti_a, punti_b), align="center", font=("Courier", 24, "normal"))

    # rimbalzo palla e giocatori
    if (palla.dx > 0) and (350 > palla.xcor() > 340) and (giocatore_2.ycor() + 50 > palla.ycor() > giocatore_2.ycor() - 50):
        palla.setx(340)
        palla.dx *= -1

    if (palla.dx < 0) and (-350 < palla.xcor() < -340) and (giocatore_1.ycor() + 50 > palla.ycor() > giocatore_1.ycor() - 50):
        palla.setx(-340)
        palla.dx *= -1
        # controllo vittoria giocatori
        if punti_a == 10:
            tabella_punteggio.clear()
            tabella_punteggio.write("Giocatore 1 vince!", align="center", font=("Courier", 24, "normal"))
            schermo.update()
            time.sleep(3)
            schermo.bye()

        if punti_b == 10:
            tabella_punteggio.clear()
            tabella_punteggio.write("Giocatore 2 vince!", align="center", font=("Courier", 24, "normal"))
            schermo.update()
            time.sleep(3)
            schermo.bye()
