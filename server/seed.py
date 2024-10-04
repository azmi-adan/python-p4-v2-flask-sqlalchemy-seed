#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet
from random import choice as rc
from faker import Faker

with app.app_context():
    #create and initialize faker generator
    fake = Faker()

    Pet.query.delete()

    # Create an empty list
    pets = []
    species = ['Dog', 'Cat', 'chicken', 'hamster','turtle']
    for i in range(10):
        pet= Pet( name =fake.first_name(), species = rc(species))
        pets.append(pet)
        db.session.add_all(pets)


    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()