import math


def file_reader(filename: str):
    f_input = open(filename, "r")

    line: list = f_input.readline().strip().split()
    duration: int = int(line[0])
    number_intersections: int = int(line[1])
    intersections: dict = {i: [[], []] for i in range(number_intersections)}
    streets: int = int(line[2])
    cars: int = int(line[3])
    points: int = int(line[4])

    streets_info: dict = {}
    for i in range(streets):
        line: list = f_input.readline().strip().split()
        intersections[int(line[1])][0].append(line[2])
        intersections[int(line[1])][1].append(0)
        streets_info[line[2]] = (int(line[0]), int(line[1]), int(line[3]))

    cars_info: list = []
    for i in range(cars):
        line: list = f_input.readline().strip().split()
        cars_info.append((int(line[0]), line[1:]))

    f_input.close()

    return duration, intersections, streets, cars, points, streets_info, cars_info


def traffic_lights_solver():
    cars_info.sort(key=lambda c: calculate_time(c[1]))

    i: int = 1
    for car in cars_info:
        for street in car[1]:
            street_score: list = []
            position: int = 0
            for j in range(len(intersections[streets_info[street][1]][0])):
                if intersections[streets_info[street][1]][0][j] == street:
                    street_score = intersections[streets_info[street][1]][1]
                    position = j
                    break

            priority: int = street_score[position] + (1/i)
            street_score[position] = priority
        i += 1

    intersections_ordered: dict = dict(sorted(intersections.items(), key=lambda item: -sum(item[1][1])))

    return intersections_ordered


def calculate_time(street_names: list):
    time: int = 0
    for street in street_names:
        time += streets_info[street][2]
    return time


if __name__ == "__main__":
    filename: str = "C:\\Users\\javie\\Desktop\\hashcode_2021\\Competition\\d.txt"

    duration, intersections, streets, cars, points, streets_info, cars_info = file_reader(filename)

    intersections_ordered = traffic_lights_solver()
    # print(intersections_ordered)

    f_output = open("C:\\Users\\javie\\Desktop\\hashcode_2021\\Competition\\submit_d.txt", "w", encoding="UTF-8")

    tiempo_base: int = duration // 2

    f_output.write("{}\n".format(len(intersections_ordered)))
    for (intersection, value) in intersections_ordered.items():
        # print("hola")
        f_output.write("{}\n".format(intersection))
        f_output.write("{}\n".format(len(value[0])))

        for i in range(len(value[0])):
            # print("pepe")
            f_output.write("{} {}\n".format(value[0][i], max(int(math.ceil(value[1][i] * tiempo_base)), 1)))

    f_output.close()
