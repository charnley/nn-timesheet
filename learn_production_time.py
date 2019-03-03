"""

    Notes
    - Not included bankholidays


"""

import pandas as pd

def main():

    # TODO maybe make a sqlite db?

    # TODO Sort by analyse navn (hash, index it)
    # TODO Translate dates to days
    # TODO Clean null cells
    # TODO Clean dummy
    # TODO Ignore if no deadline

    # TODO gaussian distribution of all tests
    # - if sample size is > 20 (note the discarded)


    xsl = pd.read_excel("LIMS_historic_data2.xlsx")


    return


if __name__ == "__main__":
    main()
