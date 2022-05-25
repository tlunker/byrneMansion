import pygame
import experimental
#from leaderBoardData import savingData
from pygame import mixer
import time

clock = pygame.time.Clock()
clock.tick(60)
screenHeight = 400
screenWidth = 700

pygame.init()

#loading images and game sizing
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Menu")
menuScreen = pygame.image.load("title/menuFullScreen.png").convert()

allShelves = pygame.image.load("assets/images/Library/backgrounds/allShelves.png").convert()
clocksArea = pygame.image.load("assets/images/Library/backgrounds/clocksArea.png").convert()
bookshelfZoom1 = pygame.image.load("assets/images/Library/backgrounds/bookshelfZoom1.png").convert()
bookshelfZoom2 = pygame.image.load("assets/images/Library/backgrounds/bookshelfZoom2.png").convert()
bookshelfZoom3 = pygame.image.load("assets/images/Library/backgrounds/bookshelfZoom3.png").convert()
bookshelfZoom4 = pygame.image.load("assets/images/Library/backgrounds/bookshelfZoom4.png").convert()

ghost = pygame.image.load("assets\images\ghost.png").convert()
dialogueBox = pygame.image.load("assets\images\dialogueBox.png").convert()

#i dont think i have this rightTriangle = pygame.image.load("Downloads/rightTriangleThing.png").convert_alpha()
<<<<<<< HEAD
deskBg = pygame.image.load("assets/images/Library/backgrounds/deskBg.png")
bookDatabase = pygame.image.load("assets/images/Library/puzzle-1/desk/bookDatabase.png")
=======
deskBg = pygame.image.load("assets/images/Library/backgrounds/closeup of desk.png")
>>>>>>> a541ec53b2db14a824c9a86ec8b189b012ef67e8
deskOpen = pygame.image.load("assets/images/Library/backgrounds/deskOpen.png")

#DeskFile = pygame.image.load("assets/images/Library/backgrounds/file_inside_of_desk.png")
hintButton = pygame.image.load("assets/buttons/all-screens/hint.jpg").convert()
backButton = pygame.image.load("assets/buttons/all-screens/backButton.jpg").convert()
leftArrow = pygame.image.load("assets/buttons/all-screens/leftArrow.jpg").convert()
rightArrow = pygame.image.load("assets/buttons/all-screens/rightArrow.jpg").convert()

leverOn = pygame.image.load("assets/images/Library/puzzle-1/lever/leverOn.png").convert()
leverOff = pygame.image.load("assets/images/Library/puzzle-1/lever/leverOff.png").convert()

dialogBox = pygame.image.load("experimental/dialogueBox.png").convert()
mansionImage = pygame.image.load("experimental/mansionImage.jpg").convert()
userBox = pygame.image.load("experimental/dialogBox.png").convert()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (111, 78, 55)
Transparent = (0, 0, 0, 0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('red1')
active = False

#inventoryBible = pygame.image.load(" .................. ") #inventory image
#inventoryDancingMen = pygame.image.load(" ................ ") #inventory image
#inventoryBlankBook = pygame.image.load(" ................ ") #inventory image
#Bible = pygame.image.load(" .............. ") #should be the vesion where we see the verses 
#DancingMen = pygame.image.load(" .............. ") #version where we see the explanation to the dancing men cipher
#BlankBook = pygame.image.load(" .............. ") #nothing inside until ran under water

#i dont have any idea where the images for these are... if yo could please find them id be most gracious


#work-in-progress

oneOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/1clock.png").convert_alpha()
twoOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/2clock.png").convert_alpha()
threeOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/3clock.png").convert_alpha()
fourOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/4clock.png").convert_alpha()
fiveOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/5clock.png").convert_alpha()
sixOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/6clock.png").convert_alpha()
sevenOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/7clock.png").convert_alpha()
eightOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/8clock.png").convert_alpha()
nineOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/9clock.png").convert_alpha()
tenOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/10clock.png").convert_alpha()
elevenOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/11clock.png").convert_alpha()
twelveOClock = pygame.image.load("assets/images/Library/puzzle-1/clocks/12clock.png").convert_alpha()
timerBg = pygame.image.load("title/timerBg.jpg").convert()


'''oneOClock = pygame.image.load("1clockold.png").convert_alpha()
twoOClock = pygame.image.load("2clockold.png").convert_alpha()
threeOClock = pygame.image.load("3clockold.png").convert_alpha()
fourOClock = pygame.image.load("4clockold.png").convert_alpha()
fiveOClock = pygame.image.load("5clockold.png").convert_alpha()
sixOClock = pygame.image.load("6clockold.png").convert_alpha()
sevenOClock = pygame.image.load("7clockold.png").convert_alpha()
eightOClock = pygame.image.load("8clockold.png").convert_alpha()
nineOClock = pygame.image.load("9clockold.png").convert_alpha()
tenOClock = pygame.image.load("10clockold.png").convert_alpha()
elevenOClock = pygame.image.load("11clockold.png").convert_alpha()
twelveOClock = pygame.image.load("12clockold.png").convert_alpha()'''

inventoryImage = pygame.image.load("assets/images/inv/inventoryIcon.png").convert_alpha()
inventoryHotbar = pygame.image.load("assets/images/inv/inventoryHotbar.png").convert_alpha()
inventoryTextThing = pygame.image.load("assets/images/inv/inventoryTextThing.png").convert_alpha()
keyImage = pygame.image.load("assets/images/inv/keyImage.png").convert_alpha()
inventoryBackground = pygame.image.load("assets/images/inv/inventoryBackground.jpeg").convert_alpha()

#music
mixer.init()
inventoryDing = pygame.mixer.Sound("assets\sounds\effects\inventoryDing.wav")
#mixer.music.set_volume(0.7)
clueClick = pygame.mixer.Sound("assets\sounds\effects\clueClick.wav")
#bgMusic = mixer.music.load("assets/sounds/music/bgMusic.mp3")
#intense music lag moment


#classes for defining image, scale, and location
class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))

