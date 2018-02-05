# 5-ifs

When we need the computer to make a decision about something, we have to set that choice up in a way that Python can understand. We call this decision an evaluation, and it's more like a comparison.

An if statement looks like this:
```
number = 5
if (number > 4):
    print("The number is greater than 4")
```
In the example above, since the variable "number" has the value 5, the statement "number > 4" evaluates to true. So the code block gets run and the `print()` statement happens. Note that this is a comparison of **integers**.

We can compare strings too:
```
word = "bird"
if (word == "bird"):
    print("Apparently, the bird IS the word")
```
In the second example, we test the variable "word" to see if it matches the string "bird". It does match, so the print() statement gets run. *Note that we use "==" to check if things are the same*.

When we need to specify what the computer should do in both cases of a comparison, we use "else", like this:
```
israining = True
if ( israining ):
    print("Better take your umbrella!")
else:
    print("Enjoy the sun!")
```
In this third example, we have used a new type of variable, a **boolean** called "israining", to hold a true/false value. It can be tested very simply.

Finally, you can specify several possibilities for a comparison with "else if" like this:
```
votes = 65
if (votes > 50):
    print("You have a majority")
elif (votes < 50):
    print("You have a minority")
else:
    print("It's a tie!")
```
*Note, you can have an many additional elif conditionals as you want*

## Your Task:
Use your knowledge of variables, inputs, and ifs to create a 'Rock, Paper, Scissors' game. Plan the steps your program will have to take using comments before you start to code.
