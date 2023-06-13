import tkinter as tk
import random
cw = random.randrange(4,7)
ch = random.randrange(3,10)
pw = 50
ph = 50

root = tk.Tk()

canvas = tk.Canvas(width=cw*pw+100, height=ch*ph, bg='grey')
canvas.pack()
water= []
islands = []
img = tk.PhotoImage(file = "ostrov3.png")
img1 = tk.PhotoImage(file="ostrov0.png")
img2 = tk.PhotoImage(file="ostrov1.png")
img3 = tk.PhotoImage(file="ostrov2.png")
img4 = tk.PhotoImage(file="ostrov_kruh0.png")
img5 = tk.PhotoImage(file="ostrov_kruh1.png")
status = True
counter = 0



def update_point():
    global counter
    canvas.itemconfig(price, text=str(counter))


def changer(e):
    global water, counter
    print("klikol som")
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in water:
        print("klikol som a bola to voda")
        nx = (e.x // pw) * pw
        ny = (e.y // ph) * ph
        temp = zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        if status == True:
            # canvas.itemconfig(zoz[0], image=img1)
            canvas.create_image(nx,ny,anchor='nw',image=img1, tag = 'zem')
            counter += 20
            update_point()
        else:
            canvas.create_image(nx,ny,anchor='nw',image=img2, tag = 'bridge')
            counter += 10
            update_point()

def spinner(e):
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    print(canvas.itemcget(zoz[0],"image"))
    if canvas.itemcget(zoz[0], "image") == "pyimage3":
        canvas.itemconfig(zoz[0], image=img3)
    else:
        canvas.itemconfig(zoz[0], image=img2)
def swapper(e):
    global status
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    if status == True:
        canvas.itemconfig(zoz[0], image=img5)
        status = False
        return status
    else:
        canvas.itemconfig(zoz[0], image=img4)
        status = True
        return status


def setup():
    global water, islands
    for y in range(ch):
        for x in range(cw):
            result = random.random()
            if result <= 0.2:
                islands.append(canvas.create_image(pw*x,ph*y,anchor='nw',image=img1))

            else:
                water.append(canvas.create_image(pw * x, ph * y, anchor='nw', image=img))
    canvas.create_image(cw*pw+50,0,anchor = 'nw', image = img4,tags= 'switcher')


canvas.bind('<Button-1>',changer)
canvas.tag_bind('bridge',"<Button-1>",spinner)
canvas.tag_bind('switcher',"<Button-1>",swapper)
price = canvas.create_text(cw*pw+50,ch*ph-50, text = '0', font = ('Arial',40, 'bold'),fill = 'black')
setup()
root.mainloop()

# za dve jednotky predaj ostrovov a mostov
