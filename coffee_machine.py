class CoffeeMachine:
    resourse = [400, 540, 120, 9, 550]
    ingrdnts = ["water", "milk", "beans", "cups", "money"]
    on = True

    def __init__(self):
        self.espr = [250, 0, 16, 1, -4]
        self.latte = [350, 75, 20, 1, -7]
        self.capp = [200, 100, 12 , 1, -6]
        self.start = True
    def communicate(self, string):
        self.task = string
        if self.start == True:
            print("Write action (buy, fill, take, remaining, exit):")
            self.start = False


def print_status():
    print("\nThe coffee machine has:\n",
    get_coffee.resourse[0], "of water\n",
    get_coffee.resourse[1], "of milk\n",
    get_coffee.resourse[2], "of coffee beans\n",
    get_coffee.resourse[3], "of disposable cups\n",
    f"${get_coffee.resourse[4]} of money\n")

def check_rest(coffee):
    i = 0
    while i < 5:
        if coffee[i] > get_coffee.resourse[i]:
            return i
        i += 1
    return i

def purchase(choice):
    if choice == 1:
        coffee = get_coffee.espr
    elif choice == 2:
        coffee = get_coffee.latte
    else:
        coffee = get_coffee.capp
    check = check_rest(coffee)
    counter = 0
    if check == 5:
        print("I have enough resources, making you a coffee!\n")
        while counter < 5:
            get_coffee.resourse[counter] -= coffee[counter]
            counter += 1
    else:
        print("Sorry, not enough {}!\n".format(get_coffee.ingrdnts[check]))

get_coffee = CoffeeMachine()

while get_coffee.on:
    get_coffee.start = True
    get_coffee.communicate(None)
    get_coffee.communicate(input())
    if get_coffee.task == "remaining":
        print_status()
    if get_coffee.task == "buy":
        get_coffee.communicate(input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
        if get_coffee.task == "back":
            print('')
            continue
        purchase(int(get_coffee.task))
    if get_coffee.task == "fill":
        get_coffee.resourse[0] += int(input("Write how many ml of water do you want to add:\n"))
        get_coffee.resourse[1] += int(input("Write how many ml of milk do you want to add:\n"))
        get_coffee.resourse[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        get_coffee.resourse[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print('')
    if get_coffee.task == "take":
        print("\nI gave you ${}\n".format(get_coffee.resourse[4]))
        get_coffee.resourse[4] = 0
    if get_coffee.task == "exit":
        get_coffee.on = False
