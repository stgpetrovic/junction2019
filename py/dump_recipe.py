import recipe_metadata
from pprint import pprint
import csv

MAX_RECIPE_ID = 10556

def batch(n, l):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def all_recipes():
    m = recipe_metadata.RecipeMetadata()
    infos = []
    for bucket in batch(100, range(1, MAX_RECIPE_ID)):
        ids = [str(id) for id in list(bucket)]
        fetch = m.Infos(ids)
        if not fetch:
            continue
        infos.extend(fetch)
        print("imamo recepata totalno: %s" % len(infos))
    return infos

if __name__ == '__main__':
    recipes = all_recipes()
    with open('recipes.csv', 'w') as f:
        for key in recipes.keys():
            f.write("%s,%s\n"%(key,recipes[key]))
