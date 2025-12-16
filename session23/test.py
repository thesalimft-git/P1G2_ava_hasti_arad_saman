def is_float(x:str | float) -> bool:
    if type(x) == float or type(x) == int:
        return True
    
    if type(x) == str:
        try:
            x = float(x)
            return True
        except:
            return False
    
    return False
