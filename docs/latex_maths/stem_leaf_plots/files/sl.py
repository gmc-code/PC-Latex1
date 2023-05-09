#import the module
import stemgraphic

#define a sample data set
data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]

#create a stem and leaf plot
fig, ax = stemgraphic.stem_graphic(data)

#show the plot
fig.show()