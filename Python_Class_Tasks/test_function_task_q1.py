# test_function_task_q1.py
from function_task_q1 import (

    conversion_between_si_units,

    threshold_converter,

    send_alert_for_temperature_level,
)


class TestConversion:
    def test_celsius_to_fahrenheit(self):

        assert conversion_between_si_units("c", 100) == 212

    def test_fahrenheit_to_celsius(self):

        assert conversion_between_si_units("f", 32) == 0

    def test_uppercase_unit_still_works(self):

        assert conversion_between_si_units("C", 0) == 32

    def test_invalid_unit_defaults_to_celsius_conversion(self):

        # this is the branch that catches anything that isn't "c" or "f"
        
        assert conversion_between_si_units("x", 100) == 212


class TestThreshold:
    def test_celsius_threshold(self):

        assert threshold_converter("c", 0) == 32

    def test_fahrenheit_threshold(self):

        assert threshold_converter("f", 212) == 100


class TestAlert:
    def test_heat_alert_when_above_threshold(self):

        assert send_alert_for_temperature_level(100, 50) == "Heat alert"

    def test_cold_advisory_when_below_threshold(self):

        assert send_alert_for_temperature_level(30, 50) == "Cold Advisory"

    def test_cold_advisory_when_equal(self):
        
        assert send_alert_for_temperature_level(50, 50) == "Cold Advisory"