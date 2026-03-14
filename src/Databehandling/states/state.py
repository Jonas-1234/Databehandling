# utils.py

import pygame as pg
import sys
import matplotlib.pyplot as plt
from utilities import Button
from utilities import Slider
from settings import colors

class Menu:
    """ Menu
    """
    def __init__(self):
        self.axis_title = True
        self.legend = True
        self.average = True
        self.grid = True

        self.buttons = [
            Button((100, 50), "Aksetitler", colors["Black"], 24, None, (110, 110), colors["Blue"], "axis_title", True),
            Button((100, 175), "Legend", colors["Black"], 24, None, (110, 110), colors["Blue"], "legend", True),
            Button((100, 300), "Gjennomsnitt", colors["Black"], 24, None, (110, 110), colors["Blue"], "average", True),
            Button((100, 425), "Grid", colors["Black"], 24, None, (110, 110), colors["Blue"], "grid", True),
            Button((650, 425), "Plott", colors["Black"], 24, None, (250, 110), colors["Green"], "plot", False)
        ]

        self.slider = Slider(300, 20, 300, 400, colors["Red"], ["test", "test", "test"])

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.click(pg.mouse.get_pos()):
                        if button.returnValue == "axis_title":
                            self.axis_title = not self.axis_title
                            print(self.axis_title)
                        elif button.returnValue == "legend":
                            self.legend = not self.legend
                            print(self.legend)
                        elif button.returnValue == "average":
                            self.average = not self.average
                            print(self.average)
                        elif button.returnValue == "grid":
                            self.grid = not self.grid
                            print(self.grid)
                        elif button.returnValue == "plot":
                            self.plot(self.axis_title, self.legend, self.average, self.grid)

        self.slider.drag_slider()
    
    def draw(self, screen):
        screen.fill((200, 200, 200))
        for button in self.buttons:
            button.draw(screen)
        
        self.slider.draw(screen)

    def plot(self, axis_title, legend, average, grid):
        print("plotting graph")