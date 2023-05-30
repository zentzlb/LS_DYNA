from functions import make_new_element_set


file_path = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Sled Test\sims\airbag\drop_tests\vanilla_blower\AB_Train13_1300CFM_orf_v10_blower.k"
new_file_path = r"Element_Set.k"
pid = 1402

make_new_element_set(file_path, new_file_path, 'z+406.4', tolerance=0.1, pid=pid)
