print  ('welcome to the magic 8 ball')
import random
opinion_list = ['yes', 'no', 'uncertain', 'very certain']
user_question  = input("user ask your question? >")
print(f"your answer is  {user_question} was {random.choice(opinion_list)}")
