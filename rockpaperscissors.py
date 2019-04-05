import random
rpc = ['rock', 'paper' , 'scissors']
outcome  = ['win', 'tie', 'draw']
rpc_user = input("shoot! >")
rpc_comp = random.choice(rpc)
print (rpc_user)
if rpc_comp == 'rock' and rpc_user =='rock':
    print ('tie')
















#     if rpc_user == 'rock':
#         print('draw!')
#     if rpc_user == 'paper':
#         print ('lose')
#     if rpc_user == 'scissors':
#         print ('win')
# if rpc_comp == ('paper'):
#     if rpc_user == 'paper':
#         print ('tie')
#     if rpc_user == 'rock':
#         print ('lose')
#     if rpc_user == 'scissors':
#         print ('win')
# if rpc_comp == ('scissors'):
#     if rpc_user == 'paper':
#         print ('lose')
#     if rpc_user == 'rock':
#         print ('win')
#     if rpc_comp == 'scissors':
#         print ('tie')
#
#
#
# '''
# if in_season == 'rock':
#     if user_food == 'jam':
#         print("Time to make jam!")
#     if user_food == 'toast':
#         print("Can't make avacado toast!")
# else:
#     if user_food == 'jam':
#         print("No berries right now!")
#     if user_food == 'toast':
#         print("Avacado toast, yum! :)")'''
