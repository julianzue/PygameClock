import pygame
import time

import set_reminder

pygame.init()


screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

font = pygame.font.SysFont("Monospace", 150)
font_todo = pygame.font.SysFont("Monospace", 50)

black = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

    screen.fill((10,10,10))

    todotext = set_reminder.current_task()

    if todotext == "":
        if int(time.strftime("%H")) < 12:
            todotext = "Good Morning"

        elif int(time.strftime("%H")) >= 18:
            todotext = "Good Evening"

        elif int(time.strftime("%H")) >= 20:
            todotext = "Good Night"

        else:
            todotext = "Hello"

    sp = todotext.split(" | ")

    if sp[0] == time.strftime("%H:%M"):

        if black:
            color = (50,0,0)
            black = False
        else:
            color = (10,10,10)
            black = True

        screen.fill(color)

        time.sleep(1)

        render_todo_text = font_todo.render(todotext, True, (0,255,0))
    else:
        render_todo_text = font_todo.render(todotext, True, (255,255,0))

    screen.blit(render_todo_text, (50,350))

    render_time = font.render(time.strftime("%H:%M:%S"), True, (255,255,255))
    screen.blit(render_time, (50,50))

    render_date = font_todo.render(time.strftime("%A %d.%m.%Y"), True, (255,255,255))
    screen.blit(render_date, (50, 200))

    #render_todo = font_todo.render("To-Do:", True, (255,255,0))
    #screen.blit(render_todo, (50,300))

    '''"'''

    nexttodotext = set_reminder.next_task()
    render_next_todo_text = font_todo.render(nexttodotext, True, (255,255,0))

    screen.blit(render_next_todo_text, (50, 425))

    

    pygame.display.update()
