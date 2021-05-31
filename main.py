from tkinter import *
import time
from random import randint
from tkinter import messagebox

REPEAT=0

window= Tk()
window.title('Typing Test')
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)



label=Label(text="Typing Test",font=('Courier',25,'bold'))
label.config(fg="BLUE")
label.grid(row=0,column=1,padx=50, pady=10)
guide_canvas=Canvas(width=500, height=100,highlightthickness=0)
guide=guide_canvas.create_text(250,40,text="Type text here\n+1 for Correct Letter\n -1 for 3 incorrect letter positions",font=('Courier',13,'bold'), fill='BROWN')
guide_canvas.grid(row=1,column=1)

input=Text(height=5, width=30)
input.focus()
input.grid(row=2, column=0, columnspan=4)

canvas=Canvas(width=100, height=140,highlightthickness=0)
timer_text=canvas.create_text(50,70,text="00:15",fill='black', font=('Courier',25,'bold'))
canvas.grid(row=3,column=1)

arr=['But let me warn you—it is really, really hard watching so much taxpayer cash\n wastefully go up in flames, especially when the travesty unfolds so slowly.','How religiously, if only in order to obviate neighbourly interference,\n the Darcian woman would observe contraceptive precautions!','Nitpick toward others is equal to dishonoring them, which is equal to yourself,\n and then you can not get happiness from it.','Many consultants like to tout that they have good guanxi and\n can arrange meetings with powerful officials to grease the wheels of commerce.', 'Throughout the passage, Ahab stands on the deck as if transfixed, staring\n blindly ahead into the wind and sleet.']

def begin():
    reset.config(text=' Done ')
    reset.grid(row=4, column=1)
    global REPEAT
    global count_sec
    count_sec=15
    num = randint(0, len(arr) - 1)
    canvas.itemconfig(timer_text, text=f"00:15")
    printing(count_sec)
    if REPEAT>=1:
        guide_canvas.itemconfig(timer_text, text=" ", font=('Arial', 10), fill='black')
        input.configure(state="disabled")
        Label( text=f"Restart application with new text", font=('Arial', 15), fg='black').grid(row=2, column=0, columnspan=4)
    REPEAT+=1

def printing(count):
    global REPEAT
    score=0
    guide_canvas.itemconfig(timer_text, text=f"{arr[num]}", font=('Arial', 10), fill='black')
    input_text = input.get("1.0", END)
    if REPEAT<=1:
        if count>=10:
            canvas.itemconfig(timer_text, text=f"00:{count}")
        elif 10>count>0:
            canvas.itemconfig(timer_text, text=f"00:0{count}")
        else:
            input.configure(state="disabled")
            for i in range(len(input_text)):
                if input_text[i] == arr[num][i]:
                    score += 10
                if input_text[i] != arr[num][i]:
                    score -= 3
            canvas.itemconfig(timer_text, text=f"Score: {float(score/10)}", font=('Arial', 11))
            Label(text=f"Restart application with new text", font=('Arial', 15), fg='black').grid(row=2, column=0,
                                                                                                  columnspan=4)
            reset.config(text=' Thank you\n\n❤Shubhrima ', fg='red')
            reset.grid(row=4, column=1)

        timer = window.after(1000, printing, count - 1)
    else:
        guide_canvas.itemconfig(timer_text, text=" ", font=('Arial', 10), fill='black')
        for i in range(len(input_text)):
            if input_text[i]==arr[num][i]:
                score+=10
            if input_text[i] != arr[num][i]:
                score-=3
        canvas.itemconfig(timer_text, text=f"Score: {float(score/10)}", font=('Arial', 11))
        reset.config(text=' Thank you\n\n❤Shubhrima ', fg='red')
        reset.grid(row=4, column=1)



num=randint(0, len(arr)-1)
reset=Button(text=' Begin ',width=35, height=5, fg='green', command= begin)
reset.grid(row=2,column=1)

window.mainloop()

