import pandas as pd
import pandas_profiling as pf

base = pd.read_csv("Clean_Dataset.csv")

report = pf.ProfileReport(base)

report.to_file('perfil_reporte.html')
