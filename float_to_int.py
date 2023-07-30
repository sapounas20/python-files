import re

def round_floats(string):
    # split the string into individual elements
    elements = re.findall(r'[+-]?\d+(?:\.\d+)?|\*|\^|[A-Za-z]+', string)
    
    # iterate over the elements and round the floats
    for i in range(len(elements)):
        # check if the element is a float
        if re.match(r'[+-]?\d+(?:\.\d+)?', elements[i]):
            # round the float to the nearest integer
            elements[i] = str(round(float(elements[i])))
    
    # join the elements back into a string
    new_string = ''.join(elements)
    
    return new_string


ex= round_floats() #βαλε εδω το κείμενο σου 
print(ex)

