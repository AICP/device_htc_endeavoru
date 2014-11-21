# Copyright (C) 2013 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA commands for endeavoru"""

import common
import os
import shutil

#TARGET_DIR = os.getenv('OUT')
#UTILITIES_DIR = os.path.join(TARGET_DIR, 'utilities')

# CWM displays 28 chars.
LAYOUT_ERROR_MESSAGE = """You are running a incompatible recovery. Aborting installation!
The HTC One X storage layout was changed in Lollipop.
Install a newer recovery with Lollipop support.
Please read and understand http://goo.gl/vvy4c7 to continue."""

def FullOTA_Assertions(self):
  self.script.AssertSomeBootloader("1.28.0000", "1.31.0000", "1.33.0000",
                                   "1.36.0000", "1.39.0000", "1.72.0000",
                                   "1.73.0000")

def FullOTA_InstallBegin(self):
  # ROM uses new storage layout, check if recovery supports it too
  self.script.AppendExtra('ifelse(getprop("ro.build.endeavoru.newlayout") != "1", (')
  for line in LAYOUT_ERROR_MESSAGE.split('\n'):
    self.script.AppendExtra('ui_print("%s"); ' % line)

  self.script.AppendExtra('abort(); ) );')
