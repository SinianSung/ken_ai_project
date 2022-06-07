import random as rd

import matplotlib.pyplot as plt

import datapoint as dp

test = dp.Datapoint(1, 2, 3, "+")


def generate_data(anzahl):
    data = []
    for i in range(anzahl):
        if i % 3 == 0:
            data.append(dp.Datapoint(
                rd.random(), rd.random(), rd.random(), "o"))
        elif i % 3 == 1:
            data.append(dp.Datapoint(rd.random()+0.5,
                        rd.random()+0.5, rd.random()+0.5, "x"))
        else:
            data.append(dp.Datapoint(rd.random()-0.5,
                        rd.random()+0.5, rd.random()*2+1, "^"))
    return data


def unify_data(datalist):
    all_data = {}

    for item in datalist:
        if item.tag in all_data.keys():
            all_data[item.tag][0].append(item.x)
            all_data[item.tag][1].append(item.y)
            all_data[item.tag][2].append(item.z)
        else:
            all_data[item.tag] = [[item.x], [item.y], [item.z]]
    return all_data


def show_data(data):
    all_data = unify_data(data)
    colors = ['red', 'blue', 'green', 'orange']
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(test.x, test.y, test.z, marker=test.tag, c=colors[0])
    i = 1
    for item in all_data:
        ax.scatter(all_data[item][0], all_data[item]
                   [1], all_data[item][2], marker=item, c=colors[i])
        i += 1
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


def get_abstand(element):
    return test.distance(element)


def find_neighbours(data):
    data.sort(key=get_abstand)
    neigh = data[:5]
    return neigh


def find_type(neighbours):
    tags = {}
    for items in neighbours:
        tags[items.tag] = tags.get(items.tag, 0) + 1
    print(tags)
    return max(tags, key=tags.get)


def main():
    """ Sortieren einer Liste nach dem Ergebnis einer Funktion"""
    data = generate_data(100)
    test.x = rd.random()+0.5
    test.y = rd.random()
    test.z = rd.random()+0.5
    n = find_neighbours(data)
    print(n)
    t = find_type(n)
    print(t)
    test.tag = t
    show_data(data)


if __name__ == "__main__":
    main()
