students ={
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Gryffindor"
}

for i in students:
    print(i, ' ' ,students[i]) #i - Key , students[i] - Value


#--------------------------------------------#

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft["Launch Year"] = 1968
    spacecraft["Country"] = "USA"
    spacecraft.update({"Orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== Report ========
    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU
    Year: {spacecraft["Launch Year"]}
    Status: {spacecraft.get("Active Status","Unknown")}
    MF: {spacecraft.get("Country","Unknown")}
    Orbit: {spacecraft["Orbit"]}
    ========================
    """

main()

#--------------------------------------------#


marks_dict ={
    "Maths" : 80,
    "Science" : 85,
    "English" : 80,
}

get_input = input("Subject: ").title()

if get_input in marks_dict:
    print(f"Marks: {marks_dict[get_input]}")