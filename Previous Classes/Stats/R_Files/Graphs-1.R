#############################################################
#
# Creating various plots in R
#
#############################################################
## Load the library to read the excel file
library(readxl)


#### You will need to change this value for your own computer
dataDir = "D:/School/CS/School-Projects/Stats/R_Files"

### Read in the Dataset
ncha = read_excel(paste(dataDir, 
                "NCHA-III WEB SPRING 2021 UTAH VALLEY UNIVERSITY  - TIMESTAMP.xlsx", 
                sep = "/"), sheet = "NCHA-III WEB SPRING 2021 UTAH V")

ncha = as.data.frame(ncha)

WYD_Weight = ncha$N3Q5
Num_Bevs = ncha$N3Q9A

table(Num_Bevs)
#### Pie chart
pie(table(WYD_Weight), main = "Are you trying to do any of the following about your weight")


#### Bar Chart
barplot(table(WYD_Weight), main = "Are you trying to do any of the following about your weight?", ylab="Response Count")


#### Histogram
hist(Num_Bevs, main = "Number of sugar-sweetened beverages in a day", xlab = "# of Beverages", ylab="Response Count")

#### Boxplot
boxplot(Num_Bevs, horizontal = TRUE, main = "Number of sugar-sweetened beverages in a day")

#### Side-by-Side boxplots
boxplot(Num_Bevs ~ WYD_Weight, ylab = "Number of sugar-sweetened beverages in a day", xlab = "Are you trying to do any of the following about your weight")
