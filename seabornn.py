# %%
import seaborn as sns

tips = sns.load_dataset('tips')

DataHead = tips.head()
print(DataHead)
sns.displot(tips["total_bill"])

# %%
import seaborn as sns
tips = sns.load_dataset('tips')

# sns.jointplot(x="total_bill",y="tip", data=tips)
sns.pairplot(tips,hue="sex")
# %%
