from prettytable import PrettyTable

table= PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])#methods
table.add_column("Type",["Electric","Water","Fire"])
table.align="l" #tapping table object

print(table)
