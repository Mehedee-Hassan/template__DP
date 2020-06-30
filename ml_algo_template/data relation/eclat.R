# Eclat

# Data Preprocessing
# install.packages('arules')
library(arules)
path = "C:\\Users\\mehedee\\Documents\\Python Scripts\\tutorial\\Artificial_Neural_Networks\\ML_DS\\data relation\\"


tt = paste(path,'Market_Basket_Optimisation.csv',sep='')

dataset = read.csv(tt)
dataset = read.transactions(tt, sep = ',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Eclat on the dataset
rules = eclat(data = dataset, parameter = list(support = 0.004, minlen = 2))

# Visualising the results
inspect(sort(rules, by = 'support')[1:10])