from .base import DOL


class Example_E(DOL):
    def rewrite(self, structure):
        temp_structure = []

        for char in structure:
            if char == 'F':
                temp_structure += list("FF")
            elif char == 'G':
                temp_structure += list("F[-G][+G]FG")
            else:
                temp_structure.append(char)

        return temp_structure
