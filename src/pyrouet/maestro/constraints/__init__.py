"""
┌─────────────────────────────────────┐
│ Module defining measure constraints │
└─────────────────────────────────────┘

 Florian Dupeyron
 August 2020
 Revised February 2022


 Copyright (C) 2022, the Pyrouet project core team.
 
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from dataclasses           import dataclass
from ..objects.constraints import Constraint_Object

# ┌────────────────────────────────────────┐
# │ Special constraints                    │
# └────────────────────────────────────────┘

@dataclass
class Constraint_None(Constraint_Object):
    constraint_class = "none"

    def _validate(self,v):
        return True

# ┌────────────────────────────────────────┐
# │ Boolean constraints                    │
# └────────────────────────────────────────┘

from .boolean import Constraint_Boolean


# ┌────────────────────────────────────────┐
# │ Numeric constraints                    │
# └────────────────────────────────────────┘

from .numeric import (
    Constraint_Below,
    Constraint_Above,
    Constraint_Tolerance,
    Constraint_Range
)

