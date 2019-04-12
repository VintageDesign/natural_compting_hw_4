from .base import DOL


class Example_B(DOL):
    def rewrite(self, structure):
        temp_structure = []

        for char in structure:
            if char == 'F':
                temp_structure += list("FF+[+F-F-F]-[-F+F+F]")
            else:
                temp_structure.append(char)

        return temp_structure
