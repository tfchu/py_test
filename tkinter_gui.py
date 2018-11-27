'''
http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
https://www.geeksforgeeks.org/python-gui-tkinter/
https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-loop-with-lambda
get row number
    https://stackoverflow.com/questions/32612084/getting-the-row-of-a-tkinter-button-in-grid-on-click
"default keyword parameter" trick
    https://stackoverflow.com/questions/7299955/tkinter-binding-a-function-with-arguments-to-a-widget
    https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-loop-with-lambda
'''
import tkinter

root = tkinter.Tk()

def handle_click(text):
    print(text)

def handle_click2(event):
    print(event.widget['text'])  # or event.widget.cget('text')

def get_row(row):
    print("row: {}\n".format(row))

for r in range(3):
    for c in range(6):
        text = 'R%s/C%s' % (r, c)
        if c == 5:
            # 1. print widget text. note: text=text is "default keyword parameter" trick
            #button = tkinter.Button(root, text=text, command=lambda text=text: handle_click(text)) 
            # 2. get row number
            button = tkinter.Button(root, text=text, command=lambda row=r: get_row(row))            
            button.grid(row=r, column=c)   
        else:
            label = tkinter.Label(root, text=text, borderwidth=1)
            label.grid(row=r, column=c)
            # 1. print widget text (both ok). note. text=text is "default keyword parameter" trick, usage is different
            #label.bind("<Button-1>", lambda e, text=text: handle_click(text))  
            #label.bind("<Button-1>", handle_click2)
            # 2. get row number
            label.bind("<Button-1>", lambda e, row=r: get_row(row))             

root.mainloop()
