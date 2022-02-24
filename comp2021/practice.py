from typing import *


def file_reader(filename: str):
    def add_pizza(pizza: int, ingredients: set):
        # Best combinations for two_teams
        best_combinations_two, size_combinations_two, pizzas_combinations_two = best_pizzas_combinations[2]
        # i: int = 0
        for option in best_combinations_two:
            # option is a list which contains two tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                new_combination: set = {option[0][0], pizza}
                if new_combination not in pizzas_combinations_two:
                    pizzas_combinations_two.append(new_combination)
                    option[1] = (pizza, ingredients)
                    option[-1] = len(ingredients.union(option[0][1]))
            else:
                # If we have two pizzas in the option

                # Score between the first pizza and the current pizza
                score1 = len(ingredients.union(option[0][1]))
                new_combination1: set = {pizza, option[0][0]}

                # Score between the second pizza and the current pizza
                score2 = len(ingredients.union(option[1][1]))
                new_combination2: set = {pizza, option[1][0]}

                # Update the option if we have a better score
                if score1 > score2 and score1 > option[-1] and new_combination1 not in pizzas_combinations_two:
                    pizzas_combinations_two.append(new_combination1)
                    option[-1] = score1
                    option[1] = (pizza, ingredients)
                elif score2 > option[-1] and new_combination2 not in pizzas_combinations_two:
                    pizzas_combinations_two.append(new_combination2)
                    option[-1] = score2
                    option[0] = (pizza, ingredients)

        if size_combinations_two < two_teams:
            best_combinations_two.append([(pizza, ingredients), (), -1])
            best_pizzas_combinations[2] = (best_combinations_two, size_combinations_two + 1, pizzas_combinations_two)

        # Best combinations for three_teams
        best_combinations_three, size_combinations_three, pizzas_combinations_three = best_pizzas_combinations[3]
        # i: int = 0
        for option in best_combinations_three:
            # option is a list which contains three tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), (p3, ing3), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                if len(option[1]) == 0:
                    option[1] = (pizza, ingredients)
                else:
                    new_combination: set = {pizza, option[0][0], option[1][0]}
                    if new_combination not in pizzas_combinations_three:
                        pizzas_combinations_three.append(new_combination)
                        option[2] = (pizza, ingredients)
                        option[-1] = len(ingredients.union(option[0][1], option[1][1]))
            else:
                # If we have three pizzas in the option

                # Score between the first, second and the current pizza
                score1 = len(ingredients.union(option[0][1], option[1][1]))
                new_combination1: set = {pizza, option[0][0], option[1][0]}

                # Score between the first, third and the current pizza
                score2 = len(ingredients.union(option[0][1], option[2][1]))
                new_combination2: set = {pizza, option[0][0], option[2][0]}

                # Score between the second, third and the current pizza
                score3 = len(ingredients.union(option[1][1], option[2][1]))
                new_combination3: set = {pizza, option[1][0], option[2][0]}

                scores = [score1, score2, score3]

                # Update the option if we have a better score
                if all([score1 >= i for i in scores]) and score1 > option[-1] \
                        and new_combination1 not in pizzas_combinations_three:
                    pizzas_combinations_three.append(new_combination1)
                    option[-1] = score1
                    option[2] = (pizza, ingredients)
                elif all([score2 >= i for i in scores]) and score2 > option[-1] \
                        and new_combination2 not in pizzas_combinations_three:
                    pizzas_combinations_three.append(new_combination2)
                    option[-1] = score2
                    option[1] = (pizza, ingredients)
                elif all([score3 >= i for i in scores]) and score3 > option[-1] \
                        and new_combination3 not in pizzas_combinations_three:
                    pizzas_combinations_three.append(new_combination3)
                    option[-1] = score3
                    option[0] = (pizza, ingredients)

        if size_combinations_three < three_teams:
            best_combinations_three.append([(pizza, ingredients), (), (), -1])
            best_pizzas_combinations[3] = (best_combinations_three, size_combinations_three + 1,
                                           pizzas_combinations_three)

        # Best combinations for four_teams
        best_combinations_four, size_combinations_four, pizzas_combinations_four = best_pizzas_combinations[4]
        # i: int = 0
        for option in best_combinations_four:
            # option is a list which contains two tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), (p3, ing3), (p4, ing4), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                if len(option[1]) == 0:
                    option[1] = (pizza, ingredients)
                elif len(option[2]) == 0:
                    option[2] = (pizza, ingredients)
                else:
                    new_combination: set = {pizza, option[0][0], option[1][0], option[2][0]}
                    if new_combination not in pizzas_combinations_four:
                        pizzas_combinations_four.append(new_combination)
                        option[3] = (pizza, ingredients)
                        option[-1] = len(ingredients.union(option[0][1], option[1][1], option[2][1]))
            else:
                # If we have four pizzas in the option

                # Score between the first, second, third and the current pizza
                score1 = len(ingredients.union(option[0][1], option[1][1], option[2][1]))
                new_combination1: set = {pizza, option[0][0], option[1][0], option[2][0]}

                # Score between the first, second, fourth and the current pizza
                score2 = len(ingredients.union(option[0][1], option[1][1], option[3][1]))
                new_combination2: set = {pizza, option[0][0], option[1][0], option[3][0]}

                # Score between the first, third, fourth and the current pizza
                score3 = len(ingredients.union(option[0][1], option[2][1], option[3][1]))
                new_combination3: set = {pizza, option[0][0], option[2][0], option[3][0]}

                # Score between the second, third, fourth and the current pizza
                score4 = len(ingredients.union(option[1][1], option[2][1], option[3][1]))
                new_combination4: set = {pizza, option[1][0], option[2][0], option[3][0]}

                scores = [score1, score2, score3, score4]

                # Update the option if we have a better score
                if all([score1 >= i for i in scores]) and score1 > option[-1] \
                        and new_combination1 not in pizzas_combinations_four:
                    pizzas_combinations_four.append(new_combination1)
                    option[-1] = score1
                    option[3] = (pizza, ingredients)
                elif all([score2 >= i for i in scores]) and score2 > option[-1] \
                        and new_combination2 not in pizzas_combinations_four:
                    pizzas_combinations_four.append(new_combination2)
                    option[-1] = score2
                    option[2] = (pizza, ingredients)
                elif all([score3 >= i for i in scores]) and score3 > option[-1] \
                        and new_combination3 not in pizzas_combinations_four:
                    pizzas_combinations_four.append(new_combination3)
                    option[-1] = score3
                    option[1] = (pizza, ingredients)
                elif all([score4 >= i for i in scores]) and score4 > option[-1]\
                        and new_combination4 not in pizzas_combinations_four:
                    pizzas_combinations_four.append(new_combination4)
                    option[-1] = score4
                    option[0] = (pizza, ingredients)

        if size_combinations_four < four_teams:
            best_combinations_four.append([(pizza, ingredients), (), (), (), -1])
            best_pizzas_combinations[4] = (best_combinations_four, size_combinations_four + 1, pizzas_combinations_four)

        # Re-ordering the lists of options
        for (combinations, _, _) in best_pizzas_combinations.values():
            combinations.sort(key=lambda o: -o[-1])

    f_input = open(filename, "r")

    aux_line = f_input.readline().strip().split()
    pizzas: int = int(aux_line[0])
    two_teams: int = int(aux_line[1])
    three_teams: int = int(aux_line[2])
    four_teams: int = int(aux_line[3])
    best_pizzas_combinations: dict = {i: ([], 0, []) for i in range(2, 5)}

    # pizzas_ingredients: dict = {}
    # ingredients: set = set()
    i: int = 0
    for line in f_input:
        pizza_ing = set(line.strip().split()[1:])
        # pizzas_ingredients[i] = pizza_ing
        # ingredients.update(pizza_ing)
        add_pizza(i, pizza_ing)
        i += 1

    f_input.close()

    # different_ingredients: dict = {}
    # for pizza, ingredients_pizza in pizzas_ingredients.items():
    #     ingredients_not_in_pizza: set = ingredients.difference(ingredients_pizza)
    #     if ingredients_not_in_pizza in different_ingredients:
    #         different_ingredients[ingredients_not_in_pizza].add(pizza)
    #     else:
    #         different_ingredients[ingredients_not_in_pizza] = set(pizza)

    # indexes_pizzas = sorted(range(pizzas), key= lambda i: len(different_ingredients[ingredients.difference(pizzas_ingredients[i])]))

    return pizzas, two_teams, three_teams, four_teams, best_pizzas_combinations


