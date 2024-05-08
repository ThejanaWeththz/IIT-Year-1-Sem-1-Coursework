# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: ......w2052724.......... 
# Date: ........8/11/2023............

# Referenced the graphics.py module from (https://mcsp.wartburg.edu/zelle/python/)

# importing modules
from graphics import *

# Creating Variables
pas = 0
defer = 0
fail = 0
prog = "y"
out1 = 0
out2 = 0
out3 = 0
out4 = 0
prog_data = []

# Created a function to generate outcome
def outcome(): 
    global out1, out2, out3, out4
    if pas == 120:
        print ("Progress")
        prog_data.append(f"Progress - {pas},{defer},{fail}")
        out1 += 1
    elif pas == 100:
        print ("Progress (module trailer)")
        prog_data.append(f"Progress (module trailer) - {pas},{defer},{fail}")
        out2 += 1
    elif pas >= 20 and fail < 80:
        print ("Do not progress - module retriever")
        prog_data.append(f"Module Retriever - {pas},{defer},{fail}")
        out3 += 1
    elif fail >= 80:
        print ("Exclude")
        prog_data.append(f"Exclude - {pas},{defer},{fail}")
        out4 += 1
    else:
        print ("Do not progress - module retriever")
        prog_data.append(f"Module Retriever - {pas},{defer},{fail}")
        out3 += 1

# Created a function to generate the histogram
def histogram():      
    global out1, out2, out3, out4
    win = GraphWin("Histogram",640,500) # Main window
    win.setBackground(color_rgb(237,242,236))

    title = Text(Point(140,25), "Histogram Results") # Title
    title.setSize(18)
    title.setStyle("bold")
    title.setTextColor(color_rgb(80,80,80))

    # Names for the chart
    names = Text(Point(320,415), " Progress           Trailer           Retriever          Excluded")
    names.setSize(15)
    names.setStyle("bold")
    names.setTextColor(color_rgb(118,134,147))

    # Total of outcomes 
    totOut = Text(Point(140, 470), f"{out1 + out2 + out3 + out4} outcomes in total.")
    totOut.setSize(15)
    totOut.setStyle("bold")
    totOut.setTextColor(color_rgb(118,134,147))

    under_Line = Line(Point(40,400), Point(600,400)) # Created a line for the graph
    under_Line2 = Line(Point(40,401), Point(600,401))
    under_Line.setOutline("black")
    under_Line2.setFill("black")

    rec1 = Rectangle(Point(50,400), Point(170,400 - out1 * 16)) # Rectangle for the first bar
    rec_num1 = Text(Point(110,390 - out1 * 16), out1)
    rec_num1.setStyle("bold")
    rec_num1.setTextColor(color_rgb(118,134,147))
    rec1.setFill(color_rgb(174,248,161))
    
    rec2 = Rectangle(Point(190,400), Point(310,400 - out2 * 16)) # Rectangle for the second bar
    rec_num2 = Text(Point(250,390 - out2 * 16), out2)
    rec_num2.setStyle("bold")
    rec_num2.setTextColor(color_rgb(118,134,147))
    rec2.setFill(color_rgb(160,198,137))
    
    rec3 = Rectangle(Point(330,400), Point(450,400 - out3 * 16))  # Rectangle for the third bar
    rec_num3 = Text(Point(390,390 - out3 * 16), out3)
    rec_num3.setStyle("bold")
    rec_num3.setTextColor(color_rgb(118,134,147))
    rec3.setFill(color_rgb(167,188,119))

    rec4 = Rectangle(Point(470,400), Point(590,400 - out4 * 16))  # Rectangle for the fourth bar
    rec_num4 = Text(Point(530,390 - out4 * 16), out4)
    rec_num4.setStyle("bold")
    rec_num4.setTextColor(color_rgb(118,134,147))
    rec4.setFill(color_rgb(210,182,181))

    # Drawing all in the window
    title.draw(win)
    names.draw(win)
    totOut.draw(win)
    rec_num1.draw(win)
    rec_num2.draw(win)
    rec_num3.draw(win)
    rec_num4.draw(win)
    rec1.draw(win)
    rec2.draw(win)
    rec3.draw(win)
    rec4.draw(win)
    under_Line.draw(win)
    under_Line2.draw(win)

    try:
        win.getMouse()
    except GraphicsError:
        win.close()

# Main while loop for the program to get inputs from the user
while prog == "y":
    try:
        pas = int(input("Please enter your credits at pass: "))
        if pas not in (0,20,40,60,80,100,120):
            print ("Out of Range\n")
            continue
        defer = int(input("Please enter your credits at defer: "))
        if defer not in (0,20,40,60,80,100,120):
            print ("Out of Range\n")
            continue
        fail = int(input("Please enter your credits at fail: "))
        if fail not in (0,20,40,60,80,100,120):
            print ("Out of Range\n")
            continue
    except ValueError:
        print ("Integer Required\n")
        continue
    
    total = pas + defer + fail
    if total != 120:
        print ("Total incorrect\n")
        continue
    
    # Calling outcome function to calculate the outcome
    outcome()

    # Getting input from the user to continue the loop
    prog = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    
# Calling histogram function to display the histogram graphics window
histogram()

# Opening a new text file and writing all the collected data
file = open("prog_data.txt","w")
file.write ("\nPart 3: \n")
print ("\nPart 2: ")
for x in prog_data:
    print (x) # Part 2 for printing the list data
    file.write (x) # Part 3 for writing the list data in a text file
    file.write ("\n")
file.close()
with open("prog_data.txt", "r") as f: # Reading the text file
    print (f.read())
