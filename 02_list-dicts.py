# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
# Se retiraron las comillas de los nombres
print(country)
print(capitals)
"""
What response did you get?
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""
#Para poder imprimir el segundo valor de South Africa se retiro el index del los 
# corchetes en donde se encontraba el nombre del pais
print( capitals['South Africa'][1])
"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""
