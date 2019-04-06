"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.sql.database_helper import import_flatfile_into_database
from pyensae.sql.database_main import Database
from pyensae.sql.database_core2 import NoHeaderException


class TestDatabaseImport (unittest.TestCase):

    def test_import_person(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        file = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data",
            "person.txt")
        dbf = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_person.db3")
        if os.path.exists(dbf):
            os.remove(dbf)
        columns = "sequence tag timestamp dateformat x y z activity".split()
        try:
            import_flatfile_into_database(
                dbf,
                file,
                fLOG=fLOG,
                columns=columns,
                header=False)
        except NoHeaderException:
            return

        assert os.path.exists(dbf)
        db = Database(dbf, LOG=fLOG)
        db.connect()
        view = db.execute_view("SELECT * FROM ACAPA")
        assert len(view) > 0
        assert len(view[0]) == 7


if __name__ == "__main__":
    unittest.main()
