import matplotlib.pyplot as plt
import numpy as np

# Configuración del gráfico
plt.figure(figsize=(8, 6))# Determinamos la dimension de la figura 8 pulgadas de ancho x 6 pulgadas de alto
plt.title("Carta de Plasticidad", fontsize=14)
plt.xlabel("Límite Líquido, LL (%)", fontsize=12)
plt.ylabel("Índice de Plasticidad, IP (%)", fontsize=12)
plt.xlim(0, 100) # Determinamos los limites inferior y superior de X
plt.ylim(0, 60) # Determinamos los limites inferior y superior de Y
plt.xticks(np.arange(0, 101, 10))  # Mostrar valores en el eje x de 0 a 100 con intervalos de 10
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Líneas principales
LL = np.linspace(0, 100, 200)# Creamos 200 valores equidistantes entre 0 y 100
linea_A = 0.73 * (LL - 20)  # Línea A
linea_U = 0.9 * (LL - 8)    # Línea U

# Intersecciones específicas de la Línea U con IP = 4 e IP = 7
LL_IP_4 = (4 / 0.9) + 8  # LL cuando IP = 4 en Línea U, el LL sera igual a 12.44
print(LL_IP_4)
LL_IP_7 = (7 / 0.9) + 8  # LL cuando IP = 7 en Línea U, el LL sera igual a 15.7
print(LL_IP_7)

# Segmentos de la Línea U
LL_U_1 = LL[LL <= LL_IP_4 ]  # Operacion de indexacion condicional, evaluamos si cada valor LL menor a LL_IP_4, es decir LL_U_1 es un arreglo que cumple la condicion filtrada.
linea_U_1 = 0.9 * (LL_U_1 - 8)

LL_U_2 = LL[LL >= LL_IP_7]  # Segmento 2: Desde IP = 7
linea_U_2 = 0.9 * (LL_U_2 - 8)

# Ploteo de líneas
plt.plot(LL, linea_A, 'r-', label="Línea A: PI = 0.73(LL - 20)")
plt.plot(LL_U_1, linea_U_1, 'g--', label="Línea U: PI = 0.9(LL - 8)")
plt.plot(LL_U_2, linea_U_2, 'g--')
plt.axvline(x=50, color='k', linestyle='-', linewidth=1.5)  # Línea vertical en LL=50

# Cálculo de coordenadas usando las ecuaciones
interseccion_recta_LL_1= 4 / 0.73 + 20  # LL cuando IP = 4 en la Línea A
interseccion_recta_LL_2 = 7 / 0.73 + 20  # LL cuando IP = 7 en la Línea A
interseccion_recta_LL_3 = 7 / 0.9 + 8  # LL cuando IP = 7 en la linea U
interseccion_recta_LL_4 = 0.9*(50-8)  # IP cuando LL = 50 en la linea U
interseccion_recta_LL_5 = 0.73*(50-20)  # IP cuando LL = 50 en la linea A
interseccion_recta_LL_6 = 60 / 0.9 + 8   # LL cuando IP = 60 en la linea U
interseccion_recta_LL_7 = 0.73*(100-20)  # IP cuando LL = 100 en la linea A

# Coordenadas del trapecio CL - ML
x_trapecio_1 = [0, interseccion_recta_LL_1, interseccion_recta_LL_2, 0]   # coordenadas de x del trapecio
y_trapecio_1 = [4, 4, 7, 7]  # coordenadas de y del trapecio

#Cordenadas del Trapecio CL - OL
x_trapecio_2 = [interseccion_recta_LL_3, interseccion_recta_LL_2, 50, 50]  # coordenadas de x del trapecio
y_trapecio_2 = [7, 7, interseccion_recta_LL_5, interseccion_recta_LL_4]  # coordenadas de y del trapecio

#Cordenadas del poligono de 5 lados CH- OH
x_poligono_5 = [50, 50, interseccion_recta_LL_6,100, 100]  # coordenadas de x del trapecio
y_poligono_5 = [interseccion_recta_LL_5, interseccion_recta_LL_4, 60, 60, interseccion_recta_LL_7]  # coordenadas de y del trapecio

# Coordenadas del trapecio MH - OH
x_trapecio_3 = [50,50, 100, 100]  # coordenadas de x del trapecio
y_trapecio_3 = [0,interseccion_recta_LL_5, interseccion_recta_LL_7,0]  # coordenadas de y del trapecio

# Coordenadas del triangulo ML - OL
x_triangulo = [50,20, 50]  # coordenadas de x del trapecio
y_triangulo = [0,0, interseccion_recta_LL_5]  # coordenadas de y del trapecio

# La funcion "plt.fill()" se utiliza para rellenar áreas en un gráfico delimitadas por líneas, como polígonos, curvas, o áreas entre varias líneas. plt.fill(): Necesita las coordenadas completas de un área cerrada
# plt.fill_between(): Está diseñado para rellenar específicamente el área entre dos curvas o una curva y un valor constante en el eje Y.
plt.fill(x_trapecio_1, y_trapecio_1, color='blue', alpha=0.3, label="CL-ML") # Área de trapecio CL-ML 
plt.fill(x_trapecio_2 , y_trapecio_2, color='green', alpha=0.3, label="CL - OL") # Área de trapecio CL - OL 
plt.fill(x_poligono_5 , y_poligono_5, color='red', alpha=0.3, label="CH - OH")# Área de poligono de 5 lados CH - OH
plt.fill(x_trapecio_3  , y_trapecio_3, color='purple', alpha=0.3, label="CH - OH")# Área de trapecio MH - OH
plt.fill(x_triangulo  , y_triangulo, color='gray', alpha=0.3, label="CH - OH")# Área de triangulo ML - OL

# Para agregar textos o partes de un codigo al grafico usamos la funcion text()
plt.text(10, 5, "CL - ML", fontsize=12)
plt.text(38, 7, "ML - OL", fontsize=12)
plt.text(70, 20, "MH - OH", fontsize=12)
plt.text(32, 17, "CL - OL", fontsize=12)
plt.text(65, 45, "CH - OH", fontsize=12)
plt.text(55, 27, "Línea A: PI = 0.73(LL - 20)", fontsize=12, color='black', rotation=30)
plt.text(30, 22, "Línea U: PI = 0.9(LL - 8)", fontsize=12, color='black', rotation=35)

# Leyenda y visualización
plt.legend()
plt.show()
