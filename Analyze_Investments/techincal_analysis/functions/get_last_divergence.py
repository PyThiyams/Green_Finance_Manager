
def get_divergence(results):

    if results:
        for date, divergence in reversed(results):
            if divergence != 'None':
                print("date of DIVERGENCE:", date)
                print("divergence of DIVERGENCE:", divergence)
                return date, divergence

    return None, None
