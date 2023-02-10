def doubleChar(str_name):
    final_str = " "
    for items in str_name:
        final_str += items *2 
    return final_str    
 
print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))