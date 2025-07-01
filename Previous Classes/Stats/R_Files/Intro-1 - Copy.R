#############################################################
#
# Get to know R and the ncha dataset 
#
#############################################################


##### Read in the data
##### This requires an additional R package
##### You can install this package by running the code below, but
#####   only do so once. 

## highlight code to run once
# install.packages("readxl")

## Load the library to read the excel file
library(readxl)


#### Create a variable with the folder directory for the data file. You will
####    need to change this value for your own computer
dataDir = "D:/School/CS/School-Projects/Stats/R_Files"

### Read in the Dataset
ncha = read_excel(paste(dataDir, 
                "NCHA-III WEB SPRING 2021 UTAH VALLEY UNIVERSITY  - TIMESTAMP.xlsx", 
                sep = "/"), sheet = "NCHA-III WEB SPRING 2021 UTAH V")

ncha = as.data.frame(ncha)
### Find the number of rows and columns
nrow(ncha)
ncol(ncha)

### Access the value in a specific location. 
### Remember that the format is [row number, column number]

ncha[100, 52]

### Table function and accessing a specific variable
table(ncha$RSEX)

### A couple other items to just run
x = ncha$N3Q6
y = ncha$N3Q7

z = x + y
z[10]

x[100] == y[200]

######## DATA PROJECT: Brief Exploration ########
# 1. How many rows are there in the data?
nrow(ncha)

# 2. How many columns are there in the data?
ncol(ncha)

# 3. What is the value in the 100th row, and the 52nd column?
ncha[100, 52]
#    a. What is the value in the 150th row and 53rd column?
ncha[150, 53]

# 4.What is the breakdown of the variable 'RSEX'?
table(ncha$RSEX)
#    a. What is the breakdown of the variable 'N3Q1'?
table(ncha$N3Q1)

# 5. Save the value of N3Q6 as x, and the value of N3Q7 as y
x = ncha$N3Q6
y = ncha$N3Q7
#    a. Add x + y (save it as another variable) and find the 10th value
z = x + y
z[10]
#    b. Multiply x*y and find the 11th value.
z = x * y
z[11]
#    c. Test if the 100th value of x is equal to the 200th value of y
x[100] == y[200]
#    d. Test if the 150th value of x is equal to the 250th value of y
x[150] == y[250]