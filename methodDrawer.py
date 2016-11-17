import sys
from PIL import Image, ImageDraw, ImageFont


def methodDrawer(printout):
    f = open("text/%s.txt" % (printout))
    stage = int(f.readline())
    fontSize = 36
    rows = f.readlines()
    w, h = (fontSize*stage+10, int(fontSize*len(rows)*1.2)+10)
    im = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("AppleGothic.ttf", fontSize)

    x = 10
    y = 10
    r = 0
    prevTrebX = x + fontSize*0.4
    prevTrebY = y + fontSize*0.6
    blueLine = "2"
    prevBlueX = x + fontSize*1.4
    prevBlueY = prevTrebY
    prevChange = rows[0][0]
    for curChange in rows:
        curChange = curChange.split()
        x = 10
        for bell in curChange:
            if bell == "1":
                draw.line((prevTrebX, prevTrebY, x+fontSize*0.4,
                           y+fontSize*0.6), fill='red', width=2)
                prevTrebX = x+fontSize*0.4
                prevTrebY = y+fontSize*0.6
            elif bell == blueLine:
                draw.line((prevBlueX, prevBlueY, x+fontSize*0.4,
                           y+fontSize*0.6), fill='blue', width=2)
                prevBlueX = x+fontSize*0.4
                prevBlueY = y+fontSize*0.6
            if r % (len(rows)-1) == 0 or (bell != "1" and bell != blueLine):
                draw.text((x, y), bell, (0, 0, 0), font)
            x += fontSize
        y += fontSize*1.2
        r += 1
        if curChange[0] == "1" and prevChange == "1":
            draw.line((x, y-fontSize*.1, im.size[0]-x, y-fontSize*.1),
                      fill='silver')
        prevChange = curChange[0]

    im.save("images/out.jpg")
    f.close()

if __name__ == "__main__":
    methodDrawer(str(sys.argv[1]))
