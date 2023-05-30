from make_sims import make_sim

source_dir = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Sled Test\sims\airbag\drop_tests\vanilla_blower"
main_dir = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Sled Test\sims\airbag\drop_tests"

Parameters = {'vent': [3.0],
              'start': [1000],
              'height': [3.0, 6.0],
              'blow_v': [14000],
              'blow_s': [300],
              'stiffness': [1, 5, 25]}

for i in Parameters['vent']:
    for j in Parameters['start']:
        for k in Parameters['height']:
            for l in Parameters['blow_v']:
                for m in Parameters['blow_s']:
                    for n in Parameters['stiffness']:
                        parameters = {'vent_d': i,
                                      'start': j,
                                      'term': 2000,
                                      'height': k,
                                      'blow_v': l,
                                      'blow_s': m,
                                      'ea': n}

                        make_sim(parameters, source_dir, main_dir)
