#############################################################
#
# Normal distribution values
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
question = ncha$N3Q71

#### mean
myMean = mean(question, na.rm = TRUE)


#### SD
mySD = sd(question, na.rm = TRUE)
#### below the mean
myVal = myMean - 1.23*mySD
myVal

pnorm(myVal, mean = myMean, sd = mySD) # prob less than
pnorm(myVal, mean = myMean, sd = mySD, lower.tail = FALSE) # prob larger than
