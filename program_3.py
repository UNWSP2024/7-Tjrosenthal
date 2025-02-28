# Program #3: US_Population
def main():
    
#Tanner Rosenthal
#2/28/2025
#US Population


data = []
total_population = 0

while True:
    year = input("Enter a year (or 'done' to stop)")
    if year.lower() == "done":
        break

    year = int(year)
    state = input("Enter a state")
    population = int(input("Enter the population"))

    data.append([year, state, population])

year_to_check = int(input("What is the year you want to check?"))

for entry in data:
    if entry[0] == year_to_check:
        total_population += entry[2]

print("The total population in", year_to_check, "is", total_population)
if __name__ == '__main__':
    main()
