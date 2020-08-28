# pylint: disable="import-error"
from image_converter import ImageConverter
from graphviz import Digraph
import os

class DotFormatter():
        
    def __init__(self, new_js):
        self.js_ast = new_js
    
    def convert_to_dot_a(self):
        os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz/bin/'
        js_data = self.js_ast
        dot = Digraph(name="G", node_attr={'shape' : 'record'}, format="png")
        
        for a_class in js_data:
            #dot.node('Animal', '{Animal|+ name : string\l+ age : int\l|+ die() : void\l}') 
            current_class = a_class.get("class_name")
            current_class_attributes = a_class.get("class_attributes")
            current_class_attribute_values = a_class.get("class_attribute_values")
            current_class_methods = a_class.get("class_methods")
            #WIP
            current_class_method_values = a_class.get("class_method_values")
            current_class_method_params = a_class.get("class_method_params")
            current_class_associations = a_class.get("class_associations")
            current_class_parent = a_class.get("class_parent")
            #print(current_class_associations)
            current_class_label = '{' + current_class + '| '
            count = 0 
            #relationships = ""
            for attribute in current_class_attributes:
                #current_class_label += f'{attribute} : string\l '
                current_class_label += f'{attribute}'
                # WORK IN PROGRESS
            #for attrib_value in current_class_attribute_values: 
            # Do I want to add logic to remove the ":" if the type is of None?
                #print(current_class_attribute_values)
                attrib_value = current_class_attribute_values[count]
                attrib_type = type(attrib_value).__name__
                #print(attrib_type)
                    #print(attrib_value)
                if attrib_type == "NoneType":
                    attrib_type = ""
                current_class_label += f' : {attrib_type}\l'
                count = count + 1

            current_class_label += "| "
            count = 0
            #print(current_class_method_values)
            for method in current_class_methods: # 
                #print(current_class_method_values)
                current_class_label += method #.format()
                method_params = ""
                for param in current_class_method_params[method]:
                    method_params += param + ', '
                    #print(param)
                
                current_class_label += f"({method_params}) : {current_class_method_values[count]}\l" #.format()
                count = count + 1

            for relationship in current_class_associations:
                #relationships += "{0} -> {1}\n".format(current_class, relationship)
                #print(relationship)
                dot.edge(current_class, relationship)
                #dot.body.append(f'\t{current_class} -> {relationship} [ arrowhead = none ]')
                # Use above code if I want to change arrowhead for basic associations

            if current_class_parent != "":
                dot.body.append(f'\t{current_class} -> {current_class_parent} [ arrowhead = onormal ]')

            current_class_label += "}"
            #current_class_label += "| method1() : void\l}"

            dot.node(current_class, current_class_label) 
        
        dot.render("test") 

        # with open("dot.txt", 'w') as d:
        #     d.truncate()
        #     d.write(dot.source)
        #js_data = self.js_ast
        # with open("boilerplate.txt", 'r') as b:
        #     #d.truncate()
        #     boilerplate = b.read()

        # with open("dot.txt", 'w') as d:
        #     d.truncate()
        #     d.write(boilerplate)
        #     d.write("""
        #         Building [
        #                 label = "{Building|+ name : string\l+ age : int\l|+ die() : void\l}"
        #         ]

        #         Library [
        #                 label = "{Library||+ bark() : void\l}"
        #         ]

        #         House [
        #                 label = "{House||+ meow() : void\l}"
        #         ]
        #     }    
        #     """)

    def convert_to_dot_b(self):
        all_js_classes = self.js_ast

        with open("boilerplate.txt", "r") as boiler_plate:
            dot_notation = boiler_plate.read()

        for a_class in all_js_classes:
            all_attributes = ''
            all_methods = ''
            for a_attribute in a_class["attributes"]:
                all_attributes += "{0}\l".format(a_attribute)

            for a_method in a_class["methods"]:
                all_methods += "{0}()\l".format(a_method)
    
            class_notation = '{0} [ label = "{{ {0}| {1}| {2} }}" ]'.format(a_class["class_name"], all_attributes, all_methods)
            dot_notation += f'{class_notation}\n'
        
        dot_notation += "\n }"
        with open("dot.txt", 'w') as dot_file:
            dot_file.truncate()
            dot_file.write(dot_notation)

    # Shared Methods
    def handle_dot_file(self, current_cmd):
        the_image_converter = ImageConverter()

        if current_cmd == "a":
            the_image_converter.produce_image_a()
        else:
            the_image_converter.produce_image_b()

