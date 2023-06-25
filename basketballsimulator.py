import pygame
import math
from pygame.math import Vector2
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

attempts = 0
score = 0
miss = 0

ball_diameter = 24
ball_radius = ball_diameter/2

backboard_height = 152

degree = 45
velocity = 5

floor_y = 750
rim_height = 305
rim_diameter = 45.72
rim_radius = rim_diameter/2

rim1_pos = Vector2(1480, floor_y - rim_height)
rim2_pos = Vector2(1480 - rim_diameter , floor_y - rim_height)
backboard_pos = Vector2(1495, 335)

# height = 338
height = floor_y - 200 - ball_radius
# distance = 960
distance = rim2_pos[0] - 396

height_display = floor_y - ball_radius - height
distance_display = rim2_pos[0] - distance


court_surf = pygame.image.load("graphics/court.jpg").convert()
court_rect = court_surf.get_rect(topleft=(0, 0))

backboard = pygame.image.load("graphics/blank.png").convert_alpha()
backboard_surf = pygame.transform.scale(backboard, (10, backboard_height))
backboard_rect = court_surf.get_rect(topleft=(backboard_pos))

rim1 = pygame.image.load("graphics/test.jpg").convert_alpha()
rim1_surf = pygame.transform.scale(rim1, (15.1, 1.6))
rim1_rect = rim1_surf.get_rect(topleft=(rim1_pos))

rim2 = pygame.image.load("graphics/test.jpg").convert_alpha()
rim2_surf = pygame.transform.scale(rim2, (1.6, 1.6))
rim2_rect = rim2_surf.get_rect(topleft=(rim2_pos))

minusheight_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minusheight_rect = minusheight_surf.get_rect(center=(680, 850))

addheight_surf = pygame.image.load("Sprites/add.png").convert_alpha()
addheight_rect = addheight_surf.get_rect(center=(780, 850))

minusdistance_surf = pygame.image.load("Sprites/minus.png").convert_alpha()
minusdistance_rect = minusdistance_surf.get_rect(center=(430, 850))

