from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen.io.cif import CifParser

class Cal_XRD():
    '''
    calculate XRD using .cif file

    '''

    #calculate XRD, imput path string
    def calXRD(self, path):
        d=XRDCalculator()
        parser = CifParser(path)
        structure = parser.get_structures()[0]
        diff_pattern = d.get_pattern(structure,two_theta_range=(0, 180))
        return diff_pattern



def main():
    p = "C:\\Users\\Yu\\Dropbox\\PythonProgram\\tkinker\\hexagonal.cif"
    result = Cal_XRD().calXRD(p)
    print(result.x)
    print(result.y/100)

if __name__ == '__main__': main()


