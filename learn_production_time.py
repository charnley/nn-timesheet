"""

    Notes
    - Not included bankholidays


"""

import numpy as np
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

    # xsl = pd.read_excel("LIMS_historic_data2.xlsx", sheet_name="Raw data")
    # xsl = pd.read_excel("LIMS_historic_data2.xlsx", sheet_name="Raw data", nrows=10000)
    # save_obj("subset", xsl)

    xsl = load_obj("subset")

    # remove null rows
    xsl = xsl.dropna()

    col_names = [col for col in xsl]

    print(col_names)

    categories = xsl["analysis_name"]
    # categories = xsl["qc_team"]
    # categories = xsl["sample_id"]

    xsl['sample_recievedate'] = pd.to_datetime(xsl['sample_recievedate'])

    dates_deadline = xsl["deadline_date"].dt.date - xsl['sample_recievedate'].dt.date
    dates_actual = xsl["sample_reviewdate"].dt.date - xsl['sample_recievedate'].dt.date
    dates_wait = xsl["qcbatch_creationdate"].dt.date - xsl['sample_reviewdate'].dt.date

    days_deadline = dates_deadline.dt.days.values
    days_actual = dates_actual.dt.days.values

    # values = list(days_deadline) + list(days_actual)

    categories = categories.values
    categories = np.array(categories, dtype=str)
    unique_categories = np.unique(categories)

    # hmmm
    # test_category = np.argwhere(categories == "Y9-175")
    # test_category = test_category.flatten()
    # print(dates_deadline[test_category])
    # print(dates_actual[test_category])
    # print()
    # print(xsl["sample_recievedate"][test_category])
    # print()
    # print(days_actual[test_category])
    # print(days_deadline[test_category])
    # print(days_actual[test_category]-days_deadline[test_category])

    # quit()

    error = days_actual - days_deadline
    values = error

    binwidth = 1

    bins = np.arange(min(values), max(values) + binwidth, binwidth)

    for i, category in enumerate(unique_categories):

        view, = np.where(categories == category)

        if view.shape[0] < 10:
            print("ignore", category)
            continue

        error = days_actual[view] - days_deadline[view]

        n, axbins, patches = plt.hist(error, bins=bins)
        plt.title(category)
        plt.savefig("results/test_"+str(i)+".png")
        plt.clf()

    return


if __name__ == "__main__":
    main()

