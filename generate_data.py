"""
Unstructured Data Generator

Generates semi-structured data in JSON, XML, and CSV formats with 1000-2000 records each.
Files saved to DATA directory with unique IDs.
"""

import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
import csv
import random
import os
import datetime
import uuid

def generate_person_data():
    """Generate list of person dictionaries with semi-structured fields."""
    data = []
    num_records = random.randint(1000, 2000)
    for i in range(num_records):
        person = {
            "name": f"Person {i}",
            "age": random.randint(20, 60),
            "city": random.choice(["New York", "Los Angeles", "Chicago"]),
            "phone": f"555-{random.randint(100,999)}-{random.randint(1000,9999)}"
        }
        if random.choice([True, False]):
            person["email"] = f"person{i}@example.com"
        data.append(person)
    return data

def generate_json_data(people):
    """Return JSON data from people list."""
    return people

def generate_xml_data(people):
    """Generate XML tree from people list."""
    root = ET.Element("people")
    for person in people:
        p = ET.SubElement(root, "person")
        for key, value in person.items():
            ET.SubElement(p, key).text = str(value)
    return root

def generate_csv_data(people):
    """Generate CSV rows from people list, adding occupation."""
    data = []
    occupations = ["Engineer", "Teacher", "Doctor", "Artist", "Manager", "Developer"]
    for person in people:
        row = [person["name"], str(person["age"]), person["city"], person.get("email", ""), person["phone"], random.choice(occupations)]
        data.append(row)
    return data

def main():
    """Main function to generate and save data files."""
    output_dir = r"C:\Users\jusamano\OneDrive - Microsoft\Documents\DATA"
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.date.today().isoformat()
    unique_id = uuid.uuid4().hex[:8]
    
    people = generate_person_data()
    
    # JSON
    json_data = generate_json_data(people)
    json_filepath = os.path.join(output_dir, f"Data_json_{date_str}_{unique_id}.json")
    with open(json_filepath, "w") as f:
        json.dump(json_data, f, indent=4)
    print(f"JSON saved to {json_filepath}")
    
    # XML
    xml_data = generate_xml_data(people)
    xml_filepath = os.path.join(output_dir, f"Data_xml_{date_str}_{unique_id}.xml")
    rough_string = ET.tostring(xml_data, encoding="utf-8")
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")
    with open(xml_filepath, "wb") as f:
        f.write(pretty_xml)
    print(f"XML saved to {xml_filepath}")
    
    # CSV
    csv_data = generate_csv_data(people)
    csv_filepath = os.path.join(output_dir, f"Data_csv_{date_str}_{unique_id}.csv")
    with open(csv_filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "city", "email", "phone", "occupation"])
        writer.writerows(csv_data)
    print(f"CSV saved to {csv_filepath}")

if __name__ == "__main__":
    main()