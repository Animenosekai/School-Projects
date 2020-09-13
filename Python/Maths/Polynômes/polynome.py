"""
Mathématiques / Polynômes du second degré
> Construire un algorithme qui affiche les coefficients du polynôme, le discriminant Δ et les solutions de l'équation: ax^2 + bx + c = 0
"""
import json
import math
import lifeeasy

class Discriminant():
    """
    A Second Degree Polynomial Discriminant (Δ) object.
    
    Takes 3 arguments: the first coefficient (coef_a), the second one (coef_b) and the 'constant' or third coefficient (const_c).
    Returns a Discriminant Object with multiple information including the steps to obtain the result, the passed arguments, a tuple with the coefficients, the result itself but also the string representation of the formula.

    Δ.value returns the value of the discriminant.
    The representation of the object (__repr__) is a string containing Δ.value.

    to_dict() returns a python dictionary representation of the object.
    to_json() returns a json string representation of the object.
    """
    def __init__(self, coef_a, coef_b, const_c):
        self.coef_a = coef_a
        self.coef_b = coef_b
        self.const_c = const_c
        self.coefficients = (self.coef_a, self.coef_b, self.const_c)
        self.steps = []
        self.steps.append(str(self.coef_b) + '**2 - 4 * ' + str(self.coef_a) + ' * ' + str(self.const_c))
        self.steps.append(str(self.coef_b ** 2) + ' - 4 * ' + str(self.coef_a) + ' * ' + str(self.const_c))
        self.steps.append(str(self.coef_b ** 2) + ' ' + str(-4 * self.coef_a) + ' * ' + str(self.const_c))
        self.steps.append(str(self.coef_b ** 2) + ' ' + str(-4 * self.coef_a * self.const_c))
        self.steps.append(str((self.coef_b**2) - (4*self.coef_a*self.const_c)))
        self.value = (self.coef_b**2) - (4*self.coef_a*self.const_c)
    
    formula = 'b^2 - 4ac'
    python_formula = 'b**2-4ac'

    def to_dict(self):
        """
        Returns a python dictionary representation of the Discriminant object.
        """
        result = {}
        result['formula'] = 'b^2 - 4ac'
        result['python_formula'] = 'b**2-4ac'
        result['coefficients'] = (self.coef_a, self.coef_b, self.const_c)
        result['steps'] = []
        result['steps'].append(str(self.coef_b) + '**2 - 4 * ' + str(self.coef_a) + ' * ' + str(self.const_c))
        result['steps'].append(str(self.coef_b ** 2) + ' - 4 * ' + str(self.coef_a) + ' * ' + str(self.const_c))
        result['steps'].append(str(self.coef_b ** 2) + ' ' + str(-4 * self.coef_a) + ' * ' + str(self.const_c))
        result['steps'].append(str(self.coef_b ** 2) + ' ' + str(-4 * self.coef_a * self.const_c))
        result['steps'].append(str((self.coef_b**2) - (4*self.coef_a*self.const_c)))
        result['discriminant'] = (self.coef_b**2) - (4*self.coef_a*self.const_c)
        return result
        
    def to_json(self):
        """
        Returns a json string representation of the Discriminant object.
        """
        return json.dumps(self.to_dict())
    
    def __repr__(self):
        return str(self.value)

def solve_equation(coef_a, coef_b, const_c):
    """
    Solves an a second degree polynomial equation.
    """
    Δ = Discriminant(coef_a, coef_b, const_c)
    if Δ.value < 0:
        return f'{str(coef_a)}x^2 + {str(coef_b)}x + {str(const_c)} has no solution in the set of real numbers.'
    elif Δ.value == 0:
        return - coef_b / 2 * coef_a
    else:
        return ((- coef_b - math.sqrt(Δ.value)) / 2 * coef_a, - coef_b + math.sqrt(Δ.value) / 2 * coef_a)

def find_coefficients(equation, approach='natural_language'):
    """
    Returns the coefficients of a given equation of the second degree (polynomial of the formula: ax^2+bx+c=0)
    """
    if approach.lower() == 'mathematical':
        pass
    elif approach.lower() == 'natural_language':
        processing_equation = equation.replace(' ', '').replace('\n', '').replace('\t', '').split('=')[0]
        processing_equation_list = processing_equation.replace('x^2', 'x').split('x')
        result = []
        for element in processing_equation_list:
            result.append(float(element.replace('+', '')))
 
        return result

print('Quel est votre équation? (sous la forme ax^2+bx+c = 0)')
user_equation = input('> ')
coefficients = find_coefficients(user_equation)
Δ = Discriminant(coefficients[0], coefficients[1], coefficients[2])
result = solve_equation(Δ.coef_a, Δ.coef_b, Δ.const_c)

lifeeasy.clear()
print(f'Le premier coefficient est: {str(Δ.coef_a)}')
print(f'Le deuxième coefficient est: {str(Δ.coef_b)}')
print(f'Le dernier coefficient est: {str(Δ.const_c)}')
print('')
print(f'Le discriminant est: {str(Δ.value)}')
print(f'Le résultat est: {str(result)}')