#images
menuScreen = imageScaling(0, 0, menuScreen, 0.5)

allShelves = imageScaling(0, 0, allShelves, 1.95)
clocksArea = imageScaling(0, 0, clocksArea, 1.85)
deskBg = imageScaling(40,0,deskBg,1)

deskOpen = imageScaling(40,0,deskOpen,2.3)
bookDatabase = imageScaling(250,150,bookDatabase,0.5)

dialogueBox = imageScaling(40,350,dialogueBox,0.4)

#DeskFile = imageScaling(40,0,DeskFile,2.3)
bookshelfZoom1 = imageScaling(0, 0, bookshelfZoom1, 1)
bookshelfZoom2 = imageScaling(0, 0, bookshelfZoom2, 1)
bookshelfZoom3 = imageScaling(0, 0, bookshelfZoom3, 1)
bookshelfZoom4 = imageScaling(0, 0, bookshelfZoom4, 1)
#rightTriangleImage = imageScaling(445, 35, rightTriangle, 0.2)

leftArrow = imageScaling(100, screenHeight/2, leftArrow, 0.3)
rightArrow = imageScaling(540, screenHeight/2, rightArrow, 0.3)

leverOn = imageScaling(435, 210, leverOn, 0.25)
leverOff = imageScaling(435, 210, leverOff, 0.25)

backButton = imageScaling(10, 10, backButton, 1)
hintButton = imageScaling(630,10,hintButton,0.3)
timerBg = imageScaling(604, 7, timerBg, 1)

#inventory media
keyImageButton = imageScaling(440, 180, keyImage, 0.3)
inventoryKey = imageScaling(197, 297, keyImage, 0.1)
#inventoryBible = imageScaling(w, x, inventoryBible, 0.1)
#inventoryBlankBook = imageScaling(w, x, inventoryBlankBook, 0.1)
#inventoryDancingMen = imageScaling(w, x, inventoryDancingMen, 0.1)

inventoryIcon = imageScaling(600, 10, inventoryImage, 0.3)
inventoryIcon2 = imageScaling(100, 300, inventoryImage, 0.4)
inventoryHotbar = imageScaling(200, 300, inventoryHotbar, 0.5)
inventoryTextThing = imageScaling(180, 40, inventoryTextThing, 0.5)
inventoryBackground = imageScaling(0, 0, inventoryBackground, 3)

#adding clock times individually to test
oneOClock = imageScaling(265, 10, oneOClock, 4)
twoOClock = imageScaling(265, 10, twoOClock, 4)
threeOClock = imageScaling(265, 10, threeOClock, 4)
fourOClock = imageScaling(265, 10, fourOClock, 4)
fiveOClock = imageScaling(265, 10, fiveOClock, 4)
sixOClock = imageScaling(265, 10, sixOClock, 4)
sevenOClock = imageScaling(265, 10, sevenOClock, 4)
eightOClock = imageScaling(265, 10, eightOClock, 4)
nineOClock = imageScaling(265, 10, nineOClock, 4)
tenOClock = imageScaling(265, 10, tenOClock, 4)
elevenOClock = imageScaling(265, 10, elevenOClock, 4)
twelveOClock = imageScaling(265, 10, twelveOClock, 4)

