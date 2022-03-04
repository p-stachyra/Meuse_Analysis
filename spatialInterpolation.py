import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


from shapely.geometry import Point


def readData(path, coordinates1, coordinates2):
    df = pd.read_csv(path)
    # creating a geometry column
    geometry = []
    for x, y in zip(df[coordinates1], df[coordinates2]):
        geometry.append(Point(x,y))

    # Creating a Geographic data frame
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    return gdf

def plotData(geodataframe, output_name, column_name=None, n_intervals=5):
    if column_name:
        geodataframe.plot(column=column_name, cmap="RdYlBu", scheme="natural_breaks", k=n_intervals, legend=True, figsize=(13, 10))
    else:
        geodataframe.plot(figsize=(13, 10))
    plt.savefig(output_name)
    plt.show()
    return 0

data = readData("meuse.csv", "x", "y")
plotData(data, "Zinc_intervals.PNG", column_name="zinc", n_intervals=5)

river_data = readData("meuse_river.csv", "V1", "V2")
plotData(river_data, "river_plot.PNG")