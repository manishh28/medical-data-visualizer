import unittest

from medical_data_visualizer import draw_cat_plot, draw_heat_map


class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        figure = draw_cat_plot()
        self.assertEqual(len(figure.axes), 2)

    def test_heat_map(self):
        figure = draw_heat_map()
        self.assertEqual(len(figure.axes), 2)


if __name__ == "__main__":
    unittest.main()
