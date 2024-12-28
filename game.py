import pygame
from NextGame import NextGame
from time import sleep

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'

class Display:
    def __init__(self) -> None:
        pygame.init()
        self.font = pygame.font.Font(None, 74) 
        self.screen = pygame.display.set_mode((600, 400))
        self.redColour = (255, 19, 0)

    def getStartY(self, text_lines):
        # Calculate the total height of all lines
        line_spacing = self.font.get_linesize()  # Spacing between lines
        total_text_height = len(text_lines) * line_spacing

        # Calculate the starting y-coordinate to center the text vertically
        start_y = (self.screen.get_height() - total_text_height) // 2
        return start_y
    
    def writeToScreen(self, text_lines):
        y = start_y  
        for line in text_lines:
            text_surface = font.render(line, True, self.redColour)
            text_rect = text_surface.get_rect(centerx=self.screen.get_width() // 2, y=y)  # Position each line
            display.screen.blit(text_surface, text_rect)
            y += 40  # Move to the next line (adjust based on font size and spacing)
    
    def displayGoal(self):
        text_lines = ["GOAL!!"]
        self.writeToScreen(text_lines)
        

nextGame = NextGame(TEAM_ABBREV)
nextGame.getNextGame()

isGameToday = nextGame.isNextGameToday()
gameTime = nextGame.getTime()
gameId = nextGame.nextGameId

print("The wings are playing next at...", gameTime)
print("Game Id: ", gameId)

display = Display()
font = pygame.font.Font(None, 74)  # Use default font, size 74
game_time_text_lines = [
    "The next game is at ",
    gameTime.strftime("%B %d, %H:%M")
]

start_y = display.getStartY(game_time_text_lines)
counter = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    display.screen.fill((255, 255, 255))  # white background
    
    print("doing other work")
    counter += 1
    sleep(1)

    if (counter > 5):
        if ((counter%5) == 0):
            display.displayGoal()
        else:
          text_lines = [
            "{} : {}".format(counter, counter)
          ]
          display.writeToScreen(text_lines)
    else:
        display.writeToScreen(game_time_text_lines)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()



