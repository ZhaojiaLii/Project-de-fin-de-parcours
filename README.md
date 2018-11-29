# Project-de-fin-de-parcours
Project de fin de parcours:  "From Pseudocode to Code".
This project originates from a research article by Portnoff [1] which showed that the area in the brain that is activated when novice programmers need to understand code is the language area (and not the logic or formal area). Based on this fact, Portnoff claims that the introductory programming course must be taught as a language course, with techniques that were shown to be successful when learning a second language. In particular, two of these techniques are to speak and hear the language as much as possible.

In the context of programming languages, it is difficult to apply these techniques. One can hardly imagine two people chitchatting in Python or Java. This issue comes from the fact that programming languages are not really similar to natural languages (like English) and were mostly created to be written and not spoken.

Pseudocode is a language often used to describe a program or an algorithm. A key characteristic of pseudocode is that it is a language closer to natural languages in comparison with traditional programming languages. This is why pseudocode is regularly presented in introductory programming courses: it removes the complex syntax of a programming language and allows learner to focus on an algorithm that is presented in a “language” they are familiar with.

While pseudocode is not a solution to the problem of “speaking” a new language, it is already a small improvement regarding the readability and understandability of a programming language. This is why, in this project, we want to create a tool that can generate “real” code from pseudocode.

By using this pseudocode to python code translation system, we can easily write the pseudocode in the txt file and get the corresponding python code by launching the translation system.

# The construction of our system
1.Pseudocode_textX.tx which is written in textX grammer, can allow us to rule the system.

2.Pseudocode-Python.py which we used to get the textX model and translate the pseudocode to python code.

3.demo is the file which we write the pseudocodes, which will be translated.

We combine the three files together, and run the python code, we can get the translated pseudocode (python code) in the command line
After we finish the system, we will have a small plateform which allows us to translate the code from pseudocode to python code.

# How to visualize out system
We have two dot files allow us to visualize our system, paste the code of the dot file into: http://www.webgraphviz.com/, and click on generate graph, then we can get the AST(Abstract Syntax Tree) structure of our translation system.




# References:
[1] S. R. Portnoff, “The Introductory Computer Programming Course is First and Foremost a
Language Course,” ACM Inroads, vol. 9, no. 2, pp. 34–52, Apr. 2018.
