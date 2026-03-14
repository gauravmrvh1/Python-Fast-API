from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot([0, 1, 2, 3, 4, 5])
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
# sns.displot(random.normal(size=1000), kind="kde")
# sns.displot(random.binomial(n=10, p=0.5, size=1000))


# data = {
#   "normal": random.normal(loc=50, scale=5, size=1000),
#   "binomial": random.binomial(n=100, p=0.5, size=1000)
# }
# sns.displot(data, kind="kde")


sns.displot(random.uniform(size=1000), kind="kde")
sns.displot(random.logistic(size=1000), kind="kde")


# random.seed(2)
# x = random.normal(3, 1, 100)
# y = random.normal(150, 40, 100) / x
# plt.scatter(x, y)


plt.show()