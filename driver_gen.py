import random
import string


class Person:
    """Person class
    parameters:
    FirstName: The first name of the person
    MiddleName: The Middle name of the person if any
    LastName: The last name of the person
    DateOfBirth: DD-MM-YYYY
    Sex:    M/F
    """

    def __init__(self, first_name, middle_name, surname, dob, sex):
        self.first_name = first_name
        self.middle_name = middle_name
        self.surname = surname
        self.dob = dob
        self.sex = sex


def get_person_details() -> Person:
    """
    Get input from user and return a person object
    """
    f_name = input("First Name: ").strip()
    m_name = input("Middle Name: ").strip()
    surname = input("Surname: ").strip()
    dob = input("Enter DOB (DD-MM-YYYY):").strip().split("-")
    sex = input("Sex M/F: ").lower().strip()

    return Person(f_name, m_name, surname, dob, sex)


def generate_drivers_license(person) -> str:
    """
    Using the supplied person object generate a UK driver license number based on the specified details below:
    Digit 1–5: The first five characters of the lastname (extra 9’s added for surnames shorter than 5 letters)
    Digit 6: The decade digit from the year of birth (e.g. for 1977 it would be 7)
    Digit 7–8: The month of birth (+5 for the first character if female)
    Digit 9–10: The day in the month of birth
    Digit 11: The year digit from the year of birth (e.g. for 1977 it would be 7)
    Digit 12–13: The first two initials of the first surnames, (9 if no middle surname)
    Digit 14: Arbitrary digit – often 9
    Digit 15–16: Two computer digits

    parameters:
    Person object :Person

    Returns:
    License number :str
    """
    day, month, year = person.dob
    while len(person.surname) < 5:
        person.surname += "9"
    if person.sex == "f" or person.sex == "F":
        month = f"5{month[-1]}"

    if person.middle_name == "" or person.middle_name == "none":
        return f"{person.surname[:5].upper()}{year[2:3]}{month}{day}{year[3:4]}{person.first_name[:1]}9{random.randint(8,9)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"
    else:
        return f"{person.surname[:5].upper()}{year[2:3]}{month}{day}{year[3:4]}{person.first_name[:1]}{person.middle_name[:1]}{random.randint(8,9)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"

def main():
  license = generate_drivers_license(get_person_details())
  print(f"Your License number: {license}")

if __name__ == "__main__":
    main()
