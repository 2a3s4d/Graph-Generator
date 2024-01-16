# Graph-Generator
This is a graph generator that can create different types of plots such as, bar graphs, line graphs, scatter plots, pie charts and step graphs.
Uses csv files and an input up to two data types you want to generate a plot of.

![Graph Generation example](https://github.com/2a3s4d/Graph-Generator/assets/84204533/314f88c4-e084-4bad-ace0-e4ef6d898867)
Here is an example of a line graph created using the following input
genRelationPlot(plt.plot, "No. ", "Time ", "Data/csTimerExport_20230309_120701.csv", title="Cubing Session From 2021", x_label="Solve #", y_label="Time", type_x=int, type_y=float)
