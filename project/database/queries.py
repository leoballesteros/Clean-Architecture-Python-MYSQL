CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE
)
"""

INSERT_USUARIO = """
INSERT INTO usuarios (nome, email)
VALUES (%s, %s)
"""

SELECT_ALL = "SELECT id, nome, email FROM usuarios"

SELECT_BY_ID = "SELECT id, nome, email FROM usuarios WHERE id = %s"

UPDATE_USUARIO = """
UPDATE usuarios
SET nome = %s, email = %s
WHERE id = %s
"""

DELETE_USUARIO = "DELETE FROM usuarios WHERE id = %s"