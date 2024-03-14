from faker import Faker
import random



fake = Faker()

print(fake.name())
print(fake.random.randint(1, 10))
print(fake.password())
print(fake.url())
print(fake.sentence())