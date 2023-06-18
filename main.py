import pygame
import math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Basketball Simulator')
clock = pygame.time.Clock()

FPS = 60
active = True
simulation = False
over = False
font = pygame.font.Font(None, 32)
g = 9.8
res = 0.86
backboard_res = 0.65
rim_res = 0.6

ball_diameter = 24
ball_radius = ball_diameter/2

backboard_height = 152

degree = 45
velocity = 5

# vyarray = []
# v0x = velocity*math.cos(r)
# v0y = velocity*math.sin(r)
# vyarray.append(v0y)

height = 600
length = 800

court_surf = pygame.image.load("graphics/court.jpg").convert()
court_rect = court_surf.get_rect(topleft=(0, 0))

backboard = pygame.image.load("graphics/test.jpg").convert_alpha()
backboard_surf = pygame.transform.scale(backboard, (10, backboard_height))
backboard_rect = court_surf.get_rect(topleft=(1495, 335))

rim1 = pygame.image.load("graphics/test.jpg").convert_alpha()
rim1_surf = pygame.transform.scale(rim1, (15.1, 1.6))
rim1_rect = rim1_surf.get_rect(topleft=(1480, 444))

rim2 = pygame.image.load("graphics/test.jpg").convert_alpha()
rim2_surf = pygame.transform.scale(rim2, (1.6, 1.6))
rim2_rect = rim2_surf.get_rect(topleft=(1434.28, 444))

minusheight_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minusheight_rect = minusheight_surf.get_rect(center=(680, 850))

addheight_surf = pygame.image.load("Sprites/add.png").convert_alpha()
addheight_rect = addheight_surf.get_rect(center=(780, 850))

minuslength_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minuslength_rect = minuslength_surf.get_rect(center=(430, 850))

addlength_surf = pygame.image.load("Sprites/add.png").convert_alpha()
addlength_rect = addlength_surf.get_rect(center=(530, 850))

minusdegree_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minusdegree_rect = minusdegree_surf.get_rect(center=(930, 850))

adddegree_surf = pygame.image.load("Sprites/add.png").convert_alpha()
adddegree_rect = adddegree_surf.get_rect(center=(1030, 850))

minusvelocity_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minusvelocity_rect = minusvelocity_surf.get_rect(center=(1180, 850))

