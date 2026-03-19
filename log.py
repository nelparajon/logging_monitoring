import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Inicio del script")

    try:
        logging.info("Ejecutando proceso")

        resultado = 10 / 0

    except ZeroDivisionError as e:
        logging.error(f"Error: {e}")

    logging.info("Fin del script")

if __name__ == "__main__":
    main()