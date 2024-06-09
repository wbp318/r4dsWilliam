# Use Python within R
py_run_string("import numpy as np")
np <- import("numpy")
np$array(c(1, 2, 3, 4, 5))