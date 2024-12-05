import random
from game_data import data

def display_fields(accounts):
    accounts_name = accounts['name']
    accounts_disc = accounts["description"]
    accounts_count = accounts['country']
    return f"{accounts_name}, a {accounts_disc} from {accounts_count}"

def check_win(u_guess, a, b):
    if a > b:
        return u_guess == "a"
    else:
        return  u_guess == "b"

score = 0
is_game_continue = True
account_b = random.choice(data)

while is_game_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {display_fields(account_a)}")
    print("VS")
    print(f"Against B: {display_fields(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()[0]

    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    is_check = check_win(guess, follower_count_a, follower_count_b)
    print('\n' * 20)
    if is_check:
        score += 1
        print(f"You are right! Current score {score}")
    else:
        print(f"You are wrong. Final score {score}")
        is_game_continue = False






"""import random
from arts import logo_higher_lower_game, logo_higher_lower_vs_game

import os

data = [{
    'name': 'abcd',
    'follower_count': 346,
    'description': 'Social',
    'country': 'United State'
},
{
    'name': 'zack',
    'follower_count': 210,
    'description': 'Social',
    'country': 'United State'
},
{
    'name': 'honda',
    'follower_count': 560,
    'description': 'Social',
    'country': 'United State'
},
{
    'name': 'Suzuki',
    'follower_count': 750,
    'description': 'Social',
    'country': 'United State'
},
]

def choice_play(my_data):
    '''Choice random data from dict'''
    return random.choice(my_data)

#choices = random.choice(data)

def display_data(index, my_display_data):
    ''' Display each dict lists '''
    return f"{my_display_data[index]['name']}, a {my_display_data[index]['description']}, from {my_display_data[index]['country']}"


def clear_console():
    '''Clears the console.'''
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)



my_choices = []
for i in range(0, len(data)):
    my_choices.append(data[i]['name'])



def play():
    is_play = False
    count = 0
    index2 = random.randint(0, len(my_choices) - 1)
    while not is_play:


        index1 = index2
        index2 = random.randint(0, len(my_choices) - 1)



        while index1 == index2:
            index2 = random.randint(0, len(my_choices) - 1)


        #print(my_choices[index1])
        print(logo_higher_lower_game)
        print(display_data(index1, data))

        print(logo_higher_lower_vs_game)

        #print(my_choices[index2])
        print(display_data(index2, data))
        print('\n')

        #clear_console()

        who_ab = input("Who is more follower 'A' or , 'B': ").upper()[0]

        print('\n' * 20)


        if who_ab == 'A':

            if data[index1]['follower_count'] > data[index2]['follower_count'] and who_ab == 'A':
                count += 1
                print('\n')
                print(f"Yes, You ara right, current score {count}")
                #print('\n' * 20)

            else:
                print(f"No Sorry that is wrong, final score {count}")
                is_play = True
        else:
            #print(data[index1]['follower_count'])
            #print(data[index2]['follower_count'])
            if data[index2]['follower_count'] > data[index1]['follower_count']:
                count += 1
                print('\n')
                print(f"Yes, You ara right, current score {count}")


            else:
                print(f"No Sorry that is wrong, final score {count}")
                is_play = True


play()
"""