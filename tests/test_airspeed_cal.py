import numpy as np
from hypothesis import given
from hypothesis import strategies as st

from app.performance.calcs import Flaps, airspeed_calibration

# Define the strategy for generating test cases
kias_strategy = st.floats(min_value=40, max_value=170)
flaps_strategy = st.sampled_from(Flaps)


@given(kias=kias_strategy, flaps=flaps_strategy)
def test_airspeed_calibration(kias, flaps):
    result = airspeed_calibration(kias, flaps)

    # Get the correct set of indicated_speeds and calibrated_speeds
    # for the given flap setting
    if flaps == Flaps.FLAPS_FULL:
        indicated_speeds = [40, 50, 60, 70, 80, 90, 95]
        calibrated_speeds = [51, 56, 64, 72, 81, 91, 95]
    elif flaps == Flaps.FLAPS_20:
        indicated_speeds = [40, 50, 60, 70, 80, 90, 100, 110, 120]
        calibrated_speeds = [53, 58, 64, 72, 81, 91, 100, 110, 119]
    else:  # Flaps == Flaps.FLAPS_UP
        indicated_speeds = [55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
        calibrated_speeds = [62, 65, 73, 82, 90, 100, 109, 118, 127, 137, 146, 156]

    # Perform interpolation using numpy
    expected_kcas = float(np.interp(kias, indicated_speeds, calibrated_speeds))

    assert result == expected_kcas
