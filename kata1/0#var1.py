precio_pan = 3.49
descuento = 1-0.6
precio_con_descuento = precio_pan*descuento

barras_vendidas = int(input('Cuantas barras se han vendido del día: '))
print('El coste de una barra de pan es '+ str(precio_pan))
print('El descuento por no ser pan del día es del ' + str(0.6*100) +"%")
precio_final = barras_vendidas*precio_con_descuento
print ('El precio total de las ' + str(barras_vendidas) + ' barras de pan es de ' + str(precio_final) + ' euros')