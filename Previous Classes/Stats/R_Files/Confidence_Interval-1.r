#############################################################
#
# Confidence interval for a mean
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

#### mean, SD, and SE
myMean = mean(ncha$N3Q69, na.rm = TRUE)
mySD = sd(ncha$N3Q69, na.rm = TRUE)
n = sum(!is.na(ncha$N3Q69))
mySE = mySD / sqrt(n)

#### t star
tStar = qt( (1 - .99) / 2, df = 148, lower.tail = FALSE )

#### confidence interval
myMean - tStar*mySE
myMean + tStar*mySE