addvelocity_surf = pygame.image.load("Sprites/add.png").convert_alpha()
addvelocity_rect = addvelocity_surf.get_rect(center=(1280, 850))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #In game controls
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    heightframe = 0
                    lengthframe = 0
                    r = math.radians(degree)
                    vyarray = []
                    vxarray = []
                    v0x = velocity*math.cos(r)
                    v0y = velocity*math.sin(r)
                    vyarray.append(v0y)
                    vxarray.append(v0x)
                    active = False
                    simulation = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and addheight_rect.collidepoint(pygame.mouse.get_pos()) and height > 0:
                    height -= 1
                if mouse_presses[0] and minusheight_rect.collidepoint(pygame.mouse.get_pos()) and height < 800:
                    height += 1
                if mouse_presses[0] and addlength_rect.collidepoint(pygame.mouse.get_pos()):
                    length -= 1
                if mouse_presses[0] and minuslength_rect.collidepoint(pygame.mouse.get_pos()):
                    length += 1
                if mouse_presses[0] and adddegree_rect.collidepoint(pygame.mouse.get_pos()) and degree <= 90:
                    degree += 1
                if mouse_presses[0] and minusdegree_rect.collidepoint(pygame.mouse.get_pos()) and degree >= 0:
                    degree -= 1
                if mouse_presses[0] and addvelocity_rect.collidepoint(pygame.mouse.get_pos()):
                    velocity += 1
                if mouse_presses[0] and minusvelocity_rect.collidepoint(pygame.mouse.get_pos()) and velocity >= 0:
                    velocity -= 1
        if simulation:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and over:
                    height = 600
                    length = 800
                    degree = 45
                    velocity = 5
                    heightframe = 0
                    lengthframe = 0
                    vyarray = []
                    vxarray = []
                    active = True
                    simulation = False
                    over = False
                    
    if active:
        screen.blit(court_surf, court_rect)

        arrow = pygame.image.load("Sprites/arrow.png").convert_alpha()
        arrow_surf = pygame.transform.scale(arrow, (200, 75))
        arrow_surf_degree = pygame.transform.rotate(arrow_surf, degree)
        arrow_rect = arrow_surf_degree.get_rect(midleft=(length, height))
        screen.blit(arrow_surf_degree, arrow_rect)

        height_surf = font.render("height= "+str(height)+"cm", False, "White", "Black")
        height_rect = height_surf.get_rect(center=(720, 750))
        screen.blit(height_surf, height_rect)

        length_surf = font.render("length= "+str(length)+"cm", False, "White", "Black")
        length_rect = length_surf.get_rect(center=(480, 750))
        screen.blit(length_surf, length_rect)

        degree_surf = font.render("degree= "+str(degree)+"", False, "White", "Black")
        degree_rect = degree_surf.get_rect(center=(970, 750))
        screen.blit(degree_surf, degree_rect)

        velocity_surf = font.render("velocity= "+str(velocity)+"m/s", False, "White", "Black")
        velocity_rect = velocity_surf.get_rect(center=(1230, 750))
        screen.blit(velocity_surf, velocity_rect)

        screen.blit(minusheight_surf,minusheight_rect)
        screen.blit(addheight_surf,addheight_rect)
        screen.blit(minuslength_surf,minuslength_rect)
        screen.blit(addlength_surf,addlength_rect)
        screen.blit(minusdegree_surf,minusdegree_rect)
        screen.blit(adddegree_surf,adddegree_rect)
        screen.blit(minusvelocity_surf,minusvelocity_rect)
        screen.blit(addvelocity_surf,addvelocity_rect)

        basketball_surf = pygame.image.load("Sprites/basketball.png").convert_alpha()
        basketball_hitbox = pygame.transform.scale(pygame.image.load("Sprites/basketball.png").convert_alpha(),(24,24))
        basketball_rect = basketball_surf.get_rect(center=(length, height))
        basketball_hitbox_rect = basketball_hitbox.get_rect(center=(length, height))
        basketball_hitbox_rect.centerx = basketball_rect.centerx
        basketball_hitbox_rect.centery = basketball_rect.centery
        screen.blit(basketball_surf,basketball_rect)
        screen.blit(basketball_hitbox, basketball_hitbox_rect)

    if simulation:
        heightframe += 1
        lengthframe += 1
        heighttime = heightframe/60
        lengthtime = lengthframe/60
        # r = math.radians(degree)
        # v0x = velocity*math.cos(r)
        # v0y = velocity*math.sin(r)

        # vyarray.append(v0y)
        # heightperframe = (((height/100)-(v0y*time))+(((g)*math.pow(time,2))/2))*100
        heightperframe = (((height/100)-(vyarray[len(vyarray)-1]*heighttime))+(((g)*math.pow(heighttime,2))/2))*100
        lengthperframe = ((length/100) + (vxarray[len(vxarray)-1]*lengthtime))*100
        # vy = -v0y + g*time
        vy = (-vyarray[len(vyarray)-1] + g*heighttime)
        vx = vxarray[len(vxarray)-1]


        screen.blit(court_surf, court_rect)
        screen.blit(backboard_surf, backboard_rect)
        screen.blit(rim1_surf, rim1_rect)
        screen.blit(rim2_surf, rim2_rect)

        if heightperframe > (750-ball_radius):
            vy = (-vyarray[len(vyarray)-1] + g*heighttime)*res
            vyarray.append(vy)
            heightframe = 0
            height = 750-ball_radius
            print(vyarray[len(vyarray)-1])
            print(len(vyarray))

        # if basketball_rect.colliderect(backboard_rect):
        if 1495 > lengthperframe > (1495-ball_radius) and 335+backboard_height > heightperframe > 335:
            vx = -((vxarray[len(vxarray)-1])*backboard_res)
            vxarray.append(vx)
            lengthframe = 0
            length = 1495-ball_radius


         

        # heightperframe_surf = font.render("height= "+str('{0:.4g}'.format(heightperframe))+"cm", False, "White", "Black")
        # heightperframe_rect = heightperframe_surf.get_rect(center=(720, 750))
        # screen.blit(heightperframe_surf, heightperframe_rect)

        # lengthperframe_surf = font.render("length= "+str('{0:.4g}'.format(lengthperframe))+"cm", False, "White", "Black")
        # lengthperframe_rect = lengthperframe_surf.get_rect(center=(480, 750))
        # screen.blit(lengthperframe_surf, lengthperframe_rect)

        yvelocityperframe_surf = font.render("y velocity= "+str('{0:.4g}'.format(-vy))+"m/s", False, "White", "Black")
        yvelocityperframe_rect = yvelocityperframe_surf.get_rect(center=(720, 750))
        screen.blit(yvelocityperframe_surf, yvelocityperframe_rect)

        xvelocityperframe_surf = font.render("x velocity= "+str('{0:.4g}'.format(vx))+"m/s", False, "White", "Black")
        xvelocityperframe_rect = xvelocityperframe_surf.get_rect(center=(480, 750))
        screen.blit(xvelocityperframe_surf, xvelocityperframe_rect)

        basketball_surf = pygame.image.load("Sprites/basketball.png").convert_alpha()
        basketball_hitbox = pygame.transform.scale(pygame.image.load("Sprites/basketball.png").convert_alpha(),(24,24))
        basketball_rect = basketball_surf.get_rect(center=(lengthperframe, heightperframe))
        basketball_hitbox_rect = basketball_hitbox.get_rect(center=(lengthperframe, heightperframe))
        basketball_hitbox_rect.centerx = basketball_rect.centerx
        basketball_hitbox_rect.centery = basketball_rect.centery
        screen.blit(basketball_surf,basketball_rect)
        screen.blit(basketball_hitbox, basketball_hitbox_rect)

        if basketball_hitbox_rect.centery > 750-ball_radius:
            over = True
            print(over)

        # if over:
        #     #basketball_rect.centery += basketball_gravity
        #     basketball_surf = pygame.image.load("Sprites/basketball.png").convert_alpha()
        #     basketball_hitbox = pygame.transform.scale(pygame.image.load("Sprites/basketball.png").convert_alpha(),(24,24))
        #     basketball_rect = basketball_surf.get_rect(center=(length, height))
        #     basketball_hitbox_rect = basketball_hitbox.get_rect(center=(length, height))
        #     basketball_hitbox_rect.centerx = basketball_rect.centerx
        #     basketball_hitbox_rect.centery = basketball_rect.centery

        

    pygame.display.update()
    clock.tick(FPS)