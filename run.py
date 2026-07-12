from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_command(*args: str) -> None:
	subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "manage.py"), *args], check=True)


def main() -> None:
	print("Verificando models...")
	run_command("check")

	print("Gerando migrations, se necessario...")
	run_command("makemigrations", "--noinput")

	print("Aplicando migrations...")
	run_command("migrate", "--noinput")

	print("Iniciando servidor Django...")
	run_command("runserver")


if __name__ == "__main__":
	main()
