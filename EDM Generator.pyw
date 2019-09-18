import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#functions
class input:

    def __init__(self, index, r):
        self.r = r
        self.icon = tk.StringVar()
        self.iconBox = ttk.Entry(win, width=20, textvariable=self.icon)
        self.iconBox.grid(column=1, row=self.r)
        self.link = tk.StringVar()
        self.linkBox = ttk.Entry(win, width=20, textvariable=self.link)
        self.linkBox.grid(column=2, row=self.r, padx=5)

    def generate():
        templateCategory = categoryVar.get()
        headerText = headerTextVar.get()
        if templateCategory == "Baby":
            filename = "baby_keyword_insert.html"
            tracking = "2026422408"
        elif templateCategory == "Beauty":
            filename = "beauty_keyword_insert.html"
            tracking = "2026422381"
        elif templateCategory == "Digital":
            filename = "digital_keyword_insert.html"
            tracking = "2026422390"
        elif templateCategory == "Fashion":
            filename = "fashion_keyword_insert.html"
            tracking = "2026422372"
        elif templateCategory == "Food":
            filename = "food_keyword_insert.html"
            tracking = "2026422426"
        elif templateCategory == "Living":
            filename = "living_keyword_insert.html"
            tracking = "2026422417"
        elif templateCategory == "Sports":
            filename = "sports_keyword_insert.html"
            tracking = "2026422435"
        
        try:
            fileExist = open(filename, "r")
            if messagebox.askokcancel("Error - Existing file for " + templateCategory + " detected!", "Do you wish to overwrite existing file?"):
                createInsert(templateCategory, filename, tracking, headerText)
            else:
                pass
        except:
            createInsert(templateCategory, filename, tracking, headerText)

    def clear(self):
        self.iconBox.delete(0, 'end')
        self.linkBox.delete(0, 'end')

def delete():
    one.iconBox.delete(0, 'end')
    one.linkBox.delete(0, 'end')

    two.iconBox.delete(0, 'end')
    two.linkBox.delete(0, 'end')

    three.iconBox.delete(0, 'end')
    three.linkBox.delete(0, 'end')

    four.iconBox.delete(0, 'end')
    four.linkBox.delete(0, 'end')

    five.iconBox.delete(0, 'end')
    five.linkBox.delete(0, 'end')

    six.iconBox.delete(0, 'end')
    six.linkBox.delete(0, 'end')

    seven.iconBox.delete(0, 'end')
    seven.linkBox.delete(0, 'end')

def createInsert(templateCategory, filename, tracking, headerText):

    keywordArray = []

    keywordArray.append([one.icon.get(), one.link.get()])
    keywordArray.append([two.icon.get(), two.link.get()])
    keywordArray.append([three.icon.get(), three.link.get()])
    keywordArray.append([four.icon.get(), four.link.get()])
    keywordArray.append([five.icon.get(), five.link.get()])
    keywordArray.append([six.icon.get(), six.link.get()])
    keywordArray.append([seven.icon.get(), seven.link.get()])

    html = open(filename, "w")
    html.write('<table width="740" border="0" align="center" cellpadding="0" cellspacing="0">\n')
    html.write('    <tr>\n')
    html.write('        <td colspan="4" style="font-family: Gotham, Helvetica Neue, Helvetica, Arial, sans-serif; text-align: center; color: #000000; font-size: 26px; text-transform: uppercase; padding: 25px 0px 10px;">' + headerText + '</td>\n')
    html.write('    </tr>\n')
    
    for i in range(2):
        html.write('    <tr>\n')
        if i == 0:
            html.write('        <td rowspan="2"><a href="' + keywordArray[0][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[0][0] + '" width="185" alt=""></a></td>\n')
            html.write('        <td><a href="' + keywordArray[i+1][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+1][0] + '" width="185" alt=""></a></td>\n')
            html.write('        <td><a href="' + keywordArray[i+2][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+2][0] + '" width="185" alt=""></a></td>\n')
            html.write('        <td><a href="' + keywordArray[i+3][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+3][0] + '" width="185" alt=""></a></td>\n')
        else:
            html.write('        <td><a href="' + keywordArray[i+3][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+3][0] + '" width="185" alt=""></a></td>\n')
            html.write('        <td><a href="' + keywordArray[i+4][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+4][0] + '" width="185" alt=""></a></td>\n')
            html.write('        <td><a href="' + keywordArray[i+5][1] + '?jaehuid=' + tracking + '" target="_blank"><img src="' + keywordArray[i+5][0] + '" width="185" alt=""></a></td>\n')
        html.write('    </tr>\n')
    html.write('</table>\n')
    html.close()

    messagebox.showinfo("Success!", "EDM insert for " + templateCategory + " created!")

#GUI
win = tk.Tk()
win.title("Keyword EDM Generator")
win.resizable(False, False)
# win.iconbitmap(r'..\icon.ico')

### Notebook ###
nb = ttk.Notebook(win)
nb.grid(row=2, column=0, pady=(5,0), padx=(1,0), sticky='NSEW')

## Input tab ##
win = ttk.Frame(nb)
nb.add(win, text="Main")

## Help Tab ##
guide = ttk.Frame(nb)
nb.add(guide, text="Help")

helpMsg = "No help yet....\n\n Keyword EDM Insert Generator by Gregory"
helpLabel = tk.Message(guide, text=helpMsg, width=500)
helpLabel.grid(row=0, column=0)

#Header labels
templateLabel = ttk.Label(win, text="Template Category")
templateLabel.grid(column=1, row=0)

headerTextLabel = ttk.Label(win, text="Header Text")
headerTextLabel.grid(column=1, row=1)

iconLabel = ttk.Label(win, text="Icon URL")
iconLabel.grid(column=1, row=3)

linkLabel = ttk.Label(win, text="Link URL")
linkLabel.grid(column=2, row=3)

#OptionMenu
categoryVar = tk.StringVar()
categoryVar.set("Baby") #default value

category = tk.OptionMenu(win, categoryVar, "Baby", "Beauty", "Digital", "Fashion", "Food", "Living", "Sports")
category.grid(column=2, row=0)

#Input
headerTextVar = tk.StringVar()
headerTextBox = ttk.Entry(win, width=20, textvariable=headerTextVar)
headerTextBox.insert('end', 'HOT TRENDS')
headerTextBox.grid(row=1, column=2, pady=(3,0))

for i in range(7):
    r = 4 + i

    if i ==0:
           indexLabel = ttk.Label(win, text=str(i + 1) + ". (185 x 280px)")
    else:
        indexLabel = ttk.Label(win, text=str(i + 1) + ". (185 x 140 px)")
    indexLabel.grid(column=0, row=r)

    if i == 0:
        one = input("one", r)
    if i == 1:
        two = input("two", r)
    if i == 2:
        three = input("three", r)
    if i == 3:
        four = input("four", r)
    if i == 4:
        five = input("five", r)
    if i == 5:
        six = input("six", r)
    if i == 6:
        seven = input("seven", r)

        clearButton = ttk.Button(win, text="Reset", command=delete)
        clearButton.grid(column=1, row=i+5)
        generateButton = ttk.Button(win, text="Generate HTML", command=input.generate)
        generateButton.grid(column=2, row=i+5)

win.mainloop()