"""
    Generator and list performance comparison
"""

import random
import time

import memory_profiler as mem_profile

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "CompSci", "Arts", "Business"]

print(f"Memory (Before): {mem_profile.memory_usage()} MB")


def people_list(num_people):
    """people list"""
    result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "majors": random.choice(majors),
        }
        result.append(person)
    return result


def people_generator(num_people):
    """people generator"""
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "majors": random.choice(majors),
        }
        yield person


t1 = time.process_time()
# people = people_list(1000000)
people = people_generator(1000000)
# for person in people:
#     print(person)
t2 = time.process_time()

print(f"Memory (After): {mem_profile.memory_usage()} MB")
print(f"Took {t2-t1} Seconds")
