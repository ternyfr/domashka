input_string = input("введи названия продуктов:")
p_list = input_string.split(", ")
i = 0
n = 1
while i < len(p_list):
    print(f"{n}) {p_list[i]}")
    i += 1
    n += 1