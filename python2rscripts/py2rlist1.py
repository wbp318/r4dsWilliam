# Install rpy2 using pip
!pip install rpy2

# Use rpy2 to run R code in Python
import rpy2.robjects as robjects

# Run R code
robjects.r('x <- c(1, 2, 3, 4, 5)')
robjects.r('print(mean(x))')

# Pass data between Python and R
r_vector = robjects.FloatVector([1, 2, 3, 4, 5])
print(r_vector)
