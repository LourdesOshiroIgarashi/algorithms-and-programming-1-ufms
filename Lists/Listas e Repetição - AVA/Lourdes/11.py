x = float(input())                               
y = int(input())                                 
somatorio = []                                   
formula = 0                                      
soma = 0                                         
                                                 
                                                 
for i in range(1, y + 1):                        
    formula = i * x ** i / i ** 2                
    somatorio.append(print(f"{formula:.3f}", end=" "))
    soma = soma + formula                              
                                                 
print(f"\n\nO valor do somatório é: {soma:.4f}")   
