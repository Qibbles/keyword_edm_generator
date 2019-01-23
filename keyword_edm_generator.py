import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#images
babyImg, babySize, babyAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_baby.png", 750, "center"
beautyImg, beautySize, beautyAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_beauty.png", 750, "left"
digitalImg, digitalSize, digitalAlign = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_digital.png", 750, "center"
fashionImg, fashionSize, fashionAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_fashion.png", 750, "center"
foodImg, foodSize, foodAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_food.png", 680, "left"
livingImg, livingSize, livingAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_living.png", 750, "center"
sportsImg, sportsSize, sportsAlign  = "http://dp.image-gmkt.com/dp2016/SG/design/CM2/edm_trending_sports.png", 750, "center"

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
        template = update()
        try:
            fileExist = open(template[4], "r")
            if messagebox.askokcancel("Error - Existing file for " + template[0] + " detected!", "Do you wish to overwrite existing file?"):
                createInsert(template[0], template[1], template[2], template[3], template[4])
            else:
                pass
        except:
            createInsert(template[0], template[1], template[2], template[3], template[4])
        aspect()

def update(*args):
    templateCategory = categoryVar.get()
    if templateCategory == "Baby":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, babyImg)
        bannerWidthBox.insert(0, babySize)
        banner = babyImg
        size = babySize
        align = babyAlign
        filename = "baby_keyword_insert.html"
    elif templateCategory == "Beauty":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, beautyImg)
        bannerWidthBox.insert(0, beautySize)
        banner = beautyImg
        size = beautySize
        align = beautyAlign
        filename = "beauty_keyword_insert.html"
    elif templateCategory == "Digital":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, digitalImg)
        bannerWidthBox.insert(0, digitalSize)
        banner = digitalImg
        size = digitalSize
        align = digitalAlign
        filename = "digital_keyword_insert.html"
    elif templateCategory == "Fashion":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, fashionImg)
        bannerWidthBox.insert(0, fashionSize)
        banner = fashionImg
        size = fashionSize
        align = fashionAlign
        filename = "fashion_keyword_insert.html"
    elif templateCategory == "Food":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, foodImg)       
        bannerWidthBox.insert(0, foodSize)
        banner = foodImg
        size = foodSize
        align = foodAlign
        filename = "food_keyword_insert.html"
    elif templateCategory == "Living":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, livingImg)
        bannerWidthBox.insert(0, livingSize)
        banner = livingImg
        size = livingSize
        align = livingAlign
        filename = "living_keyword_insert.html"
    elif templateCategory == "Sports":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        bannerImgBox.insert(0, sportsImg)
        bannerWidthBox.insert(0, sportsSize)
        banner = sportsImg
        size = sportsSize
        align = sportsAlign
        filename = "sports_keyword_insert.html"
    elif templateCategory == "Others":
        bannerImgBox.delete(0, 'end')
        bannerWidthBox.delete(0, 'end')
        banner = ""
        size = ""
        align = "center"
        filename = "keyword_edm_insert.html"
    return(templateCategory, banner, size, align, filename)

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

