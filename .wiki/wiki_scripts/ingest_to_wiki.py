import pandas as pd

df : pd.DataFrame = pd.read_csv("Data/prevalence.csv")
df.to_markdown("../EMOD_Nyanza.wiki/Calibration-Prevalence.md")

df : pd.DataFrame = pd.read_csv("Data/onart.csv")
df.to_markdown("../EMOD_Nyanza.wiki/Calibration-OnART.md")

df : pd.DataFrame = pd.read_csv("Data/population.csv")
df.to_markdown("../EMOD_Nyanza.wiki/Calibration-Population.md")