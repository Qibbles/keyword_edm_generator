import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#images
babyImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_baby.png"
beautyImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_beauty.png"
digitalImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_digital.png"
fashionImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_fashion.png"
foodImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_food.png"
livingImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_living.png"
sportsImg = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_sports.png"

#functions
class input:

    def __init__(self, index, r):
        self.r = r
        self.icon = tk.StringVar()
        self.iconBox = ttk.Entry(win, width=20, textvariable=self.icon)
        self.iconBox.grid(column=1, row=self.r)
        self.keyword = tk.StringVar()
        self.keywordBox = ttk.Entry(win, width=20, textvariable=self.keyword)
        self.keywordBox.grid(column=2, row=self.r)
        self.link = tk.StringVar()
        self.linkBox = ttk.Entry(win, width=20, textvariable=self.link)
        self.linkBox.grid(column=3, row=self.r)

    def generate():
        templateCategory = categoryVar.get()
        if templateCategory == "Baby":
            banner = babyImg
            filename = "baby_keyword_insert.html"
        elif templateCategory == "Beauty":
            banner = beautyImg
            filename = "beauty_keyword_insert.html"
        elif templateCategory == "Digital":
            banner = digitalImg
            filename = "digital_keyword_insert.html"
        elif templateCategory == "Fashion":
            banner = fashionImg
            filename = "fashion_keyword_insert.html"
        elif templateCategory == "Food":
            banner = foodImg
            filename = "food_keyword_insert.html"
        elif templateCategory == "Living":
            banner = livingImg
            filename = "living_keyword_insert.html"
        elif templateCategory == "Sports":
            banner = sportsImg
            filename = "sports_keyword_insert.html"
        
        try:
            fileExist = open(filename, "r")
            if messagebox.askokcancel("Error - Existing file for " + templateCategory + " detected!", "Do you wish to overwrite existing file?"):
                createInsert(templateCategory, banner, filename)
            else:
                pass
        except:
            createInsert(templateCategory, banner, filename)

    # def clear(self):
    #     self.iconBox.delete(0, 'end')
    #     self.keywordBox.delete(0, 'end')
    #     self.linkBox.delete(0, 'end')

def delete():
    one.iconBox.delete(0, 'end')
    one.keywordBox.delete(0, 'end')
    one.linkBox.delete(0, 'end')

    two.iconBox.delete(0, 'end')
    two.keywordBox.delete(0, 'end')
    two.linkBox.delete(0, 'end')

    three.iconBox.delete(0, 'end')
    three.keywordBox.delete(0, 'end')
    three.linkBox.delete(0, 'end')

    four.iconBox.delete(0, 'end')
    four.keywordBox.delete(0, 'end')
    four.linkBox.delete(0, 'end')

    five.iconBox.delete(0, 'end')
    five.keywordBox.delete(0, 'end')
    five.linkBox.delete(0, 'end')

    six.iconBox.delete(0, 'end')
    six.keywordBox.delete(0, 'end')
    six.linkBox.delete(0, 'end')

    seven.iconBox.delete(0, 'end')
    seven.keywordBox.delete(0, 'end')
    seven.linkBox.delete(0, 'end')

    eight.iconBox.delete(0, 'end')
    eight.keywordBox.delete(0, 'end')
    eight.linkBox.delete(0, 'end')

    nine.iconBox.delete(0, 'end')
    nine.keywordBox.delete(0, 'end')
    nine.linkBox.delete(0, 'end')

    ten.iconBox.delete(0, 'end')
    ten.keywordBox.delete(0, 'end')
    ten.linkBox.delete(0, 'end')

