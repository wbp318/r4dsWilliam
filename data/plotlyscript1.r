# Install the plotly package if you haven't already
install.packages("plotly")

# Load the plotly package
library(plotly)

# Create your ggplot object
p <- ggplot(brand_summary, aes(x = factor(brand), y = total_items)) +
  geom_bar(stat = "identity") +
  labs(title = "Total Items Sold by Brand", x = "Brand", y = "Total Items")

# Convert the ggplot object to an interactive plotly object
ggplotly(p)