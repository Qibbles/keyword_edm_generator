import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#images
babyImg, babySize, babyAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_baby.png", 750, "Center"
beautyImg, beautySize, beautyAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_beauty.png", 750, "Left"
digitalImg, digitalSize, digitalAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_digital.png", 750, "Center"
fashionImg, fashionSize, fashionAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_fashion.png", 750, "Center"
foodImg, foodSize, foodAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_food.png", 680, "Left"
livingImg, livingSize, livingAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_living.png", 750, "Center"
sportsImg, sportsSize, sportsAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_sports.png", 750, "Center"

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
        self.linkBox.grid(column=3, row=self.r, padx=(0, 5))
        update()
        
    def generate():
        templateCategory = categoryVar.get()

        if templateCategory == "Baby":
            filename = "baby_keyword_insert.html"
        elif templateCategory == "Beauty":
            filename = "beauty_keyword_insert.html"
        elif templateCategory == "Digital":
            filename = "digital_keyword_insert.html"
        elif templateCategory == "Fashion":
            filename = "fashion_keyword_insert.html"
        elif templateCategory == "Food":
            filename = "food_keyword_insert.html"
        elif templateCategory == "Living":
            filename = "living_keyword_insert.html"
        elif templateCategory == "Sports":
            filename = "sports_keyword_insert.html"
        elif templateCategory == "Others":
            filename = "keyword_edm_insert.html"

        try:
            fileExist = open(template[1], "r")
            if messagebox.askokcancel("Error - Existing file for " + template[0] + " detected!", "Do you wish to overwrite existing file?"):
                createInsert(templateCategory, filename)
            else:
                pass
        except:
            createInsert(templateCategory, filename)
        aspect()

def update(*args):
    templateCategory = categoryVar.get()
    if templateCategory == "Baby":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, babyImg)
        bannerWidthBox.insert(0, babySize)
        alignVar.set(babyAlign)
    elif templateCategory == "Beauty":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, beautyImg)
        bannerWidthBox.insert(0, beautySize)
        alignVar.set(beautyAlign)
    elif templateCategory == "Digital":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, digitalImg)
        bannerWidthBox.insert(0, digitalSize)
        alignVar.set(digitalAlign)
    elif templateCategory == "Fashion":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, fashionImg)
        bannerWidthBox.insert(0, fashionSize)
        alignVar.set(fashionAlign)
    elif templateCategory == "Food":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, foodImg)       
        bannerWidthBox.insert(0, foodSize)
        alignVar.set(foodAlign)
    elif templateCategory == "Living":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, livingImg)
        bannerWidthBox.insert(0, livingSize)
        alignVar.set(livingAlign)
    elif templateCategory == "Sports":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, sportsImg)
        bannerWidthBox.insert(0, sportsSize)
        alignVar.set(sportsAlign)
    elif templateCategory == "Others":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')

def aspect():
        aspect = round(max(int(heightOption.get()), int(widthOption.get()))/min(int(heightOption.get()), int(widthOption.get())),5)
        aspectBox.delete(0, 'end')
        aspectBox.insert(0, aspect)

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

    one.iconBox.focus()

def createInsert(templateCategory, filename):
    keywordArray = []
    bannerImg = bannerImgOption.get()
    bannerSize = bannerWidthOption.get()
    bannerAlign = alignVar.get()
    fontSize = fontOption.get()
    widthSize = widthOption.get()
    heightSize = heightOption.get()  

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
    html.write('<table width="' + str(bannerSize) + '" style="table-layout: fixed; padding-left: 0px; padding-top: 10px; padding-right: 0px; padding-bottom: 10px;" border="0" cellspacing="0" cellpadding="0" align="' + bannerAlign +'">\n')
    html.write('    <tbody>\n')
    if bannerImg != "":
        html.write('        <tr>\n')
        html.write('            <td colspan="11"><img src=' + bannerImg + ' width="100%" border="0"></td>\n')
        html.write('        </tr>\n')
    html.write('        <tr>\n')
    html.write('            <table width="' +str(bannerSize) + '" align="' + bannerAlign + '">\n')
    for i in range(2):
        html.write('                    <tr>\n')
        for icon in range(5):
            if keywordArray[icon][0] != "":
                html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+icon][2] + '"><img src="' + keywordArray[(i*5)+icon][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')
            else:
                html.write('                        <th padding="10px"></th>\n')
        html.write('                    </tr>\n')
        html.write('                    <tr>\n')
        for keyword in range(5):
            if keywordArray[keyword][1] != "":
                html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)+keyword][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)+keyword][1] + '</a></th>\n')
            else:
                html.write('                        <th padding="10px"></th>\n')
        html.write('                    </tr>\n')
        html.write('                    <tr>\n')
        html.write('                        <td></br ></td>\n')
        html.write('                    </tr>\n')
    html.write('            </table>\n')
    html.write('        </tr>\n')
    html.write('    </tbody>\n')
    html.write('</table>\n')
    html.close()

    messagebox.showinfo("Success!", "EDM insert for " + templateCategory + " created!")

