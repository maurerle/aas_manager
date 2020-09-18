import sys

from aas_editor.editorApp import EditorApp
from PyQt5 import QtWidgets
from aas.examples.data.example_aas import create_full_example


def main():
    app = QtWidgets.QApplication(sys.argv)

    obj_store = create_full_example()

    window = EditorApp()
    window.importTestPack(obj_store)
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
