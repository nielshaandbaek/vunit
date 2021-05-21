# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com

"""
VHDL User Guide
---------------

The most minimal VUnit VHDL project covering the basics of the
:ref:`User Guide <user_guide>`.
"""

from pathlib import Path
from vunit import VUnit

VU = VUnit.from_argv()
VU.add_library("lib").add_source_files(Path(__file__).parent / "*.vhd")
VU.main()
