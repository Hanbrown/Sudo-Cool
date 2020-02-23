# 2/22/2020
# A program that does text to speech

import os
import requests
import time
from xml.etree import ElementTree
import winsound
import sudokugrid
import time
import pygame

try:
    input = raw_input
except NameError:
    pass


class TextToSpeech(object):
    def __init__(self, subscription_key, text):
        self.subscription_key = subscription_key
        self.tts = text #Used to be an input line
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def setText(self, text):
        self.tts = text

    def get_token(self):
        fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self, isEdit, name):

        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        if isEdit:
            voice.set(
                'name', 'Microsoft Server Speech Text to Speech Voice (en-AU, Catherine)') #en-US, Guy24KRUS
        else:
            voice.set(
                'name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            with open(name +'.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                      "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
                  "\nSomething went wrong. Check your subscription key and headers.\n")

#This function creates audio files for each number
def init():
    if __name__ == "__main__":
        subscription_key = "3dac5169881a4623a77d92d516f673d7" #Private Key

        msg = "Enter Difficulty"
        filename = "difficulty"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Blank"
        filename = "blank"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Read row"
        filename = "read_row"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Read column"
        filename = "read_col"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Read block"
        filename = "read_block"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Read"
        filename = "read"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Coordinate of number, please enter row and column"
        filename = "coord_prompt"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Row"
        filename = "row"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Column"
        filename = "col"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Cursor at"
        filename = "cursorloc"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "New Value"
        filename = "newval"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Current Value"
        filename = "curval"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Warning: current value conflicts with cell in"
        filename = "warning"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        msg = "Warning: edit failed please retry. "
        filename = "editfail"
        app = TextToSpeech(subscription_key, msg)
        app.get_token()
        app.save_audio(False, filename)

        #Creates the permanent files (isEdit parameter is set to false)
        for i in range(1, 10):
            filename = "perm-" +str(i)
            app = TextToSpeech(subscription_key, str(i))
            app.get_token()
            app.save_audio(False, filename)

        #Creates the edit files (isEdit parameter is set to true)
        for i in range(1, 10):
            filename = "edit-" +str(i)
            app = TextToSpeech(subscription_key, str(i))
            app.get_token()
            app.save_audio(True, filename)

#This function reads an array of numbers out loud
def readGrid(section):
    for i in range(len(section)):
            pressed = pygame.key.get_pressed()
            if section[i] < 10 and section[i] > 0:
                winsound.PlaySound("perm-" +str(section[i]) +".wav",winsound.SND_ASYNC)
                time.sleep(1.25)
            elif section[i] == 0:
                winsound.PlaySound("blank.wav",winsound.SND_ASYNC)
                time.sleep(1.25)
            else:
                winsound.PlaySound("edit-" +str(section[i]-10) +".wav",winsound.SND_ASYNC)
                time.sleep(1.25)

            #Skips the rest went pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

#This function performs certain actions based the menu index passed in
def playMenuAction(index):
    if (index == 0):
        winsound.PlaySound("coord_prompt.wav",winsound.SND_ASYNC)
    elif (index == 1):
        winsound.PlaySound("read_row.wav",winsound.SND_ASYNC)
    elif (index == 2):
        winsound.PlaySound("read_col.wav",winsound.SND_ASYNC)
    else:
        winsound.PlaySound("read_block.wav",winsound.SND_ASYNC)

def readCell(x, y):
    winsound.PlaySound("cursorloc.wav",winsound.SND_ASYNC)
    time.sleep(1.25)
    winsound.PlaySound("row.wav",winsound.SND_ASYNC)
    time.sleep(0.5)
    winsound.PlaySound("perm-" +str(x) +".wav",winsound.SND_ASYNC)
    time.sleep(1)
    winsound.PlaySound("col.wav",winsound.SND_ASYNC)
    time.sleep(0.5)
    winsound.PlaySound("perm-" +str(y) +".wav",winsound.SND_ASYNC)
    time.sleep(1)
    winsound.PlaySound("curval.wav",winsound.SND_ASYNC)
    time.sleep(1)
    if (gridObj.getCell(x, y) > 10):
        winsound.PlaySound("edit-" + str(gridObj.getCell(x, y)-10) +".wav",winsound.SND_ASYNC)
        time.sleep(1)
    elif (gridObj.getCell(x, y) == 0):
        winsound.PlaySound("blank.wav",winsound.SND_ASYNC)
        time.sleep(1.25)
    else:
        winsound.PlaySound("perm-" + str(gridObj.getCell(x, y)) +".wav",winsound.SND_ASYNC)
        time.sleep(1)
        

