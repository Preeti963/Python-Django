recharge_pin = "234223 2344213 2323 5657 2234 2343 6767"
splited_recharge_pin = recharge_pin.split(" ")

encoded_list = []

for i in range(len(splited_recharge_pin)-1):
    encoded_string = "*" * len(splited_recharge_pin[i])  
    encoded_list.append(encoded_string)

encoded_list.append(splited_recharge_pin[-1])   # keep last one as it is

output = " ".join(encoded_list)

print(output)   
