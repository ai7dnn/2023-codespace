from faker import Faker

fake = Faker('ko-KR')
fake.name()
fake.address()
fake.color()
fake.country()

test_data = [(fake.name(), fake.address(), fake.country()) for i in range(10)]
test_data