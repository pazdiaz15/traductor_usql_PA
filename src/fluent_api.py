class FluentQueryBuilder:
    def __init__(self):
        self.select_clause = ""
        self.from_clause = ""
        self.join_clause = ""
        self.where_clause = ""
        self.group_by_clause = ""
        self.having_clause = ""
        self.insert_clause = ""
        self.values_clause = ""
        self.update_clause = ""
        self.set_clause = ""
        self.delete_clause = ""
        self.alter_clause = ""

    # Métodos para construir la consulta
    def select(self, columns):
        self.select_clause = f"SELECT {columns}"
        return self

    def from_table(self, table):
        self.from_clause = f"FROM {table}"
        return self

    def join(self, table, condition):
        self.join_clause = f"JOIN {table} ON {condition}"
        return self

    def where(self, condition):
        self.where_clause = f"WHERE {condition}"
        return self

    def group_by(self, column):
        self.group_by_clause = f"GROUP BY {column}"
        return self

    def having(self, condition):
        self.having_clause = f"HAVING {condition}"
        return self

    def insert_into(self, table, columns):
        self.insert_clause = f"INSERT INTO {table} ({columns})"
        return self

    def values(self, values):
        self.values_clause = f"VALUES ({values})"
        return self

    def update(self, table):
        self.update_clause = f"UPDATE {table}"
        return self

    def set(self, assignments):
        self.set_clause = f"SET {assignments}"
        return self

    def delete_from(self, table):
        self.delete_clause = f"DELETE FROM {table}"
        return self

    def alter(self, table):
        self.alter_clause = f"ALTER TABLE {table}"
        return self

    def add_column(self, column, data_type, not_null=False):
        not_null_str = " NOT NULL" if not_null else ""
        self.alter_clause += f" ADD COLUMN {column} {data_type}{not_null_str}"
        return self

    def drop_column(self, column):
        self.alter_clause += f" DROP COLUMN {column}"
        return self


    def build(self):
        parts = [
            self.insert_clause,
            self.select_clause,
            self.from_clause,
            self.join_clause,
            self.update_clause,
            self.set_clause,
            self.delete_clause,
            self.where_clause,
            self.group_by_clause,
            self.having_clause,
            self.values_clause,
            self.alter_clause
        ]
        return " ".join(part for part in parts if part)