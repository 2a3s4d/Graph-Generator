import matplotlib.pyplot as plt
import GetData

def genRelationPlot(plot_type, qx: str, qy: str, file_path: str, title = "", x_label = "", y_label = "", type_x = str, type_y = str, alpha=1.0) -> None:
    """
    Generates a plot which relates 2 variables

    Args:
        plot_type (function): pyplot function to be used
        qx (str): question on the x axis
        qy (str): question on the y axis
        file_path (str): file path to csv
        title (str, optional): title of the plot. Defaults to "".
        x_label (str, optional): x axis label. Defaults to "".
        y_label (str, optional): y axis label. Defaults to "".
    """
    # auto generated titles if none are specified
    if (title == ""):
        title = "%s vs %s" %(qx, qy)
        
    if (x_label == ""):
        x_label = qx
    
    if (y_label == ""):
        y_label = qy
    
    
    relation = GetData.getRelation(qx, qy, file_path, type_x=type_x, type_y=type_y)
    x_points = relation[0]
    y_points = relation[1]
    print(y_points[0:10])
    print(type(y_points[0]))
    plot_type(x_points, y_points, alpha=alpha)
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.show()

def genSingleDataPlot(plot_type, qx: str, file_path: str, title = "", x_label = "", y_label = "Number of Students") -> None:
    """
    Generates a single variable plot with the question responses on the x axis and the
    number of responses on the y axis
    Args:
        plot_type (function): pyplot function to be used 
        qx (str): question on the x axis
        file_path (str): file path to csv
        title (str, optional): title of the plot. Defaults to "".
        x_label (str, optional): x axis label. Defaults to "".
        y_label (str, optional): y axis label. Defaults to "Number of Students".
    """
    if (x_label == ""):
        x_label = qx
    
        
    data_count = GetData.getSingleData(qx, file_path)
    x_points = data_count[0]
    y_points = data_count[1]

    if (plot_type == plt.pie):
        s = sum(y_points)
        wedge_sizes = [n / s for n in y_points]
        plt.pie(wedge_sizes, labels=x_points, shadow=True, startangle=180, autopct='%1.2f%%')
        
    else:
        plot_type(x_points, y_points)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
    plt.title(title)
    plt.show()

if (__name__ == "__main__"):    
    FILEPATH = "" # String for file path to out survey results (csv format)
    X_QUESTION = "" # Question on x axis of 2 variable graph and data set for 1 variable graph
    Y_QUESTION = "" # Question on y axis of 2 variable graph --> does not matter for 1 variable graph
    TITLE = "" # Title of graph
    X_LABEL = "" # label on x axis of graph
    Y_LABEL = "" # label on y axis of graph --> does not matter for 1 variable graph (always made "Number of Students")
    # plot types
    # plt.plot (line graph)
    # plt.scatter (scatter graphs)
    # plt.bar (bar graph)
    # plt.step (step graph)
    # plt.hist2d (2d histogram)
    
    # generates a 2 variable graph 
    genRelationPlot(plt.scatter, X_QUESTION, Y_QUESTION, FILEPATH, title=TITLE, x_label=X_LABEL, y_label=Y_LABEL)
    
    # generates a 1 variable graph
    genSingleDataPlot(plt.bar, X_QUESTION, FILEPATH, x_label=X_LABEL, title=TITLE)
    
