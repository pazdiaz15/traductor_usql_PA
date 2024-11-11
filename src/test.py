import unittest
from traductor import parser

class TestUSQLParser(unittest.TestCase):
    
    def test_select_todo(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18"
        result = parser.parse(query)
        expected_sql = "SELECT * FROM usuarios WHERE edad > 18"
        self.assertEqual(result, expected_sql)

    def test_select_distinct(self):
        query = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid'"
        result = parser.parse(query)
        expected_sql = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid'"
        self.assertEqual(result, expected_sql)

    def test_insert(self):
        query = "METE EN usuarios (nombre, edad) VALORES ('Juan', 25)"
        result = parser.parse(query)
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"
        self.assertEqual(result, expected_sql)

    def test_update(self):
        query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'"
        result = parser.parse(query)
        expected_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"
        self.assertEqual(result, expected_sql)

    def test_delete(self):
        query = "BORRA DE clientes DONDE edad ENTRE 18 Y 25"
        result = parser.parse(query)
        expected_sql = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25"
        self.assertEqual(result, expected_sql)

    def test_alter_add_column(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO"
        result = parser.parse(query)
        expected_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL"
        self.assertEqual(result, expected_sql)

    def test_alter_drop_column(self):
        query = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion"
        result = parser.parse(query)
        expected_sql = "ALTER TABLE empleados DROP COLUMN direccion"
        self.assertEqual(result, expected_sql)

    # Tests de error de sintaxis
    def test_invalid_syntax_missing_table(self):
        query = "TRAEME TODO DONDE edad > 18" 
        with self.assertRaises(SyntaxError):
            parser.parse(query)

    def test_invalid_syntax_unknown_keyword(self):
        query = "TRAEME TODO DE LA TABLA usuarios PARECIDO edad > 18"  
        with self.assertRaises(SyntaxError):
            parser.parse(query)

    def test_invalid_condition_syntax(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE edad PARECIDO 18"
        with self.assertRaises(SyntaxError):
            parser.parse(query)

    def test_invalid_alter_missing_column_name(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA VARCHAR(255) NO NULO"  
        with self.assertRaises(SyntaxError):
            parser.parse(query)

    def test_insert_missing_values(self):
        query = "METE EN usuarios (nombre, edad) VALORES ()"  
        with self.assertRaises(SyntaxError):
            parser.parse(query)

    def test_update_missing_set_clause(self):
        query = "ACTUALIZA empleados DONDE puesto = 'ingeniero'" 
        with self.assertRaises(SyntaxError):
            parser.parse(query)

if __name__ == '__main__':
    unittest.main()