#hints
clockHint = "Counting is fun!" 
bookHint = "Aren't the books and shelves numbered?"
bookmarkHint = "Art isn't always perfect. There are often missing details."

#lists
imageList = [allShelves, clocksArea, deskBg]
shelfZooms = [bookshelfZoom1, bookshelfZoom2, bookshelfZoom3, bookshelfZoom4]
clockTimes = [oneOClock, twoOClock, threeOClock, fourOClock, fiveOClock, sixOClock, sevenOClock, eightOClock, nineOClock, tenOClock, elevenOClock, twelveOClock]
<<<<<<< HEAD
hintsList = [clockHint,bookHint,bookmarkHint]
inventory = []
=======
inventory = [inventoryKey]#, inventoryBible, inventoryBlankBook, inventoryDancingMen
>>>>>>> a541ec53b2db14a824c9a86ec8b189b012ef67e8
booksList = []
inventoryOpen = False
global userName
userName = ''

#initialization
clockIndex = 8 #clock time (it starts at 12:00)
imageIndex = 0 #rotates images of library 
hintIndex = 0 
leverState = False #false until lever clicked
keySelected = False #false until key in inventory is clicked

run = True 
imageOne = False  #used to cycle images and put arrows
clocksIteration = True #avoid stacked images and lag

menuOpen = True #will say menu is open until startButton clicked
menuImage = True #avoid stacked images and lag

zoomIn = False #checks if user zoomed into certain shelves
firstOpen = True #if user clicks bookshelf for first time, game bugs out (this is a temporary solution)

optionsClicked = False
leaderBoardClicked = False
startClicked = False

deskOpened = False

largeSans = pygame.font.Font("fonts/OpenSans-Regular.ttf", 28)

t = 1800
timerDelay = True

hintClockText = "Tick tock?"

def hint(text):
  dialogueBox.draw()
  font = pygame.font.Font("fonts/OpenSans-Regular.ttf", 12)
  text_surface = font.render(text, True, WHITE)
  text_rect = text_surface.get_rect()
  text_rect.center = (330, 385)
  screen.blit(text_surface, text_rect)

