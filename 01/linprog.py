from pulp import LpMaximize, LpProblem, LpVariable

# Define the model
model = LpProblem(name="Production_Optimization", sense=LpMaximize)

# Define the decision variables
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Define the constraints
water_constraint = 2 * lemonade + fruit_juice <= 100
sugar_constraint = lemonade <= 50
lemon_juice_constraint = lemonade <= 30
fruit_puree_constraint = 2 * fruit_juice <= 40


# Add the constraints to the model
model += water_constraint, "Water_constraint"
model += sugar_constraint, "Sugar_constraint"
model += lemon_juice_constraint, "Lemon_juice_constraint"
model += fruit_puree_constraint, "Fruit_puree_constraint"

# Define the objective function
model += lemonade + fruit_juice, "Total_production"

# Solve the model
model.solve()

# Print results
print("Status:", model.status)
print("Maximum Total Production (Lemonade + Fruit Juice):", model.objective.value())
print("Lemonade:", lemonade.value())
print("Fruit Juice:", fruit_juice.value())
