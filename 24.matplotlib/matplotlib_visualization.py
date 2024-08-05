"""
    Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
    Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias

        Color Reference
        'r'	Red	
        'g'	Green	
        'b'	Blue	
        'c'	Cyan	
        'm'	Magenta	
        'y'	Yellow	
        'k'	Black	
        'w'	White

        Line Reference
        '-'	    Solid line	
        ':'	    Dotted line	
        '--'	Dashed line	
        '-.'	Dashed/dotted line

        Marker Reference
        'o'	Circle	
        '*'	Star	
        '.'	Point	
        ','	Pixel	
        'x'	X	
        'X'	X (filled)	
        '+'	Plus	
        'P'	Plus (filled)	
        's'	Square	
        'D'	Diamond	
        'd'	Diamond (thin)	
        'p'	Pentagon	
        'H'	Hexagon	
        'h'	Hexagon	
        'v'	Triangle Down	
        '^'	Triangle Up	
        '<'	Triangle Left	
        '>'	Triangle Right	
        '1'	Tri Down	
        '2'	Tri Up	
        '3'	Tri Left	
        '4'	Tri Right	
        '|'	Vline	
        '_'	Hline	    
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(f"matplotlib version: {matplotlib.__version__}")

# Draw a line in a diagram from position (0,0) to position (6,250)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, "o")
plt.show()

############################################################
# plotting - Multiple Points
############################################################
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

############################################################
# Markers
############################################################
# use the keyword argument marker to emphasize each point with a specified marker
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker="*")
plt.show()


# Format Strings fmt marker|line|color
# shortcut string notation parameter to specify the marker.
plt.plot(ypoints, "o:r")
plt.show()

# use the keyword argument markersize or the shorter version, ms to set the size of the markers
# use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers
# use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers
# it can use Hexadecimal color values in mec and mfc
plt.plot(ypoints, marker="o", ms=20, mec="g", mfc="#4CAF50")
plt.show()


############################################################
# Linestyle
############################################################
# use the keyword argument linestyle, or shorter ls, to change the style of the plotted line
# use the keyword argument color or the shorter c to set the color of the line
# use the keyword argument linewidth or the shorter lw to change the width of the line
plt.plot(ypoints, linestyle="dotted", color="r", linewidth="20.5")
# shortcut
# plt.plot(ypoints, ls=":")
plt.show()

# plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()


############################################################
# Labels and Title
############################################################
# use the fontdict parameter in xlabel(), ylabel(), and title()
# to set font properties for the title and labels
# use the loc parameter in title() to position the title,
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}

plt.title("Sports Watch Data", fontdict=font1, loc="left")
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.plot(x1, y1, x2, y2)
plt.show()

############################################################
# Grid Lines
############################################################
plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.plot(x1, y1, x2, y2)
# use the grid() function to add grid lines to the plot
# plt.grid()
# Display only grid lines for the x-axis
# plt.grid(axis="x")
# Display only grid lines for the x-axis
# plt.grid(axis="y")
plt.grid(color="green", linestyle="--", linewidth="0.5")
plt.show()

############################################################
# Subplot - Display Multiple Plots
############################################################
# subplot() function can draw multiple plots in one figure
# it takes three arguments that describes the layout of the figure
# The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.
# plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(1, 2, 1)
# Draw 2 plots on top of each other:
# plt.subplot(2, 1, 1)
plt.plot(x, y)
# add a title to each plot with the title() function
plt.title("SALSE")

# plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

# the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(1, 2, 2)
# Draw 2 plots on top of each other:
# plt.subplot(2, 1, 2)
plt.plot(x, y)
# add a title to each plot with the title() function
plt.title("INCOME")

# add a title to the entire figure with the suptitle() function
plt.suptitle("MY SHOP")
plt.show()

############################################################
# Scatter
############################################################
# Use scatter() function plots one dot for each observation.
# It needs two arrays of the same length (X and y - axis)

# day one, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# set a specific color for each dot by using an array of colors as value for the c argument
colors = np.array(
    [
        "red",
        "green",
        "blue",
        "yellow",
        "pink",
        "black",
        "orange",
        "purple",
        "beige",
        "brown",
        "gray",
        "cyan",
        "magenta",
    ]
)
# plt.scatter(x, y, color="hotpink")
# change the size of the dots with the s argument.
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
# adjust the transparency of the dots with the alpha argument.
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# day two, the age and speed of 15 cars:
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
# plt.scatter(x, y, color="#88c999")
# colormap is called 'viridis' and # it ranges from 0,
# which is a purple color, up to 100, which is a yellow color.
color_map = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 75, 80, 90, 95, 100])
plt.scatter(x, y, c=color_map, cmap="viridis")

plt.colorbar()
plt.show()


############################################################
# Bars
############################################################
# use the bar() function to draw bar graphs
# default width and height value is 0.8
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
# vertical bar
# plt.bar(x, y, width=0.1)

# horizontal bar
plt.barh(x, y, color="red", height=0.1)
plt.show()

############################################################
# Histograms
############################################################
# A histogram is a graph showing frequency distributions.
# use the hist() function to create histograms.
# use NumPy to randomly generate an array with 250 values,
# where the values will concentrate around 170, and the standard deviation is 10.
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

############################################################
# Pie Charts
############################################################
# use the pie() function to draw pie charts
# pie chart draws one piece (called a wedge)
# By default the plotting of the first wedge
# starts from the x-axis and moves counterclockwise
# The size of each wedge is determined by comparing
# the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)
y = np.array([35, 25, 25, 15])
# labels parameter must be an array with one label for each wedge
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# explode parameter allow one of the wedges to stand out
myexplode = [0.2, 0, 0, 0]
# set the color of each wedge
mycolors = ["black", "hotpink", "b", "#4CAF50"]
# change the start angle by specifying a startangle parameter, default angle is 0
plt.pie(
    y, labels=mylabels, startangle=90, explode=myexplode, shadow=True, colors=mycolors
)

# use the legend() function to add a list of explanation
plt.legend(title="Four Fruits: ", loc="lower right")
plt.show()
