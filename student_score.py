# -*- coding: utf-8 -*-
"""Student Score.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GEwPUj8yE6kRP-ck2N-1gJBPzsmj_iDX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("student_scores.csv")

df.columns

"""Data Cleaning"""

df.describe()

df.isna().sum()

del[df["Unnamed: 0"]]

#drop unnamed column
df.shape

#replacing wrong values in a column to correct values
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("5-Oct","5-10")

"""Data Analysis"""

we = sb.countplot(x = "Gender", data = df)
sb.set(rc = {"figure.figsize" : (3,3)})
plt.ylabel("No of Students")
plt.xlabel("Gender")
plt.title("Gender wise Distribution")
for bars in we.containers:
  we.bar_label(bars)

# from the above chart , we found out the number of females are slighly more than number of males.

gp = df.groupby("ParentEduc").agg({"WritingScore":"mean","MathScore":"mean","ReadingScore":"mean"})
sb.heatmap(gp, annot = True)
sb.set(rc = {"figure.figsize": (10,5)})

# from above heatmap, we concluded that parent's educatiom have good impact on student's score.
# For eg- kids of parents with master's degree have better average score compared to other parents.

gp1 = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
sb.heatmap(gp1, annot = True)

#from this above heatmap we concluded that the parent marital status do not have any significant impact or negligible impact on their kids scores.

sb.boxplot(x = "MathScore", data = df)
sb.set(rc = {"figure.figsize" : (15,2)})

sb.boxplot(x = "WritingScore", data = df)
sb.set(rc = {"figure.figsize" : (15,2)})

sb.boxplot(x = "ReadingScore", data = df)
sb.set(rc = {"figure.figsize" : (15,2)})

#from the above boxplots of all three subjects we can see that the minimum range of Math is much at lower side compared to other two subjects and also there is zero score in Math unlike other two. We can conclude math is toughest subject here.

dt = df["EthnicGroup"].value_counts()

plt.pie(dt,labels = dt.index,autopct='%1.1f%%')
plt.title("Distribution of Ethnic Groups")
sb.set(rc = {"figure.figsize": (20,5)})

# from the above pie chart we conclude that group c contributes the highest number of students followed by group d, group b, group e, group a.