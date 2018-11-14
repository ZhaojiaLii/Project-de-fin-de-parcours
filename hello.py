#!/usr/bin/python
# -*- coding: UTF-8 -*-

from textx.metamodel import metamodel_from_file
python_meta = metamodel_from_file('declare.tx')
example_python_model = python_meta.model_from_file('demo')

class Python(object):


    def if_function(self, model):
        for c in model.rule:
            if c.__class__.__name__ == 'If':
                com = '{}'.format(c.comparision)
                if com.index('is greater than'):
                    print(com)
                else:
                    print('shibaile!')

    def declare_and_print(self, model):

        show_declare = '//you have not give values to these variables: '
        show_input = '//you need to type in variable: '
        declare_list = []
        input_list = []
        need_value_list = []

        for c in model.rule:       
            if c.__class__.__name__ == 'Declare_variable':                
                var_declare = '{}'.format(c.variable.var)
                declare_list.append(var_declare)
                need_value_list.append(var_declare)
            elif c.__class__.__name__ == 'Input_variable':
                var_input = '{}'.format(c.variable.var)
                if var_input not in declare_list:
                    print ("//please declare the variable '"+var_input+"' first")
                else:
                    show_input = show_input + var_input
                    input_list.append(var_input)
                    print (var_input + " = raw_input('input:"+var_input+"')" )     
            elif c.__class__.__name__ == 'Declare_value':
                var_value = '{}'.format(c.variable.var)
                if isinstance(c.value.val,int):
                    value = str(c.value.val)
                    print (var_value+' = '+value)
                    need_value_list.remove(var_value)
                elif isinstance('{}'.format(c.value.val),str):
                    value = c.value.val
                    print (var_value+" = '"+value+"'")
                    need_value_list.remove(var_value)   
                else:
                    return
            elif c.__class__.__name__ == 'Print_words':
                content = '{}'.format(c.content.con)
                if content in declare_list and input_list:
                    print ('print '+ content)
                elif content in declare_list not in input_list:
                    print ('//'+content+' is a variable, please give a value before print.')
                else:
                    print ('print "'+ content +'"')
            elif c.__class__.__name__ == 'Print_string':
                content = '{}'.format(c.content_string.con)
                print ('print '+'"'+content+'"')

        if len(need_value_list)>0:
            for vals in need_value_list[:-1]:
                show_declare = show_declare + vals + ','
            show_declare = show_declare + need_value_list[-1]
            print (show_declare)
        else:
            return

        #print (show_input)
        #print 'input list:',input_list
        #print 'declare list:',declare_list
        #return declare_list

pyth = Python()
pyth.declare_and_print(example_python_model)



# Calculation:
#     Equal | Plus | Minus | Multiply | Power | Divide 
# ;

# Equal:
#     variable1 = ID 'equal' variable2 =ID
# ;

# Logical_operation:
#     And | Or | Not 
# ;
