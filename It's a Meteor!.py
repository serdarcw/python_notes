https://edabit.com/challenge/9YfCbQpRPqRLzPCcg

It's a Meteor!
In a video game, a meteor will fall toward the main character's home planet. Given the meteor's trajectory as a string in the form y = mx + b and the character's position as a tuple of (x, y), return True if the meteor will hit the character and False if it will not.

Examples
will_hit("y = 2x - 5", (0, 0)) ➞ False

will_hit("y = -4x + 6", (1, 2)) ➞ True
Notes
The b value will never be zero or blank.
The m value will always be an integer.
If the m value is 1, the "1" will be shown.
For example, "y = x + 5" will be shown as "y = 1x + 5".
If the m value is -1, the "-1" will be shown.
For example, "y = -x + 2" will be shown as "y = -1x + 2".

equation="y = 4x + 15"
lst=equation.split()
position= (0,15)

if equation[4]=="-" and equation[8]=="+":
   print(position[1] + int(equation[5])*position[0]==int(lst[4]))
elif equation[7]=="-":
   print(position[1]-int(equation[4])*position[0]==-int(lst[4]))
elif equation[7]=="+":
   print(position[1]-int(equation[4])*position[0]==int(lst[4]))
elif equation[4]=="-" and equation[8]=="-":
   print(position[1]+int(equation[5])*position[0]==-int(lst[4]))