def createInsert(templateCategory, banner, size, align, filename):
    keywordArray = []
    bannerSize = bannerWidthOption.get()
    bannerImg = bannerImgOption.get()
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
    html.write('<table width="' + str(size) + '" style="table-layout: fixed; padding-left: 0px; padding-top: 10px; padding-right: 0px; padding-bottom: 10px;" border="0" cellspacing="0" cellpadding="0" align="' + align +'">\n')
    html.write('    <tbody>\n')
    if banner != "":
        html.write('        <tr>\n')
        html.write('            <td colspan="11"><img src=' + banner + ' width="100%" border="0"></td>\n')
        html.write('        </tr>\n')
    html.write('        <tr>\n')
    html.write('            <table width="' +str(size) + '" align="' + align + '">\n')
    for i in range(2):
        html.write('                    <tr>\n')
        for each in range(5):
            if keywordArray[each][0] != "":
                html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+each][2] + '"><img src="' + keywordArray[(i*5)+each][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')
            else:
                html.write('                        <th padding="10px"></th>\n')
            # html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+1][2] + '"><img src="' + keywordArray[(i*5)+1][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')       
            # html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+2][2] + '"><img src="' + keywordArray[(i*5)+2][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')
            # html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+3][2] + '"><img src="' + keywordArray[(i*5)+3][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')        
            # html.write('                        <th padding="10px"><a href="' + keywordArray[(i*5)+4][2] + '"><img src="' + keywordArray[(i*5)+4][0] + '" width="' + widthSize + '" height="' + heightSize + '"></a></th>\n')   
        html.write('                    </tr>\n')
        html.write('                    <tr>\n')
        html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)][1] + '</a></th>\n')
        html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)+1][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)+1][1] + '</a></th>\n')
        html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)+2][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)+2][1] + '</a></th>\n')
        html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)+3][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)+3][1] + '</a></th>\n')
        html.write('                        <th style="word-wrap: break-word"><a href="' + keywordArray[(i*5)+4][2] + '" style="font-family: Helvetica, sans-serif; font-size:' + fontSize + '; color: #333; text-decoration: none;">' + keywordArray[(i*5)+4][1] + '</a></th>\n')
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
win = tk.Tk()
win.title("Keyword EDM Generator by Gregory")
win.resizable(False, False)
# win.iconbitmap(r'..\icon.ico')

#Header labels
bannerLabel = ttk.Label(win, text="Banner Width").grid(row=1, column=1)

bannerImgLabel = ttk.Label(win, text="Banner Image URL").grid(row=0, column=1)

fontLabel = ttk.Label(win, text="Font Size")
fontLabel.grid(column=1, row=2)

widthLabel = ttk.Label(win, text="Image Width (pixels)")
widthLabel.grid(column=1, row=3)

aspectLabel = ttk.Label(win, text="Aspect Ratio").grid(row=1, column=3)

heightLabel = ttk.Label(win, text="Image Height (pixels)")
heightLabel.grid(column=1, row=4)

templateLabel = ttk.Label(win, text="Template Category")
templateLabel.grid(column=1, row=5)

iconLabel = ttk.Label(win, text="Icon URL")
iconLabel.grid(column=1, row=6)

KeywordLabel = ttk.Label(win, text="Keyword")
KeywordLabel.grid(column=2, row=6)

linkLabel = ttk.Label(win, text="Link URL")
linkLabel.grid(column=3, row=6)

#OptionMenu
categoryVar = tk.StringVar()
categoryVar.set("Baby") #default value
category = tk.OptionMenu(win, categoryVar, "Baby", "Beauty", "Digital", "Fashion", "Food", "Living", "Sports", "Others")
category.grid(column=2, row=5)
categoryVar.trace("w", update)

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
fontBox.grid(column=2, row=2, pady=(3,0))

widthOption = tk.StringVar()
widthBox = ttk.Entry(win, width=20, textvariable=widthOption)
widthBox.insert(0, "76")
widthBox.grid(column=2, row=3, pady=(3,0))

heightOption = tk.StringVar()
heightBox = ttk.Entry(win, width=20, textvariable=heightOption)
heightBox.insert(0, "100")
heightBox.grid(column=2, row=4, pady=(3,0))

aspectOption = tk.StringVar()
aspectBox = ttk.Entry(win, width=8, textvariable=aspectOption)
aspectBox.grid(column=3, row=2, pady=(3,0))
# aspectFrame = tk.Frame(win).grid(row=2, column=3, padx=20)
aspectWidthButton = ttk.Button(win, text="Width", command=width).grid(row=3, column=3)
aspectHeightButton = ttk.Button(win, text="Height", command=height).grid(row=4, column=3)

for i in range(10):
    r = 7 + i

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
        clearButton.grid(column=1, row=i+8, pady=5)
        generateButton = ttk.Button(win, text="Generate HTML", command=input.generate)
        generateButton.grid(column=3, row=i+8, pady=5)

aspect()

one.iconBox.focus()

win.mainloop()
