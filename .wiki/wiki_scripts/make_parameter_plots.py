import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('svg')

df = pd.read_csv("../../resampled_parameter_sets.csv").drop(["iteration_number","likelihood","parameterization_id","run_number","sim_id"], axis=1)

for column in df.columns:
    plt.figure()
    df[column].hist()
    plt.xlabel(column)
    plt.savefig(f"C:/Users/kaftad01/Code/EMOD_Nyanza/.wiki/images/{column}.svg")
    plt.close()