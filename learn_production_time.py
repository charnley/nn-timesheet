"""

    Notes
    - Not included bankholidays


"""

import matplotlib.pyplot as plt
import pandas as pd
import pickle

def save_obj(name, obj):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def main():

    # TODO maybe make a sqlite db?

    # TODO Sort by analyse navn (hash, index it)
    # TODO Translate dates to days
    # TODO Clean null cells
    # TODO Clean dummy
    # TODO Ignore if no deadline

    # TODO gaussian distribution of all tests
    # - if sample size is > 20 (note the discarded)


    # xsl = pd.read_excel("LIMS_historic_data2.xlsx", sheet_name="Raw data", nrows=400)
    # save_obj("subset", xsl)

    xsl = load_obj("subset")

    xsl = xsl.dropna()

    dates_deadline = xsl["deadline_date"] - xsl['sample_recievedate']
    dates_actual = xsl["sample_reviewdate"] - xsl['sample_recievedate']

    days_deadline = dates_actual.dt.days.values
    days_actual = dates_deadline.dt.days.values


    # bin it



    return


if __name__ == "__main__":
    main()
