army = [50]
budget = [50]
loyalty = [50]
tech = [50]
ecology = [50]



def stats_change(army_change, budget_change, loyalty_change, tech_change, ecology_change):
    army.append(army[0] + army_change)
    army.remove(army[0])
    budget.append(budget[0] + budget_change)
    budget.remove(budget[0])
    loyalty.append(loyalty[0] + loyalty_change)
    loyalty.remove(loyalty[0])
    tech.append(tech[0] + tech_change)
    tech.remove(tech[0])
    ecology.append(ecology[0] + ecology_change)
    ecology.remove(ecology[0])


print(army[0], budget[0], loyalty[0], tech[0], ecology[0])

stats_change(-10,-15, -5, 0 , 5)

print(army[0], budget[0], loyalty[0], tech[0], ecology[0])
