import requests

def bitcoin():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        dolar_precio_unitario = float(data['bpi']['USD']['rate'].replace(',', ''))  
        
        while True:
            try:
                n_bitcoins = float(input("Escriba la cantidad de bitcoins que posee: "))
                break
            except ValueError:
                print("Error, ingrese un número válido.")

        total_dolar = n_bitcoins * dolar_precio_unitario
        print(f"El costo actual de {n_bitcoins} bitcoins en USD es: ${total_dolar:,.4f}")

        # Almacenar los datos en un archivo de texto
        with open('preciobitcoin_pregunta4.txt', 'a') as file:
            file.write(f"El costo actual de {n_bitcoins:.1f} bitcoins en USD es: ${total_dolar:,.4f}\n")

        print("Los datos han sido agregados en 'preciobitcoin_pregunta4.txt'")

    except requests.RequestException as e:
        print("Error al conectar con la API:", e)
    except KeyError:
        print("No se pudo encontrar el precio de Bitcoin en la respuesta JSON.")
    except ValueError:
        print("Error de conversión de datos.")

if __name__ == "__main__":
    bitcoin()