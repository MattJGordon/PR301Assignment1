from ChartOutputController import ChartController


class ChartInputController(object):"""Use ChartOutputController instead"""

    @staticmethod
    def make_bar_graph(title, labels, values, chart_names):
        try:
            bar_graph = ChartController(title)
            bar_graph.get_bar_graph(labels, values, chart_names)
        except (ValueError, IndexError):
            print("Incorrect arguments in bar graph")
        else:
            print("Bar Graph Made!")

    @staticmethod
    def make_pie_chart(title, labels, values):
        try:
            pie_chart = ChartController(title)
            pie_chart.get_pie_chart(labels, values)
        except (ValueError, IndexError):
            print("Incorrect arguments in pie chart")
        else:
            print("Pie Chart Made!")

    @staticmethod
    def make_scatter_graph(title, labels, values, values_two):
        try:
            scatter_graph = ChartController(title)
            scatter_graph.get_scatter_graph(labels, values, values_two)
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter graph")
        else:
            print("Scatter Graph Made!")

    @staticmethod
    def make_box_plot(title, values, values_two, chart_names):
        try:
            box_plot = ChartController(title)
            box_plot.get_box_plot(values, values_two, chart_names)
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter plot")
        else:
            print("Box Plot Made!")


bar = ChartInputController()
bar.make_bar_graph('This is a bar graph', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], ['words name', 'Numbers Names'])
"""
make_bar_graph('This is a bar graph', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], ['words name', 'Numbers Names'])
make_pie_chart('This is a pie chart', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500])
make_scatter_graph('This is a scatter graph', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
make_box_plot('This is a box plot', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])"""
