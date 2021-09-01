import pygame


def make_initial_generation(Screen_Size, Actives):
    generation = []

    for cell in range(0, int(Screen_Size/4), 1):
        if Actives.count(cell) == 1:
            generation.append(1)
        else:
            generation.append(0)

    return generation


def apply_rules(actives, Screen_Size, rule_set):
    full_generation = make_initial_generation(Screen_Size, actives)
    new_actives =[]

    for cell in range(1, len(full_generation)-1, 1):
        first_neighbor = full_generation[cell-1]
        second_neighbor = full_generation[cell]
        third_neighbor = full_generation[cell+1]

        neighborhood = str(first_neighbor) + str(second_neighbor) + str(third_neighbor)

        if rule_set[neighborhood] == 1:
            new_actives.append(cell)
        else:
            pass

    return new_actives