while run:
  #testing music
  #pygame.mixer.music.play(-1)
  while menuImage == True:
    menuScreen.draw()
    menuImage = False
    pygame.display.update()
    
  while imageOne == True:
    imageList[imageIndex].draw()
    leftArrow.draw()
    rightArrow.draw()
    hintButton.draw()
    imageOne = False
    pygame.display.update()

  '''while t > 0 and timerDelay == False:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    # display timer
    timerBg.draw()
    timerText = largeSans.render(timer, True, (0, 0, 0))
    screen.blit(timerText,[610,1]) 
    pygame.display.update()
    timerDelay = True
    time.sleep(1)
    timerDelay = False
    t -= 1'''
  
  if imageIndex == 1 and clocksIteration == True:
    imageList[imageIndex].draw()
    clockTimes[clockIndex].draw()
    leftArrow.draw()
    rightArrow.draw()
    hintButton.draw()
    #rightTriangleImage.draw()
    if leverState == False:
      leverOff.draw()
    if leverState == True:
      leverOn.draw()
    clocksIteration = False
    hint(hintClockText)
    pygame.display.update()

  if imageIndex == 2 and inventoryOpen == False: 
    '''if deskOpened == True:
      deskOpen.draw()
      leftArrow.draw()
      rightArrow.draw()
      hintButton.draw()
      pygame.display.update()
          
    if deskOpened == False:
      deskBg.draw()
      leftArrow.draw()
      rightArrow.draw()
      hintButton.draw()
      pygame.display.update()'''
    deskRect = pygame.Rect(365, 240, 160, 145)
    backButtonRect2 = pygame.Rect(10, 10, 30, 30)
    if deskRect.collidepoint(x, y):
      if keySelected == True and deskOpened == False:
        deskOpen.draw()
        print("Desk opened.")
        deskOpened = True
        leftArrow.draw()
        rightArrow.draw()
        inventory.remove("Key")
        #pygame.display.update()
      elif keySelected == False:
        print("You have not obtained the key yet")
    if deskOpened == True:
      print("Database here")
      bookDatabase.draw()
      backButton.draw()
      deskDatabase = True
      #pygame.display.update()

    if backButtonRect2.collidepoint(x, y) and deskOpened == True:
      screen.fill(BLACK)
      deskDatabase = False
      deskOpen.draw()
      leftArrow.draw()
      rightArrow.draw()

  #for all rooms

  for event in pygame.event.get():
      #pygame.quit() will run and close window
    print(event)
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      #This is to allow pressing the 'e' key to open the inv and then close it (should have a note telling the user this option)
      if inventoryOpen == True and event.key == pygame.K_e and zoomIn == False:
        print('E pressed while in inv')
        screen.fill((0, 0, 0, 0))
        if imageIndex == 1:
          clocksIteration = True
        imageList[imageIndex].draw()
        imageOne = True
        leftArrow.draw()
        rightArrow.draw()
        pygame.display.set_caption("Byrne Mansion")
        inventoryOpen = False
        
      elif inventoryOpen == False and menuOpen == False and event.key == pygame.K_e and zoomIn == False:
        print("E pressed")
        screen.fill((0, 0, 0,0))
        inventoryBackground.draw()
        inventoryIcon.draw()
        inventoryIcon2.draw()
        inventoryHotbar.draw()
        pygame.display.set_caption("Inventory")
        print("Inventory drawn")
        inventoryOpen = True
        inventoryBorder = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(197, 297, 300, 105), 2)
        inventoryTextThing.draw()
        pygame.display.update()
        try:
          if inventory[0] == 'Key':
            inventoryKey.draw()
            pygame.display.update()
        except:
          print("The key has not been obtained yet.")

        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      x, y = event.pos
      leftArrowRect = pygame.Rect(100, 200, 30, 30)
      rightArrowRect = pygame.Rect(540, 200, 30, 30)
      hintButtonRect = pygame.Rect(630, 10, 30, 30)
      startButtonRect = pygame.Rect(455, 100, 135, 50)
      optionsButtonRect = pygame.Rect(455, 180, 130, 50)
      rankingButtonRect = pygame.Rect(455, 260, 130, 50)
      exitButtonRect = pygame.Rect(455, 340, 130, 50)
      backButtonMenu = pygame.Rect(10, 10, 30, 30)

      if leftArrowRect.collidepoint(x, y) or rightArrowRect.collidepoint(x, y):
        inventoryOpen = False
                  
      if startButtonRect.collidepoint(x, y) and menuOpen == True:
        pygame.display.set_caption("Byrne Mansion")
        print("Start clicked")
        menuOpen = False
        experimental.scene0() #attempting to bring the cutscene over via importing
        pygame.display.update()
        if experimental.userNameEntered == True:
          imageIndex = 0
          print("Username entered")
          userName = experimental.userText
          imageOne = True
          #savingData()
        startClicked = True
        t = 1800
        timerDelay = False
      
      if exitButtonRect.collidepoint(x, y) and menuOpen == True and zoomIn == False:
        run = False

      if optionsButtonRect.collidepoint(x, y) and menuOpen == True and zoomIn == False:
        pygame.display.set_caption("Options")
        print("Placeholder options")
        optionsClicked = True
        menuOpen = False
        screen.fill((0, 0, 0, 0))
        backButton.draw()
        pygame.display.flip()

      if rankingButtonRect.collidepoint(x, y) and menuOpen == True and zoomIn == False:
        pygame.display.set_caption("Leaderboard")
        print("Placeholder leaderboard")
        leaderBoardClicked = True
        menuOpen = False
        screen.fill((0, 0, 0, 0))
        backButton.draw()
        pygame.display.flip()

      if backButtonMenu.collidepoint(x, y) and leaderBoardClicked == True:
        menuImage = True
        menuOpen = True
        leaderBoardClicked = False
        pygame.display.set_caption("Menu")
        pygame.display.flip()

      if backButtonMenu.collidepoint(x, y) and optionsClicked == True:
        menuImage = True
        menuOpen = True
        optionsClicked = False
        pygame.display.set_caption("Menu")
        pygame.display.update()
      
      if leftArrowRect.collidepoint(x, y) and menuOpen == False and zoomIn == False and inventoryOpen == False: 
        if imageIndex == 0:
          imageIndex = len(imageList) - 1
          screen.fill((0, 0, 0, 0))
          imageOne = True
          firstOpen = True
          print(imageIndex)
          pygame.display.update() 
          
        elif imageIndex == 2:
          imageIndex -= 1
          clocksIteration = True
          firstOpen = True
          print(imageIndex)
          
        else:
          imageIndex -= 1
          screen.fill((0, 0, 0, 0))
          firstOpen = True
          imageOne = True
          print(imageIndex)
          pygame.display.update()    
        
      if rightArrowRect.collidepoint(x, y) and menuOpen == False and zoomIn == False and inventoryOpen == False: 
        if imageIndex == len(imageList) - 1:
          imageIndex = 0
          screen.fill((0, 0, 0, 0))
          imageOne = True
          firstOpen = True
          print(imageIndex)
          pygame.display.update()     
          
        elif imageIndex == 0:
          imageIndex += 1       
          clocksIteration = True
          firstOpen = True
          print(imageIndex)    
          
        else:
          imageIndex += 1
          screen.fill((0, 0, 0, 0))
          firstOpen = True
          imageOne = True
          print(imageIndex)
          pygame.display.update()
      
      if hintButtonRect.collidepoint(x,y):
          hint(hintsList[hintIndex])
          print(hintsList[hintIndex])
          print("hint displayed")
          pygame.display.update()

      if imageIndex == 0 and startClicked == True:
        shelfOne = pygame.Rect(0, 70, 130, 110)
        shelfTwo = pygame.Rect(141, 0, 184, 300)
        shelfThree = pygame.Rect(331, 0, 194, 300)
        shelfFour = pygame.Rect(525, 60, 175, 120)
        backButtonRect = pygame.Rect(10, 10, 30, 30)

        if shelfOne.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
          print("Shelf one clicked")
          shelfZooms[0].draw()
          backButton.draw()
          pygame.display.update()
          zoomIn = True
          if firstOpen == True:
            zoomIn = False
            firstOpen = False
            #BibleRect = pygame.Rect(w, x, y, z)
          #if BibleRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False:
        """print("Bible clicked!")
          screen.fill((0, 0, 0, 0))

          inventory.append("inventoryBible")
          #pygame.mixer.Sound.play(inventoryDing)
          pygame.mixer.music.stop()
          inventory = list(set(inventory))
          print(inventory)"""
            
        if shelfTwo.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
          print("Shelf two clicked")
          shelfZooms[1].draw()
          backButton.draw()
          pygame.display.update()
          zoomIn = True
          if firstOpen == True:
            zoomIn = False
            firstOpen = False
            #BlanBookRect = pygame.Rect(w, x, y, z)
          #if BlankBookRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False:
        """print("Blank Book clicked!")
          screen.fill((0, 0, 0, 0))

          inventory.append("inventoryBlankBook")
          #pygame.mixer.Sound.play(inventoryDing)
          pygame.mixer.music.stop()
          inventory = list(set(inventory))
          print(inventory)"""
          
        if shelfThree.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
          print("Shelf three clicked")
          shelfZooms[2].draw()
          backButton.draw()
          pygame.display.update() 
          zoomIn = True
          if firstOpen == True:
            zoomIn = False
            firstOpen = False
        if shelfFour.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
          print("Shelf four clicked")
          shelfZooms[3].draw()
          backButton.draw()
          pygame.display.update()
          zoomIn = True
          if firstOpen == True:
            zoomIn = False
            firstOpen = False
            #DancingMenRect = pygame.Rect(w, x, y, z)
          #if DancingMenRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False:
        """print("The Adventures of the Dancing Men clicked!")
          screen.fill((0, 0, 0, 0))

          inventory.append("inventoryDancingMen")
          #pygame.mixer.Sound.play(inventoryDing)
          pygame.mixer.music.stop()
          inventory = list(set(inventory))
          print(inventory)
          if inventoryDancingMen.collidepoint(x, y) and inventoryOpen == True and ZoomIn == False and menuOpen == False:
            DancingMen.draw()
            if DancingMen.collidepoint(x, y)
            DancingMen.fill(Transparent)

"""
        if backButtonRect.collidepoint(x, y):
          imageOne = True
          zoomIn = False

      #clocks
      if imageIndex == 1:
        print("clock hint displayed")
        clockRect = pygame.Rect(280, 20, 120, 100)
        leverRect = pygame.Rect(435, 210, 65, 45)
        keyRect = pygame.Rect(485, 215, 110, 110)

        #runs when clock clicked
        if clockRect.collidepoint(x, y) and inventoryOpen == False:
          if clockIndex != 11:
            print("Clock time set to " + str(clockIndex+2) + ':00')
      
            
          else:
            print('Clock time set to ' + str(1) + ':00')
          if clockIndex == 11:
            clockIndex = 0
            clockTimes[clockIndex].draw()
            pygame.display.update()
          else:
            clockIndex+=1
            clockTimes[clockIndex].draw()
            pygame.display.update()
          
            
        #runs when lever clicked
        if leverRect.collidepoint(x, y) and inventoryOpen == False:
          clockTimes[clockIndex].draw()
          pygame.display.update()
          print("Lever clicked")
          if leverState == False:
            leverOn.draw()
            leverState = True
            if clockIndex == 4:
              mixer.Sound.play(clueClick)
              print("Correct!")
              keyImageButton.draw()
              hintClockText = "Clicking on the key will place it in your inventory. Press E to access your inventory."
              hint(hintClockText)
              hintClockText = "Good Job! There's nothing else to do on this side of the room..."
              hintIndex += 1
            else:
              print("Don't you dare to guess again!")
            pygame.display.update()
      
          elif leverState == True:
            leverOff.draw()
            pygame.display.update()
            leverState = False
          
          
      #adds key to inventory
        if keyRect.collidepoint(x, y) and clockIndex == 4 and inventoryOpen == False:
          print("Key clicked")
          screen.fill((0, 0, 0, 0))
          imageOne = True
          
          clocksIteration = True
          inventory.append("Key")
          mixer.Sound.play(inventoryDing)
          pygame.mixer.music.stop()
          inventory = list(set(inventory))
          print(inventory)
          pygame.display.update()

      #inventory
      if inventoryOpen == True:
        slotOneRect = pygame.Rect(196, 296, 45, 56)
        if slotOneRect.collidepoint(x, y):
          try:
            print("In the first slot, there is a " + inventory[0])
            keySelectedRect = pygame.draw.rect(screen, (220, 20, 60), pygame.Rect(0, 0, 700, 700), 2)
            keySelected = True
            print("Where does this key lead me?")
          except:
            print("There is nothing in that slot.")

      if imageIndex == 2:
        deskRect = pygame.Rect(365, 240, 160, 145)
        if deskRect.collidepoint(x, y):
          if keySelected == True and deskOpened == False:
            deskOpen.draw()
            print("Desk opened.")
            deskOpened = True
            leftArrow.draw()
            rightArrow.draw()
            pygame.display.update()
          if keySelected == False:
            print("You have not obtained the key yet")
          if deskOpened == True:
            print("Up view of desk here ;D")

