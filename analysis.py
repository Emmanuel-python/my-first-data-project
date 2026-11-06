#My first data analysis
#By Emmanuel Peter 
import pandas as pd

data = {
  'Name': ['Praise', 'Joy', 'Favour', 'Tunde', 'Samuel'],
  'Age': [17,15,18,16,14],
  'Score': [87,91,82,81,77],
}

df = pd.DataFrame(data)

print("My First Dataset:")
print(df)
print("\nAverage Score:", df['Score'].mean())
print("Highest Score:", df['Score'].max())

  
