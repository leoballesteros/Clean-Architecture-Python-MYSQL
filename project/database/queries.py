CREATE_TABLE_USUARIOS = """
CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""".strip()

INSERT_USUARIO = "INSERT INTO usuarios (nome, email) VALUES (%s, %s);"
SELECT_USUARIO_BY_ID = "SELECT id, nome, email FROM usuarios WHERE id = %s;"
SELECT_USUARIO_BY_EMAIL = "SELECT id, nome, email FROM usuarios WHERE email = %s;"
SELECT_USUARIOS = "SELECT id, nome, email FROM usuarios ORDER BY id;"
UPDATE_USUARIO = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s;"
DELETE_USUARIO = "DELETE FROM usuarios WHERE id = %s;"

