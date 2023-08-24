class State:
    def __init__(self):
        self.lines = []

    def append_lines(self, lines):
        if isinstance(lines, str):
            self.lines.append(lines)
        elif isinstance(lines, list):
            self.lines.extend(lines)

    def display_lines(self):
        for line in self.lines:
            print(line)

    def write_to_file(self, filename="script_out.txt"):
        with open(filename, 'w') as file:
            for line in self.lines:
                file.write(line + '\n')

# create an instance of State to hold lines
script = State()

def display_lines():
    script.display_lines()

def write_to_file(filename="script_out.txt"):
    script.write_to_file(filename)
