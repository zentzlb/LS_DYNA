from functions import make_new_part_set


file_path = r"C:\Users\Logan.Zentz\Documents\Sled Test\sims\airbag\v3\AB_Train13_1300CFM_orf_v8_6x10.k"
new_file_path = r"C:\Users\Logan.Zentz\Documents\Sled Test\sims\airbag\v3\Part_Set.k"
sid = 1600

newfile_text = make_new_part_set(file_path, new_file_path, sid=sid, name='All_AB')

print(newfile_text)
