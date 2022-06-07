import random

import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

import datapoint as dp

number_of_neighbors = 5
number_of_datapoints = 40

test = dp.Datapoint(random.random()+0.75, random.random() + 0.75, "")
plt.scatter(test.x, test.y, marker='^', c='green')


def generate_data():
    data = []
    for i in range(number_of_datapoints):
        if i % 2 == 0:
            data.append(dp.Datapoint(
                random.random()+0.5, random.random()+0.5, "o"))
        else:
            data.append(dp.Datapoint(
                random.random()+1, random.random()+1, "x"))
    return data


def show_data(data):
    all_data = unify_data(data)
    colors = ['red', 'blue', 'green', 'orange']
    i = 0
    for item in all_data:
        plt.scatter(all_data[item][0], all_data[item]
                    [1], marker=item, c=colors[i])
        i += 1


def unify_data(datalist):
    all_data = {}

    for item in datalist:
        if item.tag in all_data.keys():
            all_data[item.tag][0].append(item.x)
            all_data[item.tag][1].append(item.y)
        else:
            all_data[item.tag] = [[item.x], [item.y]]
    return all_data


def get_abstand(element):
    return test.distance(element.x, element.y)


def find_neighbors(data, test):
    data.sort(key=get_abstand)
    neigh = data[:number_of_neighbors]
    return neigh


def find_type(neighbors):
    tags = {}
    for items in neighbors:
        tags[items.tag] = tags.get(items.tag, 0)+1
    return max(tags, key=tags.get)


def main():
    data = generate_data()
    neigh = find_neighbors(data, test)
    show_data(data + neigh)
    plt.ylim(0, 3)
    plt.xlim(0, 3)
    plt.title(f" Der Testpunkt {test} ist vom Typ {find_type(neigh)}")
    plt.show()


if __name__ == "__main__":
    main()
