#Lathika and Calvin
#Oct.15 2020
#Random Quotes Program
#1 Import tkinter and random (modules)
#2 create a function that runs when the button is pressed
#2.1 Store the quotes with number variables because they are easy to read
#2.2 Get a random number from the random module to get what quote will be printed
# Print the quote based on the random number generated using if statements
#3 Define the window and title
#4 Run the main loop

#Step 1. Import the 2 modules that we need to use
import tkinter as tk
import random as rand
#Step 2. Define the code that happens when the button is pressed
def buttonPress():
  #Step 2.1. Have all the quotes in easy to name variables
  one = "'You don't need a license to drive a sandwich.'  - Spongebob"
  two = "'Remember licking doorknobs is illegal on other planets' - Spongebob"
  three = "'The best time to wear a wear a striped sweater...is all the time' - Spongebob"
  four = "'Well first, we have to balance a glassof chocolate milk on our heads, stand on one foot, and sing the Bikini Bottom Anthem'  - Spongebob"
  five = "'Well it's no secret that the best thing about secrets is telling someone else your secret, therby adding another secret to your collection of secrets, secretly'    -Spongebob"
  five = "'I smell the smelly smell of something that smells...smelly'   -Mr.Krabs"
  six = "'This isn't your average everyday darkness.This is...ADVANCED darkness'  - Spongebob"
  seven = "'Look at all the hip, young people eating sal...ads'   -Spongebob"
  eight = "'Oh, I wish I had a nose'   -Patrick"
  nine = "Being grownup is boring. Besides I don't get jazz.' -Patrick"
  ten = "'You know whats funnier than 24? 25'  - Spongebob"
  #Step 2.2. Get a random number for which quote to use
  quoteNum = rand.randint(1,10)
  #Step 2.3. Say the quote based on the random number
  if quoteNum >= 5:
    if quoteNum == 5:
      tk.Label(window, text = five).pack()
    if quoteNum == 6:
      tk.Label(window, text = six).pack()
    if quoteNum == 7:
      tk.Label(window, text = seven).pack()
    if quoteNum == 8:
      tk.Label(window, text = eight).pack()
    if quoteNum == 9:
      tk.Label(window, text = nine).pack()
    if quoteNum == 10:
      tk.Label(window, text = ten).pack()
  elif quoteNum < 5:
    if quoteNum == 4:
      tk.Label(window, text = four).pack()
    if quoteNum == 3:
      tk.Label(window, text = three).pack()
    if quoteNum == 2:
      tk.Label(window, text = two).pack()
    if quoteNum == 1:
      tk.Label(window, text = one).pack()

#Step 3. Define the window and title
window = tk.Tk()
window.title("Random Quotes")
#Step 4. Define the button and how its placed
randomButton = tk.Button(window, text="Press for a random Quote", command = buttonPress)
randomButton.pack()
#Step 5. Run the main loop
window.mainloop()