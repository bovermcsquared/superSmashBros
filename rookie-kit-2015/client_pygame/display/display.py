#
# This file is where you make the display for your game
# Make changes and add functions as you need.
#

import pygame
from config import *
from common.event import *
from client.base_display import BaseDisplay
from spritesheet import Spritesheet
import random
import os


class Display(BaseDisplay):
    """
    This class controls all of the drawing of the screen
    for your game.  The process of drawing a screen is
    to first draw the background, and then draw everything
    that goes on top of it.  If two items are drawn in the
    same place, then the last item drawn will be the one
    that is visible.

    The screen is a 2 dimensional grid of pixels, with the
    origin (0,0) located at the top-left of the screen, and
    x values increase to the right and y values increase as
    you go down.  The y values are opposite of what you learned
    in your math classes.

    Documentation on drawing in pygame is available here:
    http://www.pygame.org/docs/ref/draw.html

    The methods in this class are:
    __init__ creates data members (variables) that are used
        in the rest of the methods of this class.  This is
        useful for defining colors and sizes, loading image
        or sound files, creating fonts, etc.  Basically,
        any one time setup.

    paint_game controls the drawing of the screen while the
        game is in session.  This is responsible for making
        sure that any information, whether graphics, text, or
        images are drawn to the screen.

    paint_waiting_for_game controls the drawing of the screen
        after you have requested to join a game, but before
        the game actually begins.
    
    paint_game_over controls the drawing of the screen after
        the game has been won, but before the game goes away.
        This is a short (3-5 second) period.

    process_event controls handling events that occur in the
        game, that aren't represented by objects in the game
        engine.  This includes things like collisions,
        objects dying, etc.  This would be a great place to
        play an audio file when missiles hit objects.

    paint_pregame controls the drawing of the screen before
        you have requested to join a game.  This would usually
        allow the user to know the options available for joining
        games.

    Method parameters and data members of interest in these methods:
    self.width is the width of the screen in pixels.
    self.height is the height of the screen in pixels.
    self.* many data members are created in __init__ to set up
        values for drawing, such as colors, text size, etc.
    surface is the screen surface to draw to.
    control is the control object that is used to
        control the game using user input.  It may
        have data in it that influences the display.
    engine contains all of the game information about the current
        game.  This includes all of the information about all of
        the objects in the game.  This is where you find all
        of the information to display.
    event is used in process_event to communicate what
        interesting thing occurred.
    
    Note on text display:  There are 3 methods to assist
    in the display of text.  They are inherited from the
    BaseDisplay class.  See client/base_display.py.
    
    """

    def __init__(self, width, height):
        """
        Configure display-wide settings and one-time
        setup work here.
        """
        BaseDisplay.__init__(self, width, height)

        # There are other fonts available, but they are not
        # the same on every computer.  You can read more about
        # fonts at http://www.pygame.org/docs/ref/font.html
        self.font_size = 12
        self.font = pygame.font.SysFont("Courier New",self.font_size)

        # Colors are specified as a triple of integers from 0 to 255.
        # The values are how much red, green, and blue to use in the color.
        # Check out http://www.colorpicker.com/ if you want to try out
        # colors and find their RGB values.   Be sure to use the `R`, `G`,
        # `B` values at the bottom, not the H, S, B values at the top.
        self.player_color     = (0, 255, 0)
        self.opponent_color   = (255, 0, 0)
        self.missile_color    = (0, 255, 255)
        self.npc_color        = (255, 255, 0)
        self.wall_color       = (255, 255, 255)
        self.text_color       = (255, 255, 255)
        self.background_color = (0, 0, 0)
        buttonF = 'code camp buttons.png'
        sheet = Spritesheet(buttonF)

        
        self.tourneyB = sheet.image_at(pygame.Rect(5,5,200,97),(255,255,255))
        self.singleB = sheet.image_at(pygame.Rect(5,134,200,97),(255,255,255))
        self.dualB = sheet.image_at(pygame.Rect(5,264,200,97),(255,255,255))
        self.demoB = sheet.image_at(pygame.Rect(5,394,200,97),(255,255,255))

        # self.logo = pygame.image.load("display\imgs\game pngs '\code camp logo-01")


        self.filenames = ["code camp kirby-01.png", "code camp kirby-02.png", "code camp link-01-01.png", "code camp link-02-01.png", "code camp mario-01.png","code camp mario-04.png", "code camp mario-02.png","code camp mario-03.png"]
        self.imgs = []

        self.filename2 = ["code camp castle small.png", "forest background code camp small.png", "haunted house code camp small.png"]
        self.arena = []

        self.filenames2 = ["code camp logo-01.png"]
        self.logo = []


        for f in self.filenames:
            f = os.path.join('display','imgs',f)
            self.imgs.append(pygame.image.load(f))

        for a in self.filename2:
            a = os.path.join("display","imgs",a)
            self.arena.append(pygame.image.load(a))


        for l in self.filenames2:
            l = os.path.join("display", "imgs", l)
            self.logo.append(pygame.image.load(l))


        # playerStates {'walk':['walk','walkdown','walkleft','walkup','walkright'],'throw':['throw','throwdown','throwleft','throwup','throwright'], 'death':['death'],'victory':['victory'],'hp':['victory']}

        # filename = os.path.join('display', 'imgs', 'Link Sprites with coordinates.png')
        # self.image = pygame.image.load(filename)
        # self.rect = self.obj_to_rect(obj)
        # self.image = pygame.image.load(filename)
        # ss = Spritesheet(filename)
        # for s in playerStates:
            # if len(s) == 1:

            # for d in s:
                # if len()
                

        # playerStates {'walk':['walkdown','walkleft','walkup','walkright'],'throw':['throwdown','throwleft','throwup','throwright'], 'death':['death'],'victory':['victory'],'hp':['victory']}

        
        # self.image = pygame.image.load(filename)
        # self.rect = self.obj_to_rect(obj)
        # self.image = pygame.image.load(filename)
        

        
       
        return

        


    def paint_pregame(self, surface, control):
        """
        Draws the display before the user selects the game type.
        """
        # background

        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill( (0,155,0), rect)

        logo = self.logo[0]
        
        surface.blit(logo,(30,3))


        count = 0
        x = 0
        for i in control.yourcharacters:
            if i[1]:
                color = (255,255,0)
                time = pygame.time.get_ticks()
                print time
                time = time%500
                if time <250:
                    img = self.imgs[x]

                else:
                    img = self.imgs[x + 1]
            elif i[2]:
                color = (255,255,255)
                time = pygame.time.get_ticks()
                time = time%500
                if time <250:
                    img = self.imgs[x]
                else:
                    img = self.imgs[x + 1]
            else:
                color= COLORS[count]
                img = self.imgs[x]
            count +=1
            x += 2           
            surface.blit(img,i[0])
            

        count = 0
        x = 0
        for i in control.enemycharacters:
            if i[1]:
                color = (255,255,0)
                time = pygame.time.get_ticks()
                print time
                time = time%500
                if time <250:
                    img = self.imgs[x]

                else:
                    img = self.imgs[x + 1]
            elif i[2]:
                color = (255,255,255)
                time = pygame.time.get_ticks()
                time = time%500
                if time <250:
                    img = self.imgs[x]
                else:
                    img = self.imgs[x + 1]
            else:
                color= COLORS[count]
                img = self.imgs[x]
            count +=1
            x += 2
                       
            surface.blit(img,i[0])
            

         
            

        x=0
        count = 0
        for i in control.arenacharacters:
            if i[1]:
                color = (255,255,0)
                arena = self.arena[x]
            elif i[2]:
                color = (255,255,255)
                arena = self.arena[x]
            else:
                color= COLORS[count]
                arena = self.arena[x]
            count +=1
            x +=1

            surface.blit(arena, i[0])

        # surface.blit(pygame.image.load('display/imgs/code camp buttons.png'), (0,0))
            

        if control.arenaSelected and control.charSelected and control.foeSelected:
            surface.blit(self.tourneyB,control.tourneyR)
            surface.blit(self.singleB,control.singleR)
            surface.blit(self.dualB,control.dualR)
            surface.blit(self.demoB,control.demoR)

        

        # pygame.draw.rect(surface, (0,255,0), rect1, 0)
        # text message in center of screen
          
        # s = "Press 'd' for dual player, 'q' for single player,"
        # self.draw_text_center(surface, s, self.text_color,
        #                       self.width/2, self.height/2,
        #                       self.font)
        # s = "'t' for tournament, 'esc' to quit."
        # self.draw_text_center(surface, s, self.text_color,
        #                       self.width/2, self.height/2 + 3*self.font_size/2,
        #                       self.font)
        return
        
    def paint_waiting_for_game(self, surface, engine, control):
        """
        Draws the display after user selects the game type, before the game begins.
        This is usually a brief period of time, while waiting for an opponent
        to join the game.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)
        # surface.blit(self.logo, (0,0))
        # text message in center of screen
        s = "Waiting for opponent to connect."
        self.draw_text_center(surface, s, self.text_color,
                              self.width/2, self.height/2,
                              self.font)
        return

    def paint_game(self, surface, engine, control):
        """
        Draws the display after the game starts.
        """
        # print "went to paint"
        # background
        # clock = pygame.time.Clock()
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)

            
        # draw each object
        objs = engine.get_objects()
        for key in objs:
            obj = objs[key]
            if obj.is_wall():
                self.paint_wall(surface, engine, control, obj)
            elif obj.is_npc():
                self.paint_npc(surface, engine, control, obj)
            elif obj.is_missile():
                self.paint_missile(surface, engine, control, obj)
            elif obj.is_player():
                # tick = pygame.time.get_ticks()
                # i = 0                
                # self.paint_player(surface, engine, control, obj, self.char[0][0])
                # img = self.char[0][0]
                # print control.char.get_row(0)
                cycle = control.char.get_row(0) * CHAR_SPEED
                # print cycle
                step = self.tick(obj,cycle)
                img = control.char.find_sprite_direction(obj.get_rotation(), step)

                width = obj.get_pw()
                height = obj.get_ph()
                img = pygame.transform.scale(img, (width, height))
                self.paint_player(surface, engine, control, obj, img)


            else:
                print "Unexpected object type: %s" % (str(obj.__class__))
                
        # draw game data
        
        self.paint_game_status(surface, engine, control)
        return

    def tick(self, obj, cycle):
        
        step = int((obj.get_distance()%cycle)/6)
        # print "step",step

        return step

    
            



        
    def paint_game_over(self, surface, engine, control):
        """
        Draws the display after the game ends.  This
        chooses to display the game, and add a game over
        message.
        """
        self.paint_game(surface, engine, control)
        
        s = "Game Over (%s wins!)" % (engine.get_winner_name())
        self.draw_text_center(surface, s, self.text_color, int(self.width/2), int(self.height/2), self.font)
        return

    def process_event(self, surface, engine, control, event):
        """
        Should process the event and decide if it needs to be displayed, or heard.
        """
        return

    # The following methods draw appropriate rectangles
    # for each of the objects, by type.
    # Most objects have an optional text display to
    # demonstrate how to send information from the control
    # to the display.
    def paint_wall(self, surface, engine, control, obj):
        """
        Draws walls.
        """
        rect = self.obj_to_rect(obj)
        pygame.draw.rect(surface, self.wall_color, rect)
        return
        
    def paint_npc(self, surface, engine, control, obj):
        """
        Draws living NPCs.
        """
        if obj.is_alive():
            color = self.npc_color
            rect = self.obj_to_rect(obj)
            pygame.draw.rect(surface, color, rect)
        return
        
    def paint_missile(self, surface, engine, control, obj):
        """
        Draws living missiles.
        """
        if obj.is_alive():
            color = self.missile_color
            rect = self.obj_to_rect(obj)
            pygame.draw.rect(surface, color, rect)
        return
        
    def paint_player(self, surface, engine, control, obj, img):
        """
        Draws living players.
        My player is my opponent are in different colors
        """
        if obj.is_alive():
            rect = self.obj_to_rect(obj)
            if obj.get_oid() == engine.get_player_oid():
                color = self.player_color
            else:
                color = self.opponent_color
            surface.blit(img, (obj.get_px(),obj.get_py()))
        return

    def paint_game_status(self, surface, engine, control):  
        """
        This method displays some text in the bottom strip
        of the screen.  You can make it do whatever you want,
        or nothing if you want.
        """

        # display my stats
        oid = engine.get_player_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Me: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 3 * self.font_size / 2
                self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                
        # display opponent's stats
        oid = engine.get_opponent_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Opponent: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_opponent_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 6 * self.font_size / 2
                self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
        return

class Confetti:
    def __init__(self, limit):
        tile = pygame.Rect(0,0,896,640)
        # print tile
        decoTemp = []
        self.imgs = [(tile, (111,111,111))]
        
        for i in range(limit):
            x = random.randint(15, 881)
            y= random.randint(15, 635)
            # decoInt = random.randint(len(objs))
            deco = pygame.Rect(x,y,5,5)
            c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.imgs.append((deco,c))

    def paint_bg(self, surface):
        
        for i in self.imgs:
            # print i[0]
            pygame.draw.rect(surface, i[1],i[0])