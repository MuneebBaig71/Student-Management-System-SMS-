# print('hello world')
# name = 'muneeb'

# _private_variable = 42



# text = "123"
# is_decimal = text.isdecimal()
# print(is_decimal)  # Output: True

# name: int = 123
# name = 'muneeb'
# # print(type(name))
# print(name)
# name = "muneeb"
# age = 23


# name: list[str] = ["muneeb", "ahmed", "ali"]
# print(name.index("muneeb"))
# print(id(list))
# popped_value = name.pop()
# print(id(popped_value))
# print(name, popped_value)

# name:str = "ada lovelace"
# print(name.title())
C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()