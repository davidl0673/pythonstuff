import random
opinion_list = ['very good', 'okay', 'pretty good', 'very bad']
user_movie = input("what movie do you like?>")
print(f"I thought that {user_movie}was{random.choice(opinion_list)}")
