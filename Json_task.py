import json


data = {
    "Model" : "Malibu",
    "Rang" : "Qora",
    "Yil":2020,
    "Narh":40000
}

data_js = json.dumps(data, indent=4)
print(data_js)

talaba_json = {
    "ism":"Hasan",
    "familiya":"Husanov",
    "tyil":2000
}

talaba_json = json.dumps(talaba_json, indent=4)

talaba = json.loads(talaba_json)
print(talaba["ism"] +" "+ talaba["familiya"])
print(talaba)

filename = 'students.json'
with open(filename, 'r') as f:
    student =  json.load(f)

for st_dent in student['student']:
    print(f"{st_dent['name']} {st_dent['lastname']} {st_dent['year']}-kurs {st_dent['faculty']} fakultet talabasi")