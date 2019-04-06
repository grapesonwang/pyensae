"""
@brief      test log(time=1s)
"""
import os
import unittest
from PIL import Image
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyensae.graphhelper import draw_diagram


class TestBlockDiag(unittest.TestCase):

    def test_draw_diagram_png(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace("            ", "")
        img = draw_diagram(code, format="png")
        temp = get_temp_folder(__file__, "temp_draw_diagram_png")
        name = os.path.join(temp, "image.png")
        with open(name, "wb") as f:
            f.write(img)

    def test_draw_diagram_pillow(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace("            ", "")
        img = draw_diagram(code, format="pillow")
        self.assertTrue(img, Image)
        self.assertEqual(img.size, (832, 200))

    def test_draw_diagram_svg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace("            ", "")
        img = draw_diagram(code, format="svg")
        self.assertTrue(img, str)
        self.assertTrue(
            '<rect fill="rgb(0,0,0)" height="40" stroke="rgb(0,0,0)"' in img)


if __name__ == "__main__":
    unittest.main()
