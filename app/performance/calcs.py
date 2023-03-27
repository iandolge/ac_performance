from enum import Enum

import numpy as np


class Flaps(Enum):
    FLAPS_UP = 0
    FLAPS_20 = 1
    FLAPS_FULL = 2


def airspeed_calibration(kias: float, flaps: Flaps) -> float:
    """Calculate KCAS given KIAS and flap angle"""
    if flaps == Flaps.FLAPS_FULL:
        indicated_speeds = [40, 50, 60, 70, 80, 90, 95]
        calibrated_speeds = [51, 56, 64, 72, 81, 91, 95]
    elif flaps == Flaps.FLAPS_20:
        indicated_speeds = [40, 50, 60, 70, 80, 90, 100, 110, 120]
        calibrated_speeds = [53, 58, 64, 72, 81, 91, 100, 110, 119]
    else:  # Flaps == Flaps.FLAPS_UP
        indicated_speeds = [55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
        calibrated_speeds = [62, 65, 73, 82, 90, 100, 109, 118, 127, 137, 146, 156]
    return float(np.interp(kias, indicated_speeds, calibrated_speeds))
