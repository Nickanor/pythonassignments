# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for value in students:
#     print value["first_name"],value["last_name"]


users = {
 'Students': [
     {'num': 1, 'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'num': 2, 'first_name' : 'John', 'last_name' : 'Rosales'},
     {'num': 3, 'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'num': 4, 'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'num': 1, 'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'num': 2, 'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for keys in users:
    print(keys)
    for value in users[keys]:
        print value["num"], "-", value["first_name"], value["last_name"],"-", len(value["first_name"]) + len(value["last_name"])