def editFail(x, y):
    winsound.PlaySound("editfail.wav",winsound.SND_ASYNC)
    time.sleep(2.5)
    winsound.PlaySound("cursorloc.wav",winsound.SND_ASYNC)
    time.sleep(1.25)
    winsound.PlaySound("row.wav",winsound.SND_ASYNC)
    time.sleep(0.5)
    winsound.PlaySound("perm-" +str(x) +".wav",winsound.SND_ASYNC)
    time.sleep(1)
    winsound.PlaySound("col.wav",winsound.SND_ASYNC)
    time.sleep(0.5)
    winsound.PlaySound("perm-" +str(y) +".wav",winsound.SND_ASYNC)

def performAction(index):
    if (index == 0):
        x = numberInput()
        y = numberInput()
        newvalue = 0
        result = 0
        exitLoop = False
        readCell(x, y)
        
        while not exitLoop:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        result = 0
                        exitLoop = True
                        break
                    if event.key == pygame.K_1:
                        result = 11
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_2:
                        result = 12
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_3:
                        result = 13
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_4:
                        result = 14
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_5:
                        result = 15
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_6:
                        result = 16
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_7:
                        result = 17
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_8:
                        result = 18
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                    if event.key == pygame.K_9:
                        result = 19
                        if (gridObj.getCell(x, y) > 10 or gridObj.getCell(x, y) == 0):
                            exitLoop = True
                            break
                        else:
                            editFail(x, y)
                            time.sleep(1)
                    if event.key == pygame.K_UP:
                        x += 7
                        x %= 9
                        x += 1
                    if event.key == pygame.K_DOWN:
                        x %= 9
                        x += 1
                    if event.key == pygame.K_RIGHT:
                        y %= 9
                        y += 1
                    if event.key == pygame.K_LEFT:
                        y += 7
                        y %= 9
                        y += 1
                    if event.key == pygame.K_ESCAPE:
                        exitLoop = True
                        break
                    if event.key == pygame.K_RETURN:
                        readCell(x, y)

        gridObj.enterAns(x, y, result)
        winsound.PlaySound("newval.wav",winsound.SND_ASYNC)
        time.sleep(1)
        winsound.PlaySound("edit-" + str(gridObj.getCell(x, y) % 10) +".wav",winsound.SND_ASYNC)
        time.sleep(1.5)
                        
                        
    elif (index == 1):
        index = numberInput()
        part = gridObj.getRow(index)
        print(part)
        readGrid(part)
    elif (index == 2):
        index = numberInput()
        part = gridObj.getCol(index)
        print(part)
        readGrid(part)
    else:
        index = numberInput()
        part = gridObj.getBlock(index)
        print(part)
        readGrid(part)

def numberInput():
    result = 0
    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    result = 0
                if event.key == pygame.K_1:
                    result = 1
                if event.key == pygame.K_2:
                    result = 2
                if event.key == pygame.K_3:
                    result = 3
                if event.key == pygame.K_4:
                    result = 4
                if event.key == pygame.K_5:
                    result = 5
                if event.key == pygame.K_6:
                    result = 6
                if event.key == pygame.K_7:
                    result = 7
                if event.key == pygame.K_8:
                    result = 8
                if event.key == pygame.K_9:
                    result = 9
                if event.key == pygame.K_RETURN:
                    return result

class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 9, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 9, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win):
    win.fill((255,255,255))
    gap = 1
    for i in range(10):
        if i % 3 == 0 and i != 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(win, (0, 0, 0), (0, i*gap), (9, i * gap), thick)
        pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, 9), thick)
    # Draw Cubes
    for i in range(0, 81):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = 1
        x = 9 * gap
        y = 9 * gap

        if gridObj.grid[i] > 10:
            text = fnt.render(str(gridObj.grid[i] % 10), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(gridObj.grid[i] == 0):
            text = fnt.render(str(gridObj.grid[i]), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))


#Main function
def main():
    #navigation
    cursor = 0
    playMenuAction(0)
    #Event Framework
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                #determine if Tab was pressed
                if event.key == pygame.K_TAB:
                    print("tab")
                    cursor += 1
                    cursor %= 4
                    playMenuAction(cursor)

                #if Return is pressed
                if event.key == pygame.K_RETURN:
                    performAction(cursor)
                    playMenuAction(cursor)
            pygame.display.update()
        pygame.display.flip()

        redraw_window(screen)
        clock.tick(60)

init()
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

width = 540
height = 600

pygame.display.set_caption('Pseudo-Cool Sudoku')

screen = pygame.display.set_mode((width, height))
screen.fill(white) 
clock = pygame.time.Clock()
winsound.PlaySound("difficulty.wav",winsound.SND_ASYNC)
diff = numberInput()
gridObj = sudokugrid.SudokuPuzzle(diff)
main()
