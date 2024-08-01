
def complex_operations(str_complex1 , str_complex2):
    try:

        complex1=complex(str_complex1)
        complex2=complex(str_complex2)

        addition= complex1+complex2
        subtraction= complex1-complex2
        multiplication= complex1*complex2
        division= complex1/complex2

        return (addition, subtraction, multiplication, division)
    except ValueError:
        return "Error: One or both of the input strings are not valid complex numbers."
result= complex_operations("2+5j" , "1+6y")
print(result)
