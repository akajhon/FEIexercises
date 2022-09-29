library(ggplot2)
library(dgof)
library(readr)

#Tabela completa
data <- read_delim("brazil_covid19.csv", delim = ",")
#Sem dados NA
data <- na.omit(data)
#Sem dados duplicados
data <- unique(data)
View(data)

#Define variáveis
x <- data$deaths
y <- data$refuses


#Medias
mean(x)
mean(y)

#Mediana 
median(x)
median(y)

#Variancia
var(x)
var(y)

#Desvio padrão
sd(x)
sd(y)

#Histograma
hist(x ,xlab="Values", col="blue", border="blue", main="Histograma Amostra X")
#par(mar = c(2, 2, 2, 2))

hist(y ,ylab="Values", col="blue", border="blue", main="Histograma Amostra Y")
#par(mar = c(2, 2, 2, 2))

#Box plot
#quantile(x, type = 2)
boxplot(x, main="Box-Plot X", col = ("red"))

#quantile(y, type = 2)
boxplot(y, main="Box-Plot Y", col = ("blue") )

boxplot(x,y, main="Box-Plot Comparativo X/Y", col = c("red","blue"))


#Coeficiente de correlação
cor(x,y)

qqnorm(x)
qqline(x)
hist(x, main="")
par(new=TRUE)
plot(density(x),ylab = "", xlab = "", axes=F, lwd=2.5 ) 

qqnorm(y)
qqline(y)
hist(y, main="")
par(new=TRUE)
plot(density(y),ylab = "", xlab = "", axes=F, lwd=2.5 )

#Teste de normalidade
shapiro.test(x)
results <- shapiro.test(x)

cat("Método usado: ", results$method, "\n")
cat("Estatistica: ", results$statistic, "\n")
cat("P-Valor: ", results$p.value, "\n\n")
alpha = 0.05
p <- results$p.value
if (p > alpha){
  cat('Não há diferença significativa entre x e y.')
} else{
  cat('Há diferença significativa entre x e y.')
}


shapiro.test(y)
results <- shapiro.test(y)
cat("Método usado: ", results$method, "\n")
cat("Estatistica: ", results$statistic, "\n")
cat("P-Valor: ", results$p.value, "\n\n")
alpha = 0.05
p <- results$p.value
if (p > alpha){
  cat('Não há diferença significativa entre x e y.')
} else{
  cat('Há diferença significativa entre x e y.')
}