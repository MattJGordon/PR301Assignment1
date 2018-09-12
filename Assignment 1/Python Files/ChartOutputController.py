from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot


class ChartController(object):

    def get_bar_graph(self, title, labels, values, chart_names):
        try:
            bar_graph = BarGraph(title, labels, values, chart_names)
            bar_graph.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in bar graph")
            return False
        else:
            print("Bar Graph Made!")
            return True

    def get_pie_chart(self, title, labels, values):
        try:
            pie_chart = PieChart(title, labels, values)
            pie_chart.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in pie chart")
            return False
        else:
            print("Pie Chart Made!")
            return True

    def get_scatter_graph(self, title, labels, values, values_two):
        try:
            scatter_graph = ScatterGraph(title, labels, values, values_two)
            scatter_graph.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter graph")
            return False
        else:
            print("Scatter Graph Made!")
            return True

    def get_box_plot(self, title, values, values_two, chart_names):
        try:
            box_plot = BoxPlot(title, values, values_two, chart_names)
            box_plot.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter plot")
            return False
        else:
            print("Box Plot Made!")
            return True


bar = ChartController()
bar.get_bar_graph('This is a bar graph', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], ['words name', 'Numbers Names'])