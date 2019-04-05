meter_dic = {'meter': 1, 'foot': 3.28 ,'in':39.377}
in_num = float(input("how many?"))
in_unit = input("from what unit?:")
out_unit = input('to what unit:')
print (f"{in_num}{in_unit} is {in_num / meter_dic[in_unit] *meter_dic[out_unit]}")
