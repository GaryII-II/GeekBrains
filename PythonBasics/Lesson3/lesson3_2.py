# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task2. Function for user details print

# имя, фамилия, год рождения, город проживания, email, телефон
def user_data_show(name='Unknown', surname='Unknown', birth=1900, city='Unknown', email='Unknown', phone='Unknown'):
    print(f'User {name} {surname}, born in {birth} lives at {city}. Contact by email {email} or phone {phone}')

user_data_show(email='j.smith@bbb.com', birth=2001, city='Bristol', phone='+44777555990', name='John', surname='Smith')
