library(ggplot2)

data <- read.csv(file = "MLA.entropy.list", sep = "\t")

## All MLA family members
ggplot(data[data$Type == "all", ]) +
    geom_line(mapping = aes(x = Position, y = Entropy)) +
    geom_hline(yintercept = (1.5/log2(20)), col = "red") + 
    ylim(0.8, 0)

#Sr33
ggplot(data[data$Type == "Sr33", ]) +
  geom_line(mapping = aes(x = Position, y = Entropy)) +
  geom_hline(yintercept = (1.5/log2(20)), col = "red") + 
  ylim(0.8, 0)


#Sr50
ggplot(data[data$Type == "Sr50", ]) +
  geom_line(mapping = aes(x = Position, y = Entropy)) +
  geom_hline(yintercept = (1.5/log2(20)), col = "red") + 
  ylim(0.8, 0)

#MLA
ggplot(data[data$Type == "MLA", ]) +
  geom_line(mapping = aes(x = Position, y = Entropy)) +
  geom_hline(yintercept = (1.5/log2(20)), col = "red") + 
  ylim(0.8, 0)

#HcMLA
ggplot(data[data$Type == "HcMLA", ]) +
  geom_line(mapping = aes(x = Position, y = Entropy)) +
  geom_hline(yintercept = (1.5/log2(20)), col = "red") + 
  ylim(0.8, 0)