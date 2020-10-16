#Lathika and Calvin
#Oct.15 2020
#Celestial Weight Program
#1. Import the tkinker Module
#2. Create functions that multiply the correct percent of the Earth weight for each planet
#Step 3. Create the Tkinter Window and title
#Step 4. Create the buttons that allow the user to call the functions.
#Step 5. Create the textbox that allows the user to input their earth weight.
#Step 6. Run the main loop.


#Step 1. Import the module that we need to use
import tkinter as tk

#2. Create functions that multiply the correct percent of the Earth weight for each planet
def moonButtonPress():
  moonWeight = float(textBox.get(1.0, 'end-1c')) *0.17
  tk.Label(window, text = "Your weight on the Moon is " + str(moonWeight) + " lb.").pack()
def marsButtonPress():
  marsWeight = float(textBox.get(1.0, 'end-1c')) *0.38
  tk.Label(window, text = "Your weight on Mars is " + str(marsWeight) + " lb.").pack()
def venusButtonPress():
  venusWeight = float(textBox.get(1.0, 'end-1c')) *0.91
  tk.Label(window, text = "Your weight on Venus is " + str(venusWeight) + " lb.").pack()
def jupiterButtonPress():
  jupiterWeight = float(textBox.get(1.0, 'end-1c')) * 2.54
  tk.Label(window, text = "Your weight on Jupiter is " + str(jupiterWeight) + " lb.").pack()

#Step 3. Create the Tkinter Window and title
window = tk.Tk()
window.title("Celestial Weight Calculator")

#Step 4. Create the buttons that allow the user to call the functions.
moonButton = tk.Button(window, text="Press for your weight on the Moon.", command = moonButtonPress).pack()
marsButton = tk.Button(window, text="Press for your weight on Mars.", command = marsButtonPress).pack()
venusButton = tk.Button(window, text="Press for your weight on Venus.", command = venusButtonPress).pack()
jupiterButton = tk.Button(window, text="Press for your weight on Jupiter.", command = jupiterButtonPress).pack()

#Step 5. Create the textbox that allows the user to input their earth weight.
tk.Label(window, text = "Enter your weight on Earth").pack()
textBox = tk.Text(window, height=1, width=10)
textBox.pack()

#Step 6. Run the main loop.
window.mainloop()