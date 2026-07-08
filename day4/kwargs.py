def introduce_student(kwargs):
    print(kwargs)

    if "name" in kwargs:
        print(f"Hello, my name is {kwargs['name']}.")

introduce_student(name="Sarishma", age=20, city="ktm")