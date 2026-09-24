#DICTIONARY AND NESTING.
student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] >= 81 and student_scores[key] <= 90 :
        student_grades[key] = 'Exceeds Expectations'
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = 'Acceptable'
    elif student_scores[key] <= 70 and student_scores[key] >= 0:
        student_grades[key] = 'Fail'
    else:
        print('Invalid input.')

print(student_scores)
print(student_grades)

# NESTING.
travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visitwiths' : 12},
    'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'stuttgart']},
}

#CHALLANGE.
country = input('Enter the name of the country. \n')
visits = int(input('Enter the number of times you\'ve visited this country. \n'))
list_of_cities = input('Enter the names of the cities you visited in that country, separated by commas: ').split(', ')

travel_log = [
    {
        'country': 'france',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'stuttgart']
    },
]

def add_new_country(country_name, times_visited, list_of_cities):
  new_dictionary = {}
  new_dictionary['country'] = country_name
  new_dictionary['visits'] = times_visited
  new_dictionary['cities'] = list_of_cities
  travel_log.append(new_dictionary)

add_new_country(country_name= country , times_visited= visits , list_of_cities= list_of_cities )

print(f'I\'ve been to {travel_log[2]['country']} {travel_log[2]['visits']} times.')
print(f'My favourite city was {travel_log[2]['cities'][0]}.')


#CHALLANGE.
name_of_bider = input('What is your name?: ')
bid_amout = int(input('What is your bid?: $'))

list_of_biders = []

def the_bids(name, amount):
    individual_bid = {}
    individual_bid['name'] = name
    individual_bid['amount'] = int(amount)
    list_of_biders.append(individual_bid)

the_bids(name= name_of_bider , amount= bid_amout )
#print(list_of_biders)

def highest_bider(list_of_biders):
    highest_amount = 0
    for bider in list_of_biders:
        if bider['amount'] > highest_amount:
            highest_amount = bider['amount']
            name = bider['name']
    print(f'The highest bidder is {name} with the amount of: {highest_amount}')

end_bid = False

while end_bid == False:
    condition = input('Is there another bider?')
    if condition == 'yes':
        name_of_bider = input('What is your name?:  ')
        bid_amout = input('What is your bid?: $')
        the_bids(name= name_of_bider , amount= bid_amout )
        #print(list_of_biders)
    elif condition == 'no':
        end_bid = True
        highest_bider(list_of_biders= list_of_biders)
        print('Thankyou!')
    else:
        print('Invalid input!')

        