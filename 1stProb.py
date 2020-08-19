def brackets(expr) : 
    stack = [] 
  
      
    for char in expr: 
        if char in ["(", "{", "["]: 
  
            
            stack.append(char) 
        else:   
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return char.index(current_char)
            if current_char == '{': 
                if char != "}": 
                    return char.index(current_char)
            if current_char == '[': 
                if char != "]": 
                    return char.index(current_char)
  

    if stack: 
        return False
    return True
  
  

if __name__ == "__main__" :  
    expr = "{}[]";  
    if brackets(expr) : 
        print("Success") 
    else : 
        x = expr.index(expr)
        print(x)