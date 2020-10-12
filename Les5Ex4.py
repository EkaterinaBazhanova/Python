with open("zad4_1.txt", "r", encoding="utf-8") as f_obj_1:
    line_1 = f_obj_1.readline()
    line_1 = line_1.replace("One", "Один")
    line_2 = f_obj_1.readline()
    line_2 = line_2.replace("Two", "Два")
    line_3 = f_obj_1.readline()
    line_3 = line_3.replace("Three", "Три")
    line_4 = f_obj_1.readline()
    line_4 = line_4.replace("Four", "Четыре")
new_list = [line_1, line_2, line_3, line_4]
with open("zad4_2.txt", "w", encoding="utf-8") as f_obj_2:
   f_obj_2.writelines(new_list)
