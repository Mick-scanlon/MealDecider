# csv meal reader
import os
import csv

# Csv format
# recipe name,ingredient,ingredient...,NEWLINE
# recipe name,ingredient,ingredient...,NEWLINE

mealsDict = {} 
here = os.path.dirname(os.path.abspath(__file__))   # find directory
filename = os.path.join(here, 'meals.csv')          # find csv file

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        row = list(filter(None, row))   # removes empty entries
        key = row[0]                    # title of dish is key
        newRow = []
        for string in row[1::]:         # remove whitespace
            string = string.replace(" ","") 
            newRow.append(string)
        mealsDict[key] = newRow         # set dict value to ingredients

# test ingredients
##for key in mealsDict:
#    for ingredient in mealsDict[key]: 
#        print(ingredient)
# Compare likeness of recipes
allCoefficientsDict = {}
allUnrelatedRecipesDict = {}
for recipe in mealsDict:
    relationCoefficientDict = {}    # store each recipes relation
    unrelatedRecipesList = []       # store each unrelated recipe
    matchingIngredients = 0         # temp variable
    for recipe2 in mealsDict:       # takes each ingredient
        for ingredient in mealsDict[recipe]:        # grabs every recipe
            for ingredient2 in mealsDict[recipe2]:  # takes each ingredient from recipe2
                if ingredient == ingredient2:       # compare ingredient to 2
                    matchingIngredients += 1        # add to matched count
                    break
        if matchingIngredients/len(mealsDict[recipe]) == 0.0:
            unrelatedRecipesList.append(recipe2)    # set list value to unrelated recipe title
        elif recipe != recipe2:   # ignore same recipe
            relationCoefficientDict[recipe2] = matchingIngredients/len(mealsDict[recipe])    # set dict value to relation coefficent
        matchingIngredients = 0 # reset count
    allCoefficientsDict[recipe] = dict(reversed(sorted(relationCoefficientDict.items(), key=lambda item:item[1]))) # sorts into most similar first 
    allUnrelatedRecipesDict[recipe] = unrelatedRecipesList  # save unrelated recipes

# test coefficient calculations
print(allCoefficientsDict)
print(allUnrelatedRecipesDict)
# find most related 
