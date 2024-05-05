import time
import pyautogui
import tempfile
import Autotypo as ps

# Global variable to control the execution of auto_type_with_indentation
stop_pasting = False

def auto_type(text, delay=0.03):
    for char in text:
        pyautogui.press(char)
        time.sleep(delay)


def auto_type_with_indentation(text, indent=4):
    global stop_pasting  # Access the global variable
    lines = text.split("\n")
    time.sleep(5)
    for line in lines:
        auto_type(line)
        pyautogui.press("enter")
        time.sleep(0.03)
        # Ensure cursor moves to the beginning of the next line
        pyautogui.press("home")
        # Check the stop flag after each line is typed
        if stop_pasting:
            break  # Exit the function if the stop flag is set to True


# Create a temporary file to store the code
temp_file = tempfile.NamedTemporaryFile(delete=False)

# Write the code from the text area to the temporary file
with open(temp_file.name, "w") as f:
    f.write(ps.code_paste)

# Type the code with indentation
auto_type_with_indentation(ps.code_paste)

# Close the temporary file
temp_file.close()
