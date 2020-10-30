import sys

from aas_editor.editorApp import EditorApp
from PyQt5 import QtWidgets
from aas.examples.data.example_aas import create_full_example

from aas_editor.models import Package
from aas_editor.settings import PREFERED_THEME
from aas_editor.util import toggleTheme


def main():
    app = QtWidgets.QApplication(sys.argv)

    obj_store = create_full_example()
    # obj_store = DictObjectStore()
    # file_store = DictSupplementaryFileContainer()
    # reader = aasx.AASXReader("/Sample_AAS/07_PhoenixContact.aasx")
    # reader.read_into(obj_store, file_store)

    window = EditorApp()
    window.packTreeViewModel.addItem(Package("/home/tehnar/Desktop/AAS_files/TestPackage.aasx"))
    toggleTheme(PREFERED_THEME)
    # window.importTestPack(obj_store)
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
