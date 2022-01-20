import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCajaCristal(unittest.TestCase):
    
    def test_mayor_de_edad(self):
        
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    

    def test_menor_de_edad(self):
        
        edad = 17

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()