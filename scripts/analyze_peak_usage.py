from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
CLIENTS_FILE = ROOT_DIR / "data" / "demo" / "rookie_filtered_clients.json"


def load_demo_clients() -> pd.DataFrame:
    """
    Carga los registros sintéticos de clientes utilizados por la demo pública.

    Cada fila representa una observación de un cliente asociada a un AP
    en una fecha y hora determinadas.
    """
    if not CLIENTS_FILE.exists():
        raise FileNotFoundError(
            f"No se ha encontrado el dataset de demostración: {CLIENTS_FILE}"
        )

    df = pd.read_json(CLIENTS_FILE)

    required_columns = {
        "date",
        "hour",
        "associated_device_name",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Faltan columnas obligatorias en el dataset de demostración: "
            + ", ".join(sorted(missing_columns))
        )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["hour"] = pd.to_numeric(df["hour"], errors="coerce")

    df = df.dropna(
        subset=[
            "date",
            "hour",
            "associated_device_name",
        ]
    ).copy()

    df["hour"] = df["hour"].astype(int)

    return df


def compute_usage_by_time(df: pd.DataFrame):
    """
    Calcula la actividad de la demo agrupando los registros por fecha y hora.

    IMPORTANTE:
    Los datos públicos son sintéticos, por lo que estas cifras sirven
    únicamente para demostrar el funcionamiento del análisis.
    """
    by_datetime = (
        df.groupby(["date", "hour"])
        .size()
        .reset_index(name="client_records")
        .sort_values(
            ["client_records", "date", "hour"],
            ascending=[False, True, True],
        )
    )

    by_hour = (
        df.groupby("hour")
        .size()
        .sort_values(ascending=False)
        .rename("client_records")
    )

    return by_datetime, by_hour


def compute_usage_by_ap(df: pd.DataFrame) -> pd.Series:
    """
    Calcula qué AP ficticio concentra más registros en la demo.
    """
    return (
        df.groupby("associated_device_name")
        .size()
        .sort_values(ascending=False)
        .rename("client_records")
    )


def main() -> None:
    df = load_demo_clients()

    if df.empty:
        print("El dataset de demostración no contiene registros válidos.")
        return

    by_datetime, by_hour = compute_usage_by_time(df)
    by_ap = compute_usage_by_ap(df)

    print("=== ANÁLISIS DE ACTIVIDAD — DEMO SINTÉTICA ===")
    print()
    print(f"Registros cargados: {len(df)}")
    print(
        "Periodo: "
        f"{df['date'].min().date()} -> {df['date'].max().date()}"
    )

    print("\n>>> ACTIVIDAD POR HORA")
    print(by_hour)

    print("\n>>> FRANJAS CON MAYOR ACTIVIDAD")
    print(by_datetime.head(10).to_string(index=False))

    print("\n>>> ACTIVIDAD POR AP FICTICIO")
    print(by_ap)

    peak = by_datetime.iloc[0]

    print("\n>>> RESUMEN")
    print(
        f"Mayor actividad de la demo: "
        f"{int(peak['client_records'])} registros "
        f"el {peak['date'].date()} a las {int(peak['hour']):02d}:00."
    )

    print(
        "\nNota: este análisis utiliza exclusivamente datos sintéticos "
        "de demostración y no representa la infraestructura real de la UAB."
    )


if __name__ == "__main__":
    main()