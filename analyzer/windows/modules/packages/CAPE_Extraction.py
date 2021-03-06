# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import shutil

from lib.common.abstracts import Package

class CAPE_Extraction(Package):
    """CAPE Extraction analysis package."""
    #PATHS = [
    #    ("SystemRoot", "system32"),
    #]

    def __init__(self, options={}, config=None):
        """@param options: options dict."""
        self.config = config
        self.options = options
        self.pids = []
        self.options["dll"] = "CAPE_Extraction.dll"

    def start(self, path):
        self.options["dll"] = "CAPE_Extraction.dll"
        arguments = self.options.get("arguments")
        
        return self.debug(path, arguments, path)
