def get_omega_from_last_collection():  # assumes that the last Bluesky scan was an MX collection
    for omega in db[-1].data('omega'):
        print(f'omega: {omega}')
