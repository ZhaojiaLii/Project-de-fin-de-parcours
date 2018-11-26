#!/usr/bin/python
# -*- coding: UTF-8 -*-

# prepare for the parsing
from textx.metamodel import metamodel_from_file
python_meta = metamodel_from_file('Pseudocode_textX.tx')
example_python_model = python_meta.model_from_file('demo')

# the class for parse all our pseudocode to python code
class Python(object):

    # for testing the output of our model
    def _test_(self, model):
        for c in model.instruction:
            print (c)

    # we parse our code in this function
    def Instructions(self, model):

        show_declare = '\n'+'//you have not give values to these variables: '
        show_input = '\n'+'//you need to type in variable: '
        declare_list = []
        input_list = []
        need_value_list = []
        have_value_list = []
        if_num_1 = 0    # let us know the number of the if instruction
        indentation = "    "    # control the indentation of python code

        
        # where we get the instructions from the model and process them
        for c in model.instruction:   
            #print (c)
                
            # Basic instructions as below:
            # we have declare_variables, input_variables and print

            # for process the indentations
            if if_num_1 == 0:
                indentation = ''
            elif if_num_1 == 1:
                indentation = "    "
            elif if_num_1 == 2:
                indentation = "        "
            elif if_num_1 > 2:
                for i in range(if_num_1-2):
                    indentation = indentation + "    "

            # we start to process the pseudocode from here:
            if c.__class__.__name__ == 'Declare_variable':                
                var_declare = '{}'.format(c.variable.var)
                declare_list.append(var_declare)
                need_value_list.append(var_declare)
                print ("//you have declared variable " + var_declare)
                
            elif c.__class__.__name__ == 'Input_variable':
                var_input = '{}'.format(c.variable.var)
                if var_input not in declare_list:
                    print ('\n'+"//please declare the variable '"+var_input+"' first")
                else:
                    show_input = show_input + var_input
                    input_list.append(var_input)
                    if if_num_1 != 0:
                        print (indentation + var_input + " = raw_input('input:"+var_input+"')" )
                    else:
                        print (var_input + " = raw_input('input:"+var_input+"')" )  

            elif c.__class__.__name__ == 'Declare_value':
                var_value = '{}'.format(c.variable.var)
                if isinstance(c.value.val,int):
                    value = str(c.value.val)
                    if if_num_1 != 0:
                        print (indentation + var_value+' = '+value)
                    else:
                        print (var_value+' = '+value)
                    need_value_list.remove(var_value)
                    have_value_list.append(var_value)
                elif isinstance('{}'.format(c.value.val),str):
                    value = c.value.val
                    if if_num_1 != 0:
                        print (indentation + var_value + " = '"+value+"'")
                    else:
                        print (var_value+" = '"+value+"'")
                    need_value_list.remove(var_value)   
                    have_value_list.append(var_value)
                else:
                    return

            elif c.__class__.__name__ == 'Print_words':
                content = '{}'.format(c.content.con)
                if content in declare_list and input_list:
                    if if_num_1 != 0:
                        print (indentation + 'print '+ content)
                    else:
                        print ('print '+ content)
                elif content in declare_list not in input_list:
                    print ('\n'+'//'+content+' is a variable, please give a value before print.')
                else:
                    if if_num_1 != 0:
                        print (indentation + 'print "'+ content +'"')
                    else:
                        print ('print "'+ content +'"')

            elif c.__class__.__name__ == 'Print_string':
                content = '{}'.format(c.content_string.con)
                if if_num_1 != 0:
                    print (indentation + 'print '+'"'+content+'"')
                else:
                    print ('print '+'"'+content+'"')
            
            elif c.__class__.__name__ == 'Calculation_simple':

                variable_af = '{}'.format(c.variable_af.var_af)
                if c.calculation_operator == 'plus':
                    print (variable_be + '+' + variable_af)
                elif c.calculation_operator == 'minus':
                    print (variable_be + '-' + variable_af)
                elif c.calculation_operator == 'multiply':
                    print (variable_be + '*' + variable_af)
                elif c.calculation_operator == 'divide':
                    print (variable_be + '/' + variable_af)
                elif c.calculation_operator == 'power':
                    print (variable_be + '**' + variable_af)

            
            # If instruction is as below:
            
            elif c.__class__.__name__ == 'If_instruction_startline':
                indentation = "    "

                if if_num_1 == 0:
                    print ('\n' + "//If instruction as below:") 
                else:
                    if_num_1 = if_num_1

                a = 0   # use a variable to know the two variables in IF are all declared
                if_num_1 = if_num_1 + 1  # let us know this is which if instruction
                variable_be = '{}'.format(c.variable_be.var_be)
                variable_af = '{}'.format(c.variable_af.var_af)
                comparasion_symbol = '{}'.format(c.comparasion)
                logic_operator = '{}'.format(c.logic_operator)

                if if_num_1 > 1:
                    if if_num_1 == 2:
                        indentation = indentation
                    elif if_num_1 > 2:
                        for i in range(if_num_1-2):
                            indentation = indentation + "    "
                else:
                    if_num_1 = if_num_1
                    indentation = ''
                        

                if variable_be in have_value_list:
                    a = a + 1                
                elif variable_be in declare_list:
                    print ("//" + variable_be + " is not a valued variable, please give a value first.")  
                else:
                    print ("//" + variable_be + " is not a declared variable, please declare first.")
                
                if variable_af in have_value_list:
                    a = a + 1
                elif variable_af in declare_list:
                    print ("//" + variable_af + " is not a valued variable, please give a value first.")  
                else:
                    print ("//" + variable_af + " is not a declared variable, please declare first.")
                
                if a == 2:

                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "if " + variable_be + " > " + variable_af + ":")                 
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "if " + variable_be + " < " + variable_af + ":")                      
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "if " + variable_be + " >= " + variable_af + ":")                     
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "if " + variable_be + " == " + variable_af + ":")                
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "if " + variable_be + " != " + variable_af + ":")

                    # logic operator in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "if " + variable_be + " and " + variable_af + ":")
                    elif logic_operator == 'or':
                        print (indentation + "if " + variable_be + " or " + variable_af + ":")
                    elif logic_operator == 'not':
                        print (indentation + "if " + variable_be + " not " + variable_af + ":")
            
            elif c.__class__.__name__ == 'If_instruction_elifline':

                a = 0   # use a variable to know the two variables in IF are all declared
                variable_be = '{}'.format(c.variable_be.var_be)
                variable_af = '{}'.format(c.variable_af.var_af)
                comparasion_symbol = '{}'.format(c.comparasion)
                logic_operator = '{}'.format(c.logic_operator)

                indentation = "    "
                if if_num_1 > 1:
                    if if_num_1 == 2:
                        indentation = indentation
                    elif if_num_1 > 2:
                        for i in range(if_num_1-2):
                            indentation = indentation + "    "
                else:
                    if_num_1 = if_num_1
                    indentation = ''

                if variable_be in have_value_list:
                    a = a + 1                
                elif variable_be in declare_list:
                    print ("//" + variable_be + " is not a valued variable, please give a value first.")  
                else:
                    print ("//" + variable_be + " is not a declared variable, please declare first.")
                
                if variable_af in have_value_list:
                    a = a + 1
                elif variable_af in declare_list:
                    print ("//" + variable_af + " is not a valued variable, please give a value first.")  
                else:
                    print ("//" + variable_af + " is not a declared variable, please declare first.")
                
                if a == 2:

                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "elif " + variable_be + " > " + variable_af + ":")                      
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "elif " + variable_be + " < " + variable_af + ":")                    
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "elif " + variable_be + " >= " + variable_af + ":")                      
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "elif " + variable_be + " == " + variable_af + ":")                       
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "elif " + variable_be + " != " + variable_af + ":")
                    
                    # logic operators in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "if " + variable_be + " and " + variable_af + ":")
                    elif logic_operator == 'or':
                        print (indentation + "if " + variable_be + " or " + variable_af + ":")
                    elif logic_operator == 'not':
                        print (indentation + "if " + variable_be + " not " + variable_af + ":")

            elif c == 'else':
                indentation = "    "
                if if_num_1 > 1:
                    if if_num_1 == 2:
                        indentation = indentation
                    elif if_num_1 > 2:
                        for i in range(if_num_1-2):
                            indentation = indentation + indentation
                else:
                    if_num_1 = if_num_1
                    indentation = ''
                print (indentation + "else:")
            elif c == 'end if':
                print ("//number " + str(if_num_1) + " if instruction finished")
                if_num_1 = if_num_1 - 1
                


                
        # show the values we have not given values

        if len(need_value_list)>0:
            for vals in need_value_list[:-1]:
                show_declare = show_declare + vals + ','
            show_declare = show_declare + need_value_list[-1]
            print (show_declare)
        else:
            return

pyth = Python()
pyth.Instructions(example_python_model)
#pyth._test_(example_python_model)