pygame.quit()


"""
This if for the Arcostic Poem!
I will add the code you guys asked for here and we'll most likely edit the minor stuff such as the images and stuff later when we have it.

##Variables called
ArcosticButtonImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialogButton.jpeg")
# Created a variable which holds an image of the dialog
ArcosticImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialog.jpeg")

## Basically what gives the variables a visible output
ArcosticButtonImageObject = Button(1, 1, ArcosticButtonImageObject, 0.05)
ArcosticImageObject = Button(100, screenHeight / 8, ArcosticImageObject, 1.6)
##

#will go inside of the run loop
ArcosticButtonImageObject.draw()
#

###Button creation
ArcosticButtonRect = pygame.Rect(1, 1, 64, 36)
###

#### Basically the button which we created when clicked will collide with the (x, y) which'll cause the Arcostic Image which is the poem to draw itself onto the user's screen. 
if ArcosticButtonRect.collidepoint(x, y):
                ArcosticImageObject.draw()
####

That's about it. idk where we're going to put it, but it's there
"""
"""
clicking sound code:

      pygame.mixer.music.play( whatever the file name for the clicking sound goes here )

just add it to the places where its needed. I didn't do that
############################################################################################################################################################################################################
when you need the moving bookshelves sound do the same code but with a different file name inside the paranthesis. It should work if not tell me (Osvaldo) and ill fix it.
############################################################################################################################################################################################################
      """

"""
#I renamed the deskBg to the new image which is technically the zoomed in version but i think it works best in contrast to the other one. I don't have any idea of where to put the code. So please do that for me. Thank you - Osvaldo
DeskLockRect = pygame.Rect(480, 360, 30, 30)

if DeskLockRect == imageList[2][0] and keySelected == True and DeskLockRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
  DeskOpen.draw()
  DeskFile.draw()
else:
  print("You need a key to unlock this desk.")
  print("If you have the key, you have to grab it from your inventory. Then try to open the desk.")
  


"""