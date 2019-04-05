#catch_not_cat.py
while True:
    # PASTE CODE HERE
    var1 = input("Please type cat >")
    if var1 == 'cat':
        break

# var2 = 'dog'
var2 = 5
while var2 != 'dog':
    var2 = input("Please type dog >")

running = True
while running == True:
    var3 = input("Please type dolphin >")
    if var3 == 'dolphin':
        running = False
