from .base import DOL


class Example_D(DOL):
    def rewrite(self, structure):
        temp_structure = []

        for char in structure:
            if char == 'F':
                temp_structure += list("FF")
            elif char == 'G':
                temp_structure += list("F[-G]F[+G]-G")
            else:
                temp_structure.append(char)

        return temp_structure
