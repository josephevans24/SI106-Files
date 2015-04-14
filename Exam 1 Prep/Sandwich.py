nested_restaurant_data = {
  "restaurant_name":"Sandwich Shoppe",
  "city":"Lansing",
  "state": "MI",
  "number_of_sandwich_items":50,
  "best_sandwich": "We have a sandwich with peanut-butter, nutella, bananas, wheat-bread, and smoked-salmon as well. It is a delight!",
  "mean_cost_of_meal_in_dollars":12.45
}

# dictionary of ingredient prices

d = {"apples": 1.25, "bananas": 1.25, "nutella": 5.25, "wheat-bread": 3.25, "smoked-salmon": 10.25, 
                     "peanut-butter": 2.25, "lettuce": 0.25, "mustard": 0.25, "mayonnaise": 0.25, "rye-bread": 3.25, 
                     "oranges": 1.25}


# finish this function

def determine_price(sandwich, prices):
    total = 0
    ingridients = sandwich.split(', ')
    for a in prices:
        if a in ingridients:
            total = prices[a] + total
    return total
                         
   
        
    print "return cost"

# what are the inputs to this function?

print determine_price('nutella, rye-bread, lettuce, oranges', d)



def health_prompt(h, mh):
    return '+'*h+'-'*(mh-h)

    



print health_prompt(3, 7)