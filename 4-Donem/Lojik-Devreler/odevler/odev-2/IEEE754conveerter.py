# -*- coding: utf-8 -*-
def decimal_to_binary(decimal, resolution):
    binary = ""
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    # Convert integer part to binary
    binary += bin(integer_part)[2:]
    #fraction resolution assigned
    fractionres = resolution - len(binary)
    # Convert fractional part to binary
    binary += "."
    for _ in range(fractionres):
        fractional_part *= 2
        bit = int(fractional_part)
        binary += str(bit)
        fractional_part -= bit

    return binary

def binary_to_decimal(binary, resolution):
    integer_part, fractional_part = binary.split(".")

    # Convert integer part to decimal
    decimal = int(integer_part, 2)
    #fraction resolution assigned
    fractionres = resolution - len(integer_part)
    # Convert fractional part to decimal
    for i in range(fractionres):
        bit = int(fractional_part[i])
        decimal += bit / 2**(i+1)

    return decimal

def calculate_error(decimal, binary, resolution):
    converted_decimal = binary_to_decimal(binary, resolution)
    error = abs(decimal - converted_decimal)
    return error
def decimal_to_ieee754(decimal , representation = 'single'):
    if representation == 'single':
        resolution = 23 + 1
        
    elif representation == 'double':
        resolution = 52 + 1
    else: return 'represtentation error' 
    binary = decimal_to_binary(decimal,resolution)
    converted_decimal = binary_to_decimal(binary, resolution)
    error = calculate_error(decimal, binary, resolution)
    exponent = str(len(binary.split('.')[0])-1)
    base = '2'
    mantissa = binary.split('.')[0][0] + '.' + binary.split('.')[0][1:] + binary.split('.')[1]
    return (binary, converted_decimal, error, mantissa+'x'+ base + '^' + exponent)

decimal = 67.5123
binary,converted_decimal,error, ieeenumber1_1 = decimal_to_ieee754(decimal)
print('Single presicion için işlemler\n')
print(f"Binary: {binary},\nConverted Decimal: {converted_decimal},\nError: {error},\nIEEE754 single representation: {ieeenumber1_1}")

binary,converted_decimal,error, ieeenumber1_2 = decimal_to_ieee754(decimal,'double')
print('Double presicion için işlemler\n')
print(f"Binary: {binary},\nConverted Decimal: {converted_decimal},\nError: {error},\nIEEE754 double representation: {ieeenumber1_2}")

#for negative number
decimal = abs(-152.23813 )
binary,converted_decimal,error, ieeenumber2_1 = decimal_to_ieee754(decimal)
ieeenumber2_1 = '-'+ ieeenumber2_1
print('Single presicion için işlemler\n')
print(f"Binary: -{binary},\nConverted Decimal: -{converted_decimal},\nError: {error},\nIEEE754 single representation: {ieeenumber2_1}")

binary,converted_decimal,error, ieeenumber2_2 = decimal_to_ieee754(decimal,'double')
ieeenumber2_2 = '-'+ ieeenumber2_2
print('Double presicion için işlemler\n')
print(f"Binary: -{binary},\nConverted Decimal: -{converted_decimal},\nError: {error},\nIEEE754 double representation: {ieeenumber2_2}")


def add_ieee754_single(num1, num2):
    if num1[0] == '-': sign1 = '-' 
    else: sign1 = '+' 
    if num1[0] == '-': sign1 = '-' 
    else: sign1 = '+' 
        
    # Extract mantissa, base, and exponent from num1
    mantissa1 = num1.split('x')[0].replace('.', '')
    exponent1 = int(num1.split('^')[1])

    # Extract mantissa, base, and exponent from num2
    mantissa2 = num2.split('x')[0].replace('.', '')
    exponent2 = int(num2.split('^')[1])

    # Adjust the exponents
    diff = exponent1 - exponent2
    if diff > 0:
        mantissa2 = mantissa2 + '0' * diff
    else:
        mantissa1 = mantissa1 + '0' * abs(diff)

    # Convert the mantissas to integers
    int_mantissa1 = int(mantissa1, 2)
    int_mantissa2 = int(mantissa2, 2)

    # Add the mantissas
    sum_mantissa = int_mantissa1 + int_mantissa2

    # Normalize the result and adjust the exponent if necessary
    if sum_mantissa >= (1 << len(mantissa1)):
        sum_mantissa >>= 1
        exponent1 += 1

    # Construct the result in IEEE 754 single precision format
    result = f"{bin(sum_mantissa)[2:].zfill(len(mantissa1))}x2^{exponent1}"

    return result


# Example usage
num1 = '1.0000111000001100100110x2^6'
num2 = '-1.0011000001111001111011x2^7'

result = add_ieee754_single(num1, num2)
print(f"Result: {result}")



