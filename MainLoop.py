import pygame
import OneD_Automata
import Cases

Screen_Size = 512
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((Screen_Size, Screen_Size))
pygame.display.set_caption("Cellular Automata")

clock = pygame.time.Clock()

pygame.init()

running = True

'''
actives are the index of the squares that have the value of 1
'''

actives = [20, 60, 90, 120]

rule_set = Cases.rule(89)

'''
rules have to be 0 to 255 otherwise it wont work

look at the binary values in Cases.py and you will understand this range
'''

generation = OneD_Automata.make_initial_generation(Screen_Size, actives)

NumOfgenerations = 1
listOfGenerations = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # remove if statement, if you want it to keep going (its not optimised and the list of gens keeps getting bigger!)

    if NumOfgenerations <= 128:
        screen.fill((0, 0, 0))

        currentGen = []
        for active in actives:
            currentGen.append(active)
        listOfGenerations[NumOfgenerations] = currentGen

        Iterator = NumOfgenerations

        for key in listOfGenerations:
            for cell in listOfGenerations[key]:
                pygame.draw.rect(screen, WHITE, (cell*4, Screen_Size - 4*Iterator, 4, 4))
            Iterator -= 1

        actives = OneD_Automata.apply_rules(actives, Screen_Size, rule_set)

        # pygame.draw.rect(screen, WHITE, (Screen_Size/2, Screen_Size-4, 4, 4))

        pygame.display.update()

        NumOfgenerations += 1

    clock.tick(30)