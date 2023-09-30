import random

# Define lists of possible name components for each ethnicity
ethnicities = { "default": 
               { "first_names": [ "Sim", "Bella", "Bob", "Nina", "Dina", "Don"],
                "last_name": ["Pancakes", "Landgraab", "Caliente", "Pleasant", "Lothario"],
                },
                "french": 
                { "first_names": [ "Jean", "Pierre", "Marie", "Claude", "Francois", "Jacques", "Elodie"],
                "last_name": ["Dubois", "Lefevre", "Leroy", "Moreau", "Fournier", "Girard", "Bonnet"],
                },
                "nigerian":
                { "first_names": [ "Sade", "Ayofemi", "Chinara", "Michael", "Adesina", "Olamide"],
                 "last_name": ["Adeoye", "Adeyemi", "Baba","Balogun", "Emem", "Igwe", "Nwadike"],
                 },
            }

# Function to generate a Sims name with a specified ethnicity

def generate_sims_name(ethnicity="default"):
    if ethnicity not in ethnicities: ethnicity = "default"  

    #Generate a Sims name with a specified ethnicity.
    first_name = random.choice(ethnicities[ethnicity]["first_names"])
    last_name = random.choice(ethnicities[ethnicity]["last_name"])
    return first_name + " " + last_name

# Generate and print a Sims name with a specific ethnicity
sims_name = generate_sims_name("french")
print("Generated Sims Name (French):", sims_name)