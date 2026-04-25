from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import mysql.connector
from mysql.connector import MySQLConnection

from project.config.settings import Settings


@contextmanager
def get_connection(settings: Settings) -> Iterator[MySQLConnection]:
    connection = mysql.connector.connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
    )
    try:
        yield connection
    finally:
        connection.close()

