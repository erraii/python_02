#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise Exception(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise Exception(f"{temp_int}°C is too hot for plants (max 40°C)")
    return temp_int


def test_temperature() -> None:
    test_temps = ["25", "abc", "100", "-50"]
    for temp in test_temps:
        print(f"Input data is '{temp}'")
        try:
            temp_int = input_temperature(temp)
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
        else:
            print(f"Temperature is now {temp_int}°C\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
