import pandas as pd

df = pd.DataFrame({
    'vertigo': ['crash', 'forever//over', 'gold'],
    'no future': ['hertz', 'isohel', 'untitled'],
    'ICYMI': ['Modern Warfare', 'PS1', 'Elsewhere']
})

print(df.to_string(index=False))