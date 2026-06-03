#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    test_temps = ["25", "abc"]
    for temp in test_temps:
        print(f"Input data is '{temp}'")
        try:
            temp_int = input_temperature(temp)
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
        else:
            print(f"Temperature is now {temp_int}°C\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
