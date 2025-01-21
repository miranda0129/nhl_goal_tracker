import pygame
from time import sleep

TEAM_ABBREV = 'DET'
TIME_ZONE = 'US/Eastern'

class Display:
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 62) 
        self.screen = pygame.display.set_mode((480, 320))
        self.redColour = (255, 19, 0)
        self.whiteColour = (255, 255, 255)
        self.boldFont = pygame.font.Font(None, 99) 

    def getStartY(self, text_lines):
        # Calculate the total height of all lines
        line_spacing = self.font.get_linesize()  # Spacing between lines
        total_text_height = len(text_lines) * line_spacing
        split_divider = len(text_lines) if len(text_lines) > 1 else 2

        # Calculate the starting y-coordinate to center the text vertically
        start_y = (self.screen.get_height() - total_text_height) // split_divider
        return start_y
    
    def writeToScreen(self, text_lines, font):
        y = self.getStartY(text_lines)  
        for line in text_lines:
            text_surface = font.render(line, True, self.redColour)
            text_rect = text_surface.get_rect(centerx=self.screen.get_width() // 2, y=y)  # Position each line
            self.screen.blit(text_surface, text_rect)
            y += 80  # Move to the next line (adjust based on font size and spacing)

    def writeToScreenFlipColour(self, text_lines, font):
        y = self.getStartY(text_lines)  
        for line in text_lines:
            text_surface = font.render(line, True, self.whiteColour)
            text_rect = text_surface.get_rect(centerx=self.screen.get_width() // 2, y=y)  # Position each line
            self.screen.blit(text_surface, text_rect)
            y += 80  # Move to the next line (adjust based on font size and spacing)
    
    def displayGoal(self):
        text_lines = ["GOAL!!"]

        for counter in range (0, 3):
            self.screen.fill((255, 255, 255))
            self.writeToScreen(text_lines, self.boldFont)
            pygame.display.flip()
            sleep(1)
            self.screen.fill(self.redColour)        
            self.writeToScreenFlipColour(text_lines, self.boldFont)
            pygame.display.flip()
            sleep(1)

    def displayScore(self, score_matrix, team_matrix):
        text_lines = [
            "{} v {}".format(team_matrix[0], team_matrix[1]),
            "{} : {}".format(score_matrix[0], score_matrix[1])
          ]
        self.writeToScreen(text_lines, self.boldFont)
        pygame.display.flip()

    def displayNextGame(self, nextGameTime):
        splitStrings = nextGameTime.split(',')
        date = splitStrings[0]
        time = splitStrings[1]
        text_lines = [
            "The next game is ",
            "{} at ".format(date),
            time
        ]
        self.writeToScreen(text_lines, self.font)
        pygame.display.flip()

    def displayTodayGame(self, nextGameTime):
        splitStrings = nextGameTime.split(',')
        time = splitStrings[1]
        text_lines = [
            "The next game is ",
            "today at ",
            time
        ]
        self.writeToScreen(text_lines, self.font)
        pygame.display.flip()



