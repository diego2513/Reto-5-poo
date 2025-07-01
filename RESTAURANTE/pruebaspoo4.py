from momento_pagar import mompay
from orden import Order, fanta,agua,vino,arepas_queso,carne_asada,perro_caliente,palitos_queso,ensalada,bandeja_paisa,helado,brownie,galleta

#Para mostrar el Menu al usuario
def show_menu():
    print("+--------------------- MENÚ ---------------------+")
    print("|                   🥤 BEBIDAS                   |")
    print("|------------------------------------------------|")
    print(f"| Fanta          | ${fanta.price} | {fanta.type_bebida}                  |")
    print(f"| Agua           | ${agua.price} | {agua.type_bebida}                  |")
    print(f"| Vino           | ${vino.price} | {vino.type_bebida}              |")
    
    print("+------------------------------------------------+")
    print("|                🍽️ APERITIVOS                    |")
    print("|------------------------------------------------|")
    print(f"| Arepa con queso | ${arepas_queso.price} | {arepas_queso.type_aperitivo} |")
    print(f"| Palitos de queso| ${palitos_queso.price} | {palitos_queso.type_aperitivo} |")
    print(f"| Ensalada        | ${ensalada.price} | {ensalada.type_aperitivo}  |")

    print("+------------------------------------------------+")
    print("|            🍛 PLATOS PRINCIPALES               |")
    print("|------------------------------------------------|")
    print(f"| Perro caliente | ${perro_caliente.price} | {perro_caliente.type_principio} |")
    print(f"| Bandeja paisa  | ${bandeja_paisa.price} | {bandeja_paisa.type_principio}  |")
    print(f"| Carne de Res   | ${carne_asada.price} | {carne_asada.type_principio} |")

    print("+------------------------------------------------+")
    print("|                🍰 POSTRES                      |")
    print("|------------------------------------------------|")
    print(f"| Helado de fresa | ${helado.price} | {helado.type_dessert} |")
    print(f"| Brownie         | ${brownie.price} | {brownie.type_dessert} |")
    print(f"| Galleta         | ${galleta.price} | {galleta.type_dessert} |")

    print("+------------------------------------------------+")

#Para mostrar despedida
def goodbye():
    print("+------------------------------------------------+")
    print("|    🙌 GRACIAS POR VISITAR EL RESTAURANTE 🙌    |")
    print("+------------------------------------------------+")

show_menu()  


O = Order()

M = mompay(0)

O.add()

O.show_final_order()

O.final_price()

#momento del pago
M.payment_mom()

goodbye()