def createInsert(templateCategory, banner, filename):

    keywordArray = []

    keywordArray.append([one.icon.get(), one.keyword.get(), one.link.get()])
    keywordArray.append([two.icon.get(), two.keyword.get(), two.link.get()])
    keywordArray.append([three.icon.get(), three.keyword.get(), three.link.get()])
    keywordArray.append([four.icon.get(), four.keyword.get(), four.link.get()])
    keywordArray.append([five.icon.get(), five.keyword.get(), five.link.get()])
    keywordArray.append([six.icon.get(), six.keyword.get(), six.link.get()])
    keywordArray.append([seven.icon.get(), seven.keyword.get(), seven.link.get()])
    keywordArray.append([eight.icon.get(), eight.keyword.get(), eight.link.get()])
    keywordArray.append([nine.icon.get(), nine.keyword.get(), nine.link.get()])
    keywordArray.append([ten.icon.get(), ten.keyword.get(), ten.link.get()])

    html = open(filename, "w")
    html.write('<table width="750" style="table-layout: fixed; padding-left: 0px; padding-top: 10px; padding-right: 0px; padding-bottom: 10px;" border="0" cellspacing="0" cellpadding="0" align="center">')
    html.write('    <tbody>')
    html.write('        <tr>')
    html.write('            <td width="750" colspan="3"><img src=' + banner + ' width="100%" border="0"></td>')
    html.write('        </tr>')
    for i in range(2):
        html.write('        <tr>')
        html.write('            <td>')
        html.write('                <table border="0">')
        html.write('                    <tr>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '"><img src="' + keywordArray[(i*5)][0] + '" style="max-width:64px;" /></a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)+1][2] + '"><img src="' + keywordArray[(i*5)+1][0] + '" style="max-width:64px;" /></a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)+2][2] + '"><img src="' + keywordArray[(i*5)+2][0] + '" style="max-width:64px;" /></a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)+3][2] + '"><img src="' + keywordArray[(i*5)+3][0] + '" style="max-width:64px;" /></a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)+4][2] + '"><img src="' + keywordArray[(i*5)+4][0] + '" style="max-width:64px;" /></a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                    </tr>')
        html.write('                    <tr>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size: 30px; color: #333; text-decoration: none;">' + keywordArray[(i*5)][1] + '</a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size: 30px; color: #333; text-decoration: none;">' + keywordArray[(i*5)+1][1] + '</a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size: 30px; color: #333; text-decoration: none;">' + keywordArray[(i*5)+2][1] + '</a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size: 30px; color: #333; text-decoration: none;">' + keywordArray[(i*5)+3][1] + '</a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                        <th width="20%"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size: 30px; color: #333; text-decoration: none;">' + keywordArray[(i*5)+4][1] + '</a></th>')
        html.write('                        <th width="1%"></th>')
        html.write('                    </tr>')
        html.write('                </table>')
        html.write('            </td>')
        html.write('        </tr>')
    html.write('    </tbody>')
    html.write('</table>')
    html.close()

    messagebox.showinfo("Success!", "EDM insert for " + templateCategory + " created!")

#GUI
win = tk.Tk()
win.title("Keyword EDM Generator by Gregory")
win.resizable(False, False)
# win.iconbitmap(r'..\icon.ico')

#Header labels
templateLabel = ttk.Label(win, text="Template Category")
templateLabel.grid(column=1, row=0)

iconLabel = ttk.Label(win, text="Icon URL")
iconLabel.grid(column=1, row=1)

KeywordLabel = ttk.Label(win, text="Keyword")
KeywordLabel.grid(column=2, row=1)

linkLabel = ttk.Label(win, text="Link URL")
linkLabel.grid(column=3, row=1)

#OptionMenu
categoryVar = tk.StringVar()
categoryVar.set("Baby") #default value

category = tk.OptionMenu(win, categoryVar, "Baby", "Beauty", "Digital", "Fashion", "Food", "Living", "Sports")
category.grid(column=2, row=0)

#Input
for i in range(10):
    r = 2 + i

    indexLabel = ttk.Label(win, text=str(i + 1) + ". ")
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
    if i == 7:
        eight = input("eight", r)
    if i == 8:
        nine  = input("nine", r)
    if i == 9:
        ten  = input("ten", r)
        clearButton = ttk.Button(win, text="Reset", command=delete)
        clearButton.grid(column=1, row=i+3)
        generateButton = ttk.Button(win, text="Generate HTML", command=input.generate)
        generateButton.grid(column=3, row=i+3)

win.mainloop()
