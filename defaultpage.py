#importing GUI tools needed
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from math import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os,sys
import subprocess


#creating a root window
window = Tk()

#using Python Image Library(PIL) to convert tablericos to tkinter images
from PIL import ImageTk
from pytablericons import TablerIcons,OutlineIcon,FilledIcon

def createIconImage(ICONNAME, size, color, stroke_width):
    """Creates an Outline Icon and converts it to an ImageTk object.
        ICONNAME: must be a usable icon name and all be in UPPERCASE e.g OutlineIcon.ALIGN_RIGHT.
        size(int): size of icon
        color(string): icon color
        srtoke_width(int)
        returns->
           ImageTk 

    """
    
    icon = TablerIcons.load(ICONNAME,size=size,color=color,stroke_width=stroke_width)
    tkIcon = ImageTk.PhotoImage(icon)
    return tkIcon

#giving a title (pypad)
window.title(f"pypad: opened")

#getting device's screen width and height in pixels
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

#setting the resolution of the window (width x height)
window.geometry(f"{screenwidth}x{screenheight}")

menuBar = Menu(window)
window.config(menu=menuBar,bg='#BCCCDC')

def saveFile(event=None):
    file_path = asksaveasfilename(
        initialdir=os.environ['USERPROFILE']+'\\Documents',
        title="Open file",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        print(f"file selected: {file_path}")
        file = open(file_path,'x')
        file.write(page.get("1.0","end-1c"))
        print('done writing to file')

    else:
        print("no file selected")

def openFile(event=None):
    readtext = ''
    file_path = askopenfilename(
        initialdir=os.environ['USERPROFILE']+'\\Documents',
        title="Open file",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        print(f"file selected: {file_path}")
        file = open(file_path,'r') #opening file object in read mode
        text_in_file = file.readlines() #reading text from file
        for line in text_in_file:
            readtext = readtext + line
        page.insert(readtext)
        page.update()
        #open defaultpage.py application
        try:
            s_process = subprocess.Popen(['python', 'defaultpage.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            output, error = s_process.communicate(input=readtext)
        except subprocess.CalledProcessError as e:
                print(f"Error running pytextEditor.py: {e}")
        except FileNotFoundError:
                print("pytextEditor.py not found in the current directory.")
        #Now write text to a page 
        
    else:
        print("no file selected")

fileMenu = Menu(menuBar)
menuBar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='SaveAs',command=saveFile)

#creating ribbon frame
ribbon_frame = Frame(window,bg='#F2F9FF',height=50,pady=10)
ribbon_frame.pack(fill='x')

#configuring grid columns
ribbon_frame.grid_columnconfigure(0,weight=1)
ribbon_frame.grid_columnconfigure(1,weight=2)
ribbon_frame.grid_columnconfigure(2,weight=2)
ribbon_frame.grid_columnconfigure(3,weight=2)
ribbon_frame.grid_columnconfigure(4,weight=2)
ribbon_frame.grid_columnconfigure(5,weight=2)

#creating subframes
file_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
clipboard_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
font_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
paragraph_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
insert_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
editing_frame = Frame(ribbon_frame,bg='#F2F9FF',height=80)
font_frame_sub = Frame(font_frame)


#creating subframe list
subframe_list = [file_frame,clipboard_frame,font_frame,paragraph_frame,insert_frame,editing_frame]

#images for paragraphing frame
alingLeftImage = createIconImage(OutlineIcon.ALIGN_LEFT,24,'black',1)
alignRightImage = createIconImage(OutlineIcon.ALIGN_RIGHT,24,'black',1)
alignCenterImage = createIconImage(OutlineIcon.ALIGN_CENTER,24,'black',1)
alignJustifyImage = createIconImage(OutlineIcon.ALIGN_JUSTIFIED,24,'black',1)
listImage = createIconImage(OutlineIcon.LIST,24,'black',1)
indentIncreaseImage = createIconImage(OutlineIcon.INDENT_INCREASE,24,'black',1)
indentDecreaseImage = createIconImage(OutlineIcon.INDENT_DECREASE,24,'black',1)
linespacingImage = createIconImage(OutlineIcon.LINE_HEIGHT,24,'black',1)
paragraphrow1Images = [indentDecreaseImage,indentIncreaseImage,linespacingImage,listImage]
paragraphrow2Images = [alingLeftImage,alignCenterImage,alignRightImage,alignJustifyImage]

#font frame images
boldImage = createIconImage(OutlineIcon.BOLD,24,'black',1)
italicImage = createIconImage(OutlineIcon.ITALIC,24,'black',1)
underlineImage = createIconImage(OutlineIcon.UNDERLINE,24,'black',1)
strikethroughImage = createIconImage(OutlineIcon.STRIKETHROUGH,24,'black',1)
superscriptImage = createIconImage(OutlineIcon.SUPERSCRIPT,24,'black',1)
subscriptImage = createIconImage(OutlineIcon.SUBSCRIPT,24,'black',1)
squareLetter_A = createIconImage(OutlineIcon.SQUARE_LETTER_A,24,'black',1)
dropdownImage = createIconImage(OutlineIcon.DROPLET_DOWN,24,'black',1)
fontFrameRow = [boldImage,italicImage,underlineImage,strikethroughImage,subscriptImage,superscriptImage]
#insertframe images
insPicImage = createIconImage(OutlineIcon.PHOTO_UP,24,'black',1)
insObjectImage = createIconImage(OutlineIcon.TRIANGLE_SQUARE_CIRCLE,24,'black',1)
insImagesRow = [insPicImage,insObjectImage]
#editingframe images
findImage = createIconImage(OutlineIcon.SEARCH,24,'black',1)
replaceImage = createIconImage(OutlineIcon.A_B_2,24,'black',1)
editImagesrow = [findImage,replaceImage]
#clipboardframe images
copyImage = createIconImage(OutlineIcon.COPY,24,'black',1)
pasteImage = createIconImage(OutlineIcon.CLIPBOARD_TEXT,24,'black',1)
cutImage = createIconImage(OutlineIcon.CUT,24,'black',1)
clipboardRow = [copyImage,pasteImage,cutImage]
#fileframe images
saveImage = createIconImage(OutlineIcon.DEVICE_FLOPPY,24,'blue',1)


def insertButton(master,image,row,col,padx,pady):
    """inserts a button widget within a particular subframe(master).
        params->
            master(Widget): parent widget
            image(tkImage): button image
            row(int): grid row number
            col(int): grid col number
    """
    button = Button(master=master,image=image,padx=padx,pady=pady)
    button.grid(row=row,column=col)



#displaying ribbon subframes
index = 0
for elem in subframe_list:
    elem.grid(row=0,column=index,sticky='nsew')
    index = index+1

#displaying font_frame_sub
font_frame_sub.grid(row=1)

row,col = 0,0
#inserting buttons in grids format within paragraph frame
for img in paragraphrow1Images:
    insertButton(paragraph_frame,image=img,row=0,col=col,padx=20,pady=5)
    col = col+1
col = 0 #reinitializing col
for img in paragraphrow2Images:
    insertButton(master=paragraph_frame,image=img,row=1,col=col,padx=20,pady=5)
    col = col+1
col = 0
#creating and displaying fonttypes and fontsize dropdowns
selectedFont = StringVar(font_frame)
selectedFontSize = IntVar(font_frame)
selectedFontSize.set(12)
selectedFont.set('Calibri')
fontDropdown = ttk.Combobox(font_frame,textvariable=selectedFont,values=font.families())
fontSizeDropdown = ttk.Combobox(font_frame,textvariable=selectedFontSize,values=list(range(1,73)),width=5)
def changeFont(event):
    page.config(font=(selectedFont.get(),selectedFontSize.get()))
    page.update()
def changeFontSize(event):
    page.config(font=(selectedFont.get(),selectedFontSize.get()))
    page.update()
def bold(event=None):
    try:
        data= page.selection_get()
        page.delete(SEL_FIRST,SEL_LAST)
        page.tag_configure('bold',font=('bold',selectedFontSize.get(),'bold'),foreground='black')
        page.insert(INSERT,data,'bold')
    except TclError:
        print("No text selected")
def italic(event=None):
    try:
        data= page.selection_get()
        page.delete(SEL_FIRST,SEL_LAST)
        page.tag_configure('italic',font=('italic',selectedFontSize.get(),'italic'),foreground='black')
        page.insert(INSERT,data,'italic')
    except TclError:
        print("No text selected")
def underline(event=None):
    try:
        data= page.selection_get()
        page.delete(SEL_FIRST,SEL_LAST)
        page.tag_configure('underline',font=('underline',selectedFontSize.get(),'underline'),foreground='black')
        page.insert(INSERT,data,'underline')
    except TclError:
        print("No text selected")
def strikethrough(event=None):
    try:
        data= page.selection_get()
        page.delete(SEL_FIRST,SEL_LAST)
        page.tag_configure('strikethrough',font=('strikethrough',selectedFontSize.get(),'normal'),foreground='black',overstrike=True)
        page.insert(INSERT,data,'strikethrough')
    except TclError:

        print("No text selected")
#displaying font_frame widgets
fontDropdown.grid(row=0,column=0)
fontSizeDropdown.grid(row=0,column=1)
fontDropdown.bind('<<ComboboxSelected>>',changeFont)
fontSizeDropdown.bind('<<ComboboxSelected>>',changeFontSize)
for img in fontFrameRow:
    insertButton(master=font_frame_sub,image=img,row=1,col=col,padx=20,pady=10)
    col = col+1
col = 0
for img in insImagesRow:
    insertButton(master=insert_frame,image=img,row=0,col=col,padx=20,pady=10)
    col = col+1
col = 0
for img in editImagesrow:
    insertButton(master=editing_frame,image=img,row=1,col=col,padx=20,pady=10)
    col = col+1

col = 0
for img in clipboardRow:
    insertButton(master=clipboard_frame,image=img,row=0,col=col,padx=20,pady=10)
    col = col+1

insertButton(master=file_frame,image=saveImage,row=0,col=0,padx=20,pady=10)





#creating a page for writing
pageFrame = Frame(window,bg='#fff',width=100,height=30)
pageFrame.pack(fill='y',expand=False)
pageFrame.pack(pady=20)
page = Text(pageFrame,
            background='#fff',
            foreground='black',
            height=30,
            width=100,
            font=(selectedFont,
            selectedFontSize.get()),
            )

vscroller = Scrollbar(pageFrame,orient='vertical',command=page)
xscroller = Scrollbar(pageFrame,orient='horizontal',command=page)
page.config(yscrollcommand=vscroller.set,xscrollcommand=xscroller.set)
vscroller.pack(side='right',fill='y')
page.insert('1.0',sys.stdin.read())
page.pack(side='left')
#binding events to page
page.bind("<Control-b>",bold)
page.bind("<Control-i>",italic)
page.bind("<Control-u>",underline)
page.bind("<Control-s>",saveFile)
page.bind("<Control-o>",openFile)
page.bind("<Control-x>",lambda event: page.event_generate("<<Cut>>"))


#adding commands to buttons


clipboard_frame.winfo_children()[0].config(command=lambda: page.event_generate("<<Copy>>"))
clipboard_frame.winfo_children()[1].config(command=lambda: page.event_generate("<<Paste>>"))
clipboard_frame.winfo_children()[2].config(command=lambda: page.event_generate("<<Cut>>"))
font_frame_sub.winfo_children()[0].config(command=bold)
font_frame_sub.winfo_children()[1].config(command=italic)
font_frame_sub.winfo_children()[2].config(command=underline)
font_frame_sub.winfo_children()[3].config(command=strikethrough)

window.mainloop()

