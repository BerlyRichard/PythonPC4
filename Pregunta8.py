import requests
import sqlite3

# Obtener el precio del Bitcoin en diferentes monedas
url1 = "https://api.coindesk.com/v1/bpi/currentprice.json"
response1 = requests.get(url1)
data1 = response1.json()
usd_rate = float(data1['bpi']['USD']['rate'].replace(',', ''))
gbp_rate = float(data1['bpi']['GBP']['rate'].replace(',', ''))
eur_rate = float(data1['bpi']['EUR']['rate'].replace(',', ''))

# Calcular el precio en PEN usando el tipo de cambio de SUNAT
url2 = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
response2 = requests.get(url2)
data2 = response2.json()
pen_rate = usd_rate*float(data2['venta'])
fecha= data2['fecha']

# Crear la tabla 'bitcoin' en la base de datos
try:
    with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS bitcoin (
                            fecha datetime PRIMARY KEY,
                            precio_usd FLOAT,
                            precio_gbp FLOAT,
                            precio_eur FLOAT,
                            precio_pen FLOAT
                            )""")
        conexion.commit()
    print("Tabla 'bitcoin' creada correctamente.")
except sqlite3.Error as e:
    print("Error al crear la tabla:", e)


with sqlite3.connect('base.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT fecha FROM bitcoin WHERE fecha = ?", (fecha,))
    existing_date = cursor.fetchone()
    if existing_date is None:
        cursor.execute("""INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                      VALUES (?, ?, ?, ?, ?)""", (fecha, usd_rate, gbp_rate, eur_rate, pen_rate))
        conexion.commit()
        print("Datos del precio del Bitcoin insertados correctamente en la tabla 'bitcoin'.")
    else:
        print("La fecha ya existe en la tabla 'bitcoin'. No se insertaron datos.")


with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''SELECT precio_pen FROM bitcoin WHERE fecha = (SELECT MAX(fecha) FROM bitcoin)''')
        precio_pen_db = cursor.fetchone()[0]
        precio_10_bitcoins_pen = precio_pen_db * 10
        print(f"Precio de comprar 10 bitcoins en PEN: {precio_10_bitcoins_pen} PEN")
        
        cursor.execute('''SELECT precio_eur FROM bitcoin WHERE fecha = (SELECT MAX(fecha) FROM bitcoin)''')
        precio_eur_db = cursor.fetchone()[0]
        precio_10_bitcoins_eur = precio_eur_db * 10
        print(f"Precio de comprar 10 bitcoins en EUR: {precio_10_bitcoins_eur} EUR")
        pass