ecof <- read.csv("C:\\Users\\Alex\\Desktop\\economy.csv")
geof <- read.csv("C:\\Users\\Alex\\Desktop\\geography.csv")
demf <- read.csv("C:\\Users\\Alex\\Desktop\\demographics.csv")
socf <- read.csv("C:\\Users\\Alex\\Desktop\\society.csv")
inff <- read.csv("C:\\Users\\Alex\\Desktop\\infrastructure.csv")
cc <- ecof$Country.Code
ecof$Country.Code = NULL
geof$Country.Code = NULL
demf$Country.Code = NULL
socf$Country.Code = NULL
inff$Country.Code = NULL
inff$Natural.Resource.Index_y <- NULL
inff$Industrial.Index_y <- NULL
inff$Instability.Index_y <- NULL
ecof <- as.data.frame(scale(ecof, center = FALSE)[,])
geof <- as.data.frame(scale(geof, center = FALSE)[,])
demf <- as.data.frame(scale(demf, center = FALSE)[,])
socf <- as.data.frame(scale(socf, center = FALSE)[,])
inff <- as.data.frame(scale(inff, center = FALSE)[,])

ecof$Exports <- ecof$Exports*4
ecof$Imports <- ecof$Imports*2
ecof$GDP <- ecof$GDP*5
ecof$GDP.Per.Capita <- ecof$GDP.Per.Capita*5
ecof$Oil.Production <- ecof$Oil.Production*4
ecof$Refined.Petroleum.Production <- ecof$Refined.Petroleum.Production*4
ecof$Score <- ecof$Exports + ecof$Imports + ecof$GDP + ecof$GDP.Per.Capita + ecof$Oil.Production + ecof$Refined.Petroleum.Production

geof$Area <- geof$Area*1
geof$Water.Area <- geof$Water.Area*3
geof$Score <- geof$Area + geof$Water.Area
print(geof$Score)

demf$Population <- demf$Population*5
demf$Dependency.Ratio <- demf$Dependency.Ratio*3
demf$Unemployment <- demf$Unemployment*2
demf$Literacy <- demf$Literacy*2
demf$Poverty <- demf$Poverty*-3
demf$Population.Growth <- demf$Population.Growth*2
demf$Score <- demf$Population + demf$Dependency.Ratio + demf$Unemployment + demf$Literacy + demf$Population.Growth

socf$Net.Migration <- socf$Net.Migration*3
socf$Urban.Population <- socf$Urban.Population*1
socf$Obesity <- socf$Obesity*1
socf$Life.Expectancy <- socf$Life.Expectancy*3
socf$Fertility <- socf$Fertility*2
socf$Internet <- socf$Internet*2
socf$Infant.Mortality <- socf$Infant.Mortality*-3
socf$Score <- socf$Net.Migration + socf$Urban.Population + socf$Obesity + socf$Life.Expectancy + socf$Fertility + socf$Internet + socf$Infant.Mortality

inff$Natural.Resource.Index_x <- inff$Natural.Resource.Index_x*4
inff$Industrial.Index_x <- inff$Industrial.Index_x*2
inff$Instability.Index_x <- inff$Instability.Index_x*-2
inff$Military.Expenditures <- inff$Military.Expenditures*5
inff$Health.Expenditures <- inff$Health.Expenditures*3
inff$Education.Expenditures <- inff$Education.Expenditures*3
inff$Industrial.Growth <- inff$Industrial.Growth*4
inff$Electricity.Production <- inff$Electricity.Production*3
inff$Score <- inff$Natural.Resource.Index_x + inff$Industrial.Index_x + inff$Instability.Index_x + inff$Health.Expenditures + inff$Military.Expenditures + inff$Industrial.Growth + inff$Electricity.Production
out = data.frame(matrix(nrow=22))
out$Country.Code <- cc
out$Infrastructure <- inff$Score
out$Society <- socf$Score
out$Demographics <- demf$Score
out$Economy <- ecof$Score
out$Geography <- geof$Score
out$matrix.nrow...22. <- NULL

write.csv(out, file = "C:\\Users\\Alex\\Desktop\\scores.csv")