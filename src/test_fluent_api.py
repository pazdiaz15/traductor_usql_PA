import unittest
from fluent_api import FluentQueryBuilder

class TestFluentQueryBuilder(unittest.TestCase):
    def test_select(self):
        print("Running test_select")
        builder = FluentQueryBuilder()
        query = builder.select("nombre, edad").from_table("usuarios").build()
        self.assertEqual(query, "SELECT nombre, edad FROM usuarios")

    def test_delete_where(self):
        print("Running test_delete_where")
        builder = FluentQueryBuilder()
        query = builder.delete_from("clientes").where("edad < 18").build()
        self.assertEqual(query, "DELETE FROM clientes WHERE edad < 18")

    def test_update_set_where(self):
        print("Running test_update_set_where")
        builder = FluentQueryBuilder()
        query = builder.update("empleados").set("salario = 3000").where("puesto = 'ingeniero'").build()
        self.assertEqual(query, "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'")

    def test_select_group_by_having(self):
        print("Running test_select_group_by_having")
        builder = FluentQueryBuilder()
        query = (builder.select("nombre, edad")
                      .from_table("usuarios")
                      .join("clientes", "usuarios.cliente_id = clientes.id")
                      .where("edad > 18")
                      .group_by("edad")
                      .having("COUNT(*) > 1")
                      .build())
        self.assertEqual(query, "SELECT nombre, edad FROM usuarios JOIN clientes ON usuarios.cliente_id = clientes.id WHERE edad > 18 GROUP BY edad HAVING COUNT(*) > 1")

    def test_insert_values(self):
        print("Running test_insert_values")
        builder = FluentQueryBuilder()
        query = builder.insert_into("usuarios", "nombre, edad").values("'Juan', 25").build()
        self.assertEqual(query, "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)")

    def test_alter_add_column(self):
        print("Running test_alter_add_column")
        builder = FluentQueryBuilder()
        query = builder.alter("empleados").add_column("direccion", "VARCHAR(255)", not_null=True).build()
        self.assertEqual(query, "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL")

    def test_alter_drop_column(self):
        print("Running test_alter_drop_column")
        builder = FluentQueryBuilder()
        query = builder.alter("empleados").drop_column("edad").build()
        self.assertEqual(query, "ALTER TABLE empleados DROP COLUMN edad")

    def test_select_with_join(self):
        print("Running test_select_with_join")
        builder = FluentQueryBuilder()
        query = builder.select("u.nombre, r.nombre").from_table("usuarios u").join("roles r", "u.rol_id = r.id").build()
        self.assertEqual(query, "SELECT u.nombre, r.nombre FROM usuarios u JOIN roles r ON u.rol_id = r.id")

if __name__ == "__main__":
    unittest.main()
