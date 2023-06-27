from functions import make_new_part_set


file_path = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Drop_Tests\sims\airbag\drop_tests\vanilla_blower_weight\Weight_hole4.k"
new_file_path = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Drop_Tests\sims\airbag\drop_tests\vanilla_blower_weight\weight_partset.k"
sid = 1600

newfile_text = make_new_part_set(file_path, new_file_path, sid=sid, name='All_AB')

print(newfile_text)