if __name__ == "__main__":
    # pizzas --> number of pizzas that has the pizzeria
    # two_teams --> number of two-people teams
    # three_teams --> number of three-people teams
    # four_teams --> number of three-people teams
    # pizza_ingredients --> dictionary with the ingredients for each pizza

    filename: str = "C:\\Users\\javie\\Desktop\\hashcode_2021\\c_many_ingredients.in"

    pizzas, two_teams, three_teams, four_teams, best_pizzas_combinations = file_reader(filename)
    # deliveries = delivery_solver(pizzas, two_teams, three_teams, four_teams, pizzas_ingredients, different_ingredients)

    f_output = open("C:\\Users\\javie\\Desktop\\hashcode_2021\\submit_c.out", "w", encoding="UTF-8")
    # Falta por añadir la primera linea que indique a cuantos equipos se le envian pizzas
    i: int = 0  # Index for two_teams' pizzas
    j: int = 0  # Index for three_teams' pizzas
    k: int = 0  # Index for four_teams' pizzas

    options_two: list = best_pizzas_combinations[2][0]
    len_options_two: int = best_pizzas_combinations[2][1]
    # print(options_two)
    # print(len_options_two)

    options_three: list = best_pizzas_combinations[3][0]
    len_options_three: int = best_pizzas_combinations[3][1]
    # print(options_three)
    # print(len_options_three)

    options_four: list = best_pizzas_combinations[4][0]
    len_options_four: int = best_pizzas_combinations[4][1]
    # print(options_four)
    # print(len_options_four)

    pizzas_delivered: set = set()
    count_pizzas_delivered: int = 0
    total_score: int = 0
    while count_pizzas_delivered < pizzas and \
            not(i >= len_options_two and j >= len_options_three and k >= len_options_four):
        opt_two: list = []
        score_two: int = -1
        opt_three: list = []
        score_three: int = -1
        opt_four: list = []
        score_four: int = -1
        if i < len_options_two:
            opt_two = options_two[i]
            score_two = opt_two[-1]
            if score_two == -1:
                i += 1
        if j < len_options_three:
            opt_three = options_three[j]
            score_three = opt_three[-1]
            if score_three == -1:
                j += 1
        if k < len_options_four:
            opt_four = options_four[k]
            score_four = opt_four[-1]
            if score_four == -1:
                k += 1

        score: int = -1
        team: int = -1
        pizzas_to_team: list = []
        if score_two != -1 and score_two >= score_three and score_two >= score_four:
            score = opt_two[-1]
            team = 2
            pizzas_to_team = [opt_two[0][0], opt_two[1][0]]
            i += 1
        elif score_three != -1 and score_three >= score_two and score_three >= score_four:
            score = opt_three[-1]
            team = 3
            pizzas_to_team = [opt_three[0][0], opt_three[1][0], opt_three[2][0]]
            j += 1
        elif score_four != -1 and score_four >= score_three and score_four >= score_two:
            score = opt_four[-1]
            team = 4
            pizzas_to_team = [opt_four[0][0], opt_four[1][0], opt_four[2][0], opt_four[3][0]]
            k += 1

        not_has_any_pizza: bool = True
        for pizza in pizzas_to_team:
            if pizza in pizzas_delivered:
                # print("hora")
                not_has_any_pizza = False

        if not_has_any_pizza and len(pizzas_to_team) > 0:
            # print("alex puto")
            count_pizzas_delivered += len(pizzas_to_team)
            total_score += score ** 2
            pizzas_delivered.update(pizzas_to_team)
            # print(pizzas_delivered)
            f_output.write("{}".format(team))
            for index_pizza in pizzas_to_team:
                f_output.write(" {}".format(index_pizza))
            f_output.write("\n")
            # f_output.flush()

    f_output.close()

    print(total_score)