adddistance_surf = pygame.image.load("Sprites/add.png").convert_alpha()
adddistance_rect = adddistance_surf.get_rect(center=(530, 850))

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
                    # Initiate variables for the simulation run
                    attempts += 1
                    scored = False
                    heightframe = 0
                    distanceframe = 0
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
                if mouse_presses[0] and addheight_rect.collidepoint(pygame.mouse.get_pos()) and height > 450-ball_radius:
                    height -= 1
                if mouse_presses[0] and minusheight_rect.collidepoint(pygame.mouse.get_pos()) and height < 750-ball_radius:
                    height += 1
                if mouse_presses[0] and adddistance_rect.collidepoint(pygame.mouse.get_pos()):
                    distance -= 1
                    distance_display += 1
                if mouse_presses[0] and minusdistance_rect.collidepoint(pygame.mouse.get_pos()):
                    distance += 1
                    distance_display += 1
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
                    if scored:
                        score += 1
                    else:
                        miss += 1
                    # Restarts the variables
                    height = 538
                    distance = rim2_pos[0] - 396
                    distance_display = rim2_pos[0] - distance
                    degree = 45
                    velocity = 5
                    heightframe = 0
                    distanceframe = 0
                    vyarray = []
                    vxarray = []
                    active = True
                    simulation = False
                    over = False
                    scored = False
                    
    if active:
        screen.blit(court_surf, court_rect)

        arrow = pygame.image.load("Sprites/arrow.png").convert_alpha()
        arrow_surf = pygame.transform.scale(arrow, (200, 75))
        arrow_surf_degree = pygame.transform.rotate(arrow_surf, degree)
        arrow_rect = arrow_surf_degree.get_rect(midleft=(distance, height))
        screen.blit(arrow_surf_degree, arrow_rect)

        scored_surf = font.render("scored= "+str(score), False, "White", "Black")
        scored_rect = scored_surf.get_rect(center=(720, 200))
        screen.blit(scored_surf, scored_rect)

        missed_surf = font.render("missed= "+str(miss), False, "White", "Black")
        missed_rect = missed_surf.get_rect(center=(480, 200))
        screen.blit(missed_surf, missed_rect)

        attempts_surf = font.render("attempts= "+str(attempts), False, "White", "Black")
        attempts_rect = attempts_surf.get_rect(center=(330, 200))
        screen.blit(attempts_surf, attempts_rect)

        height_surf = font.render("height= "+str(height_display)+"cm", False, "White", "Black")
        height_rect = height_surf.get_rect(center=(720, 750))
        screen.blit(height_surf, height_rect)

        distance_surf = font.render("distance= "+str(distance_display)+"cm", False, "White", "Black")
        distance_rect = distance_surf.get_rect(center=(480, 750))
        screen.blit(distance_surf, distance_rect)

        degree_surf = font.render("degree= "+str(degree)+"", False, "White", "Black")
        degree_rect = degree_surf.get_rect(center=(970, 750))
        screen.blit(degree_surf, degree_rect)

        velocity_surf = font.render("velocity= "+str(velocity)+"m/s", False, "White", "Black")
        velocity_rect = velocity_surf.get_rect(center=(1230, 750))
        screen.blit(velocity_surf, velocity_rect)

        screen.blit(minusheight_surf,minusheight_rect)
        screen.blit(addheight_surf,addheight_rect)
        screen.blit(minusdistance_surf,minusdistance_rect)
        screen.blit(adddistance_surf,adddistance_rect)
        screen.blit(minusdegree_surf,minusdegree_rect)
        screen.blit(adddegree_surf,adddegree_rect)
        screen.blit(minusvelocity_surf,minusvelocity_rect)
        screen.blit(addvelocity_surf,addvelocity_rect)

        basketball_surf = pygame.image.load("Sprites/basketball.png").convert_alpha()
        basketball_rect = basketball_surf.get_rect(center=(distance, height))
        screen.blit(basketball_surf,basketball_rect)

    if simulation:
        # Time variables for each frame
        heightframe += 1
        distanceframe += 1
        heighttime = heightframe/60
        distancetime = distanceframe/60

        # Calculate the height of ball per frame and the distance of ball per frame
        heightperframe = (((height/100)-(vyarray[len(vyarray)-1]*heighttime))+(((g)*math.pow(heighttime,2))/2))*100
        distanceperframe = ((distance/100) + (vxarray[len(vxarray)-1]*distancetime))*100

        # For display
        vy = (-vyarray[len(vyarray)-1] + g*heighttime)
        vx = vxarray[len(vxarray)-1]

        screen.blit(court_surf, court_rect)
        screen.blit(backboard_surf, backboard_rect)
        screen.blit(rim1_surf, rim1_rect)
        screen.blit(rim2_surf, rim2_rect)

        # If basketball hits the ground
        if heightperframe > (750-ball_radius):
            # Appends the new y axis velocity to be used in the next loop
            vy = (-vyarray[len(vyarray)-1] + g*heighttime)*res
            vyarray.append(vy)
            # Restarts height time frame
            heightframe = 0
            # Sets height
            height = 750-ball_radius

        # If basketball hits the backboard
        if 1495 > distanceperframe > (1495-ball_radius) and 335+backboard_height > heightperframe > 335:
            # Appends the new x axis velocity to be used in the next loop
            vx = -((vxarray[len(vxarray)-1])*backboard_res)
            vxarray.append(vx)
            # Restarts distance time frame
            distanceframe = 0
            # Sets distance
            distance = 1495-ball_radius

            print("Collision backboard")

        # Basketball hitbox surface
        ball_hitbox = pygame.Surface((ball_diameter, ball_diameter), pygame.SRCALPHA)
        pygame.draw.circle(ball_hitbox, [250,250,250], [ball_radius, ball_radius], ball_radius)
        ball_rect = ball_hitbox.get_rect(center=(distanceperframe, heightperframe))
        screen.blit(ball_hitbox, ball_rect)

        score_hitbox = pygame.Surface((ball_diameter, ball_diameter), pygame.SRCALPHA)
        pygame.draw.circle(score_hitbox, [250,250,250], [ball_radius, ball_radius], ball_radius)
        score_rect = score_hitbox.get_rect(center=(1480 - rim_radius, 460))
        screen.blit(score_hitbox, score_rect)

        # Basketball surface
        basketball_surf = pygame.image.load("Sprites/basketball.png").convert_alpha()
        basketball_rect = basketball_surf.get_rect(center=(distanceperframe, heightperframe))
        screen.blit(basketball_surf,basketball_rect)

        # Mask
        mask_rim1 = pygame.mask.from_surface(rim1_surf)
        mask_rim2 = pygame.mask.from_surface(rim2_surf)
        mask_ball = pygame.mask.from_surface(ball_hitbox)
        mask_scorehitbox = pygame.mask.from_surface(score_hitbox)

        # Rim 2 collision
        offset_rim1 = rim1_rect[0] - ball_rect[0], rim1_rect[1] - ball_rect[1]
        # Pass the offset to the `overlap` method. If the masks collide,
        # overlap will return a single point, otherwise `None`
        overlap_rim1 = mask_ball.overlap(mask_rim1, offset_rim1)
        # Rim 2 collision
        offset_rim2 = rim2_rect[0] - ball_rect[0], rim2_rect[1] - ball_rect[1]
        overlap_rim2 = mask_ball.overlap(mask_rim2, offset_rim2)
        # Score hitbox collision
        offset_scorehitbox = score_rect[0] - ball_rect[0], score_rect[1] - ball_rect[1]
        overlap_scorehitbox = mask_ball.overlap(mask_scorehitbox, offset_scorehitbox)

        # If basketball hits rim1
        if overlap_rim1:
            # Calculating the hit angle using pythagorean theorem, returns radians
            a = rim1_rect[1] - heightperframe
            b = rim1_rect[0] - distanceperframe
            c = math.sqrt((math.pow(a,2))+(math.pow(b,2)))
            angle = math.asin(a/c)
            # Appends the new x and y axis velocity to be used in the next loop
            v = (math.sqrt(math.pow(vyarray[len(vyarray)-1]- g*heighttime, 2)+math.pow(vxarray[len(vxarray)-1], 2)))
            vy = (v*math.sin(angle)*rim_res)
            vx = -(v*math.cos(angle)*rim_res)

            vyarray.append(vy)
            vxarray.append(vx)

            print(vxarray[len(vxarray)-1])
            print(vyarray[len(vyarray)-1])

            # Restart time frames
            heightframe = 0
            distanceframe = 0

            # Sets distance and height
            distance = distanceperframe
            height = heightperframe

            print("collision rim1")

        # If basketball hits rim2
        elif overlap_rim2:
            # Calculating the hit angle using pythagorean theorem, returns radians
            a = rim2_rect[1] - heightperframe
            b = rim2_rect[0] - distanceperframe
            c = math.sqrt((math.pow(a,2))+(math.pow(b,2)))
            angle = math.asin(a/c)
            # Appends the new x and y axis velocity to be used in the next loop
            v = (math.sqrt(math.pow(vyarray[len(vyarray)-1]- g*heighttime, 2)+math.pow(vxarray[len(vxarray)-1], 2)))
            vy = (v*math.sin(angle)*rim_res)
            vx = -(v*math.cos(angle)*rim_res)

            vyarray.append(vy)
            vxarray.append(vx)

            print(vxarray[len(vxarray)-1])
            print(vyarray[len(vyarray)-1])

            # Restart time frames
            heightframe = 0
            distanceframe = 0
            
            # Sets distance and height
            distance = distanceperframe
            height = heightperframe

            print("colission rim2")

        # If basketball hitbox collides with score hitbox
        if overlap_scorehitbox:
            scored = True

        scored_surf = font.render("scored= "+str(score), False, "White", "Black")
        scored_rect = scored_surf.get_rect(center=(720, 200))
        screen.blit(scored_surf, scored_rect)

        missed_surf = font.render("missed= "+str(miss), False, "White", "Black")
        missed_rect = missed_surf.get_rect(center=(480, 200))
        screen.blit(missed_surf, missed_rect)

        attempts_surf = font.render("attempts= "+str(attempts), False, "White", "Black")
        attempts_rect = attempts_surf.get_rect(center=(330, 200))
        screen.blit(attempts_surf, attempts_rect)

        yvelocityperframe_surf = font.render("y velocity= "+str('{0:.4g}'.format(-vy))+"m/s", False, "White", "Black")
        yvelocityperframe_rect = yvelocityperframe_surf.get_rect(center=(720, 750))
        screen.blit(yvelocityperframe_surf, yvelocityperframe_rect)

        xvelocityperframe_surf = font.render("x velocity= "+str('{0:.4g}'.format(vx))+"m/s", False, "White", "Black")
        xvelocityperframe_rect = xvelocityperframe_surf.get_rect(center=(480, 750))
        screen.blit(xvelocityperframe_surf, xvelocityperframe_rect)

        if basketball_rect.centery > 750-ball_radius:
            over = True

    pygame.display.update()
    clock.tick(FPS)