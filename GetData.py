import csv as c


def getRelation(qx: str, qy: str, file_path: str) -> tuple:
    """
    This is a function that extracts the requested data from a csv

    Args:
        qx (str): extraction of data to be used on the x axis of a plot
        qy (str): extraction of data to be used on the y axis of a plot
        file_path (str): file path to the csv
        mapx (dict): mapping string values to integers of possible question answers
                    ex: answers to questions: ["Yes", "No", "Maybe"]
                    mapx = {
                        "Yes" : 0,
                        "No" : 1,
                        "Maybe" : 2
                    }
        mapy (dict): same as mapx but for the y values
    Returns:
        tuple: (x_data, y_data)
    """
    csv = list() # list where csv file will be stored
    data = list() # where data from the csv will be stored
    x_points = list() # data points for the x axis
    y_points = list() # data points for the y axis
    
    # read csv with csv module and store lines in csv list
    with open(file_path, "r") as f:
        read_csv = c.reader(f)
        for row in read_csv:
            csv.append(row)
    
    # indices of the data to be extracted
    x_data_index = csv[0].index(qx)
    y_data_index = csv[0].index(qy)
    
    # data is everything in the csv - the first row which is the titles
    data = csv[1:]
    
    # correct order of tick mark labels --> called map because for consistency with singe variable data function
    mapx = find_map(data, x_data_index)
    mapy = find_map(data, y_data_index)
    print(mapx)
    print(mapy)
    # The code is structured in this way, as opposed to x_points = [row[x_data_index] for row in data],
    # so the x and y labels on the final plot will be placed in logical order --> (1, 2, 3, 4, 5) rather
    # than (2, 5, 3, 1, 4) if the data had been put in by which ever rows came first
    for group_x in mapx: # 'group' is the tick name --> ex. '1st Year' is a group
        for group_y in mapy:
            for row in data:
                if (row[x_data_index] == group_x and row[y_data_index] == group_y):
                    x_points.append(group_x)
                    y_points.append(group_y)
    
    return(x_points, y_points)

def getSingleData(q: str, file_path: str) -> tuple:
    """
    This is a function that finds the count of answers to 
    a single question

    Args:
        q (str): the question from the csv
        file_path (str): file path to the csv

    Returns:
        tuple: (x_points, count)
    """
    csv = list() # list where csv file will be stored
    data = list() # where data from the csv will be stored
    x_points = list() # data points for the x axis
    count = list()
    
    with open(file_path, "r") as f:
        read_csv = c.reader(f)
        for row in read_csv:
            csv.append(row)
    
    # indices of the data to be extracted
    x_data_index = csv[0].index(q)
    
    # data is everything in the csv - the first row
    data = csv[1:]
    
    # map of which index of "count" to increment
    mapx = find_map(data, x_data_index)
    
    # x_points functions as the tick marks on the graph so it = mapx
    x_points = mapx
    
    # counter for number of people who chose a given answer
    count = [0 for i in mapx]
    
    for row in data:
        # filters out blank data
        if (row[x_data_index] != ""):
            # increment count[n] for n corresponding to the participants response
            count[mapx.index(row[x_data_index])] += 1
        
    return (x_points, count)

def find_map(data: list, index: int, sorted=True) -> list:
    """
    Finds all of the distinct responses at a specific 
    x index in a 2D list

    Args:
        data (list): data from csv file (without header containing questions)
        index (int): index of question
        sorted (bool, optional): if the map should be sorted. Defaults to True.

    Returns:
        list: map
    """
    map = []
    for row in data:
        # Filters out blank entries
        if (row[index] != "" and row[index] not in map):
            map.append(row[index])
    
    # sort map if "sorted" is True --> sorts strings
    if (sorted):
        map.sort()
    return map
