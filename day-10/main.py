import re

def main():
    with open("input.txt", "r") as file:
        data = file.read()
    
    lines = data.splitlines()

    for line in lines:
        instructions = {
            "lights": "",
            "buttons": [],
            "joltages": ""
        }

        match = re.search(r"\[(.*)\] (.*) \{(.*)\}", line)

        lights = match.group(1).replace(".", "0").replace("#", "1")

        raw_buttons = match.group(2).split()
        buttons = []
        for button in raw_buttons:
            button = button.strip("(").strip(")").split(",")
            buttons.append(button)

        bin_buttons = []
        for button in buttons:
            switches = []
            for i in range(len(lights)):
                if str(i) in button:
                    switches.append("1")
                else:
                    switches.append("0")
            bin_buttons.append("".join(switches))
                    

                
        


        instructions["lights"] = lights
        instructions["buttons"] = bin_buttons
        instructions["joltages"] = match.group(3)

        print(instructions)


if __name__ == "__main__":
    main()