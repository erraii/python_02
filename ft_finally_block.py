#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    test_plants = ["Tomato", "Lettuce", "Carrots"]
    print("\nTesting valid plants...")
    try:
        for plant in test_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
    finally:
        print("Closing watering system")
    test_plants = ["Tomato", "lettuce", "carrots"]
    print("\nTesting invalid plants...")
    try:
        for plant in test_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
