import os
from pathlib import Path
import sys

poetry_python_lib = Path(Path.home(), ".poetry", "lib")
sys.path.append(os.path.realpath(poetry_python_lib))

from poetry.core.masonry.builders.sdist import SdistBuilder
from poetry.factory import Factory

current_path = Path(__file__).parent

factory = Factory()
poetry = factory.create_poetry(current_path)

sdist_builder = SdistBuilder(poetry, None, None)
setuppy_blob = sdist_builder.build_setup()

with open(Path(current_path, "setup.py"), "wb") as unit:
    unit.write(setuppy_blob)
    unit.write(b"\n# This setup.py was autogenerated using poetry.\n")
