# Andrew Shen, 06/22/2022
# Script to process qPCR data and pipe into Benchling, input qPCR file is in csv form
# To run: python process_qpcr.py <path to input file>

import sys
import pandas as pd

# Assign input files
qpcr_in = sys.argv[1]

# Read in input qPCR file
df = pd.read_csv(qpcr_in)

# Connect to Benchling



# Package data


# Upload to Benchling


print(df)