def width():
    height = heightOption.get()
    widthBox.delete(0, 'end')
    width = int(round(float(aspectOption.get()) * float(height),0))
    widthBox.insert(0, width)

def height():
    width = widthOption.get()
    heightBox.delete(0, 'end')
    height = int(round(float(aspectOption.get()) * float(width),0))
    heightBox.insert(0, height)

#GUI
main = tk.Tk()
main.title("Keyword EDM Generator")
main.resizable(False, False)

### Notebook ###
nb = ttk.Notebook(main)
nb.grid(row=2, column=0, pady=(5,0), padx=(1,0), sticky='NSEW')

#Input tab
win = ttk.Frame(nb)
nb.add(win, text="Input")

guide = ttk.Frame(nb)
nb.add(guide, text="Help")

### Help Tab ###
helpMsg = "There is no help.\nGood luck!\n\nEDM Generator Version 3"
helpLabel = tk.Message(guide, text=helpMsg, width=500)
helpLabel.grid(row=0, column=0)

### Input Tab ###
#Header labels
bannerImgLabel = ttk.Label(win, text="Banner Image URL").grid(row=0, column=1)

bannerLabel = ttk.Label(win, text="Banner Width").grid(row=1, column=1)

bannerAlignLabel = ttk.Label(win, text="EDM Alignment").grid(row=2, column=1)
aspectLabel = ttk.Label(win, text="Aspect Ratio").grid(row=2, column=3)

fontLabel = ttk.Label(win, text="Font Size").grid(row=3, column=1)

widthLabel = ttk.Label(win, text="Image Width (pixels)").grid(row=4, column=1)

heightLabel = ttk.Label(win, text="Image Height (pixels)").grid(row=5, column=1)

templateLabel = ttk.Label(win, text="Template Category").grid(row=6, column=1)

iconLabel = ttk.Label(win, text="Icon URL").grid(row=7, column=1)
KeywordLabel = ttk.Label(win, text="Keyword").grid(row=7, column=2)
linkLabel = ttk.Label(win, text="Link URL").grid(row=7, column=3)

#OptionMenu
categoryVar = tk.StringVar()
categoryVar.set("Baby") #default value
category = tk.OptionMenu(win, categoryVar, "Baby", "Beauty", "Digital", "Fashion", "Food", "Living", "Sports", "Others")
category.grid(column=2, row=6)
categoryVar.trace("w", update)

alignVar = tk.StringVar()
alignVar.set("center") #default value
alignment = tk.OptionMenu(win, alignVar, "Left", "Center", "Right").grid(row=2, column=2)

#Input
bannerImgOption = tk.StringVar()
bannerImgBox = ttk.Entry(win, width=20, textvariable=bannerImgOption)
bannerImgBox.grid(row=0, column=2, pady=(3,0))

bannerWidthOption = tk.StringVar()
bannerWidthBox = ttk.Entry(win, width=20, textvariable=bannerWidthOption)
bannerWidthBox.grid(row=1, column=2, pady=(3,0))

fontOption = tk.StringVar()
fontBox = ttk.Entry(win, width=20, textvariable=fontOption)
fontBox.insert(0, "30")
fontBox.grid(row=3, column=2, pady=(3,0))

widthOption = tk.StringVar()
widthBox = ttk.Entry(win, width=20, textvariable=widthOption)
widthBox.insert(0, "76")
widthBox.grid(row=4, column=2, pady=(3,0))

heightOption = tk.StringVar()
heightBox = ttk.Entry(win, width=20, textvariable=heightOption)
heightBox.insert(0, "100")
heightBox.grid(row=5, column=2, pady=(3,0))

aspectOption = tk.StringVar()
aspectBox = ttk.Entry(win, width=8, textvariable=aspectOption)
aspectBox.grid(column=3, row=3, pady=(3,0))
# aspectFrame = tk.Frame(win).grid(row=2, column=3, padx=20)
aspectWidthButton = ttk.Button(win, text="Width", command=width).grid(row=4, column=3)
aspectHeightButton = ttk.Button(win, text="Height", command=height).grid(row=5, column=3)

for i in range(10):
    r = 8 + i

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
        clearButton.grid(column=1, row=i+9, pady=5)
        generateButton = ttk.Button(win, text="Generate HTML", command=input.generate)
        generateButton.grid(column=3, row=i+9, pady=5)

aspect()

one.iconBox.focus()

win.mainloop()
