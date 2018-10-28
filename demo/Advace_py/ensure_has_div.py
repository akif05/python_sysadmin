# items = [2, 36, 25, 9, 48]
# devisor = 12
#
# for item in items:
#     if item % devisor == 0:
#         found = item
#         break
# else:
#     itmes.append(devisor)
#     found = devisor
#
# print(f"{items} contains {found} which is a multiple of {devisor}")
#
# #print("{items} contains {found} which is a multiple of {devisor}"
# #      .format(**locals()))

## Folowing and previous code are doing identical job

def ensure_has_div(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
        items.append(divisor)
        return divisor

items = [2, 25, 9]
divisor = 12

dividend = ensure_has_div(items, divisor)
print (f"{items} contains {divisor} which is multiplier by {divisor}")