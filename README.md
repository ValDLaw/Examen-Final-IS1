# Examen Final de Ingenieria de Software

* Estudiante: Valeria Nicole Espinoza Tarazona (202110109)

## BilleteraUtec

Para correr el sistema, asegúrese de tener instaladas las librerías del archivo `requirements.txt`. Para ello puede ejecutar en su virtualenv lo siguiente:  

```bash
pip install -r requirements.txt
```

Una vez realizado dicho paso, correr la aplicación usando:  

```bash
python3 app.py
```

## Testing

Para correr los test, ejecute el siguiente comando dentro de la carpeta del proyecto:  

```bash
python3 test.py
```

## Cambio a futuro (Pregunta 3)  

Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir por día.

> Cambios en el código (Clases / Métodos)  

Para agregar el valor máximos de transferencia de 200 soles por día, realizaría cambios en las siguientes clases:  

* `BilleteraUTEC`  

- Agregaría un atributo llamado ** limite_transferencia ** que almacene el límite diario de transferencia.
- Luego, en el método `pagar` de la clase `BilleteraUTEC`, antes de procesar la transferencia, verificaría si el valor de la transferencia (`valor`) excede el límite diario (`limite_transferencia`). Si es así, retornaría un mensaje de error indicando que se ha excedido el límite.  
- Además, necesitarías llevar un registro del monto total transferido por día. Para ello,agregaría un nuevo atributo en la clase `BilleteraUTEC` llamado `total_transferido` y un atributo `ultima_transferencia_fecha` para realizar un seguimiento de la última fecha en que se realizó una transferencia. Después, en el método `pagar`, puedes verificar si la transferencia excede el límite diario acumulado y restablecerlo si ha pasado a otro día.

Luego de dichas modificaciones, si se intenta realizar una transferencia que exceda los 200 soles, se mostrará un mensaje de error correspondiente.  

> Casos de prueba a adicionar  

Al implementar las modificaciones para agregar el límite de transferencia diario de 200 soles, incorporaría casos de prueba adicionales para verificar el comportamiento del sistema.

* Success:
   - Transferencia dentro del límite diario: Realizar una transferencia menor o igual a 200 soles. No debería mostrar errores.
   - Transferencia en días distintos: Realizar una transferencia de 200 soles en un día y luego, al día siguiente, realizar otra transferencia menor o igual a 200 soles. No debería mostrar errores.

* Fail:
   - Transferencia que excede el límite diario: Intentar realizar una transferencia mayor a 200 soles. Se debería mostrar un mensaje de error indicando que se ha excedido el límite de transferencia diario.
   - Transferencia que excede el límite diario acumulado: Realizar una transferencia de 160 soles y luego intentar realizar otra transferencia de 80 soles en el mismo día, lo que resultaría en un total de 240 soles transferidos en el mismo día. Se debería mostrar un mensaje de error indicando que se ha excedido el límite de transferencia diario.  

> Riesgos  

Algunos posibles riesgos asociados con la implementación de este cambio en el software son:  

1. Interrupción de la funcionalidad existente: Si los cambios realizados afectan áreas críticas del sistema o rompen la integración con otros componentes, existe el riesgo de interrumpir la funcionalidad existente. Esto puede resultar en errores, fallos del sistema o una experiencia deficiente para los usuarios. Por ejemplo, al agregar la validación del límite de transferencia diario, hay la posibilidad de realizar cambios en el flujo existente del endpoint `/billetera-utec/pagar`. En base a ello, aparece el riesgo de que estos cambios afecten negativamente otros aspectos del flujo, como la actualización del saldo de las cuentas involucradas o la generación de registros de transacciones.  

2. Problemas de rendimiento: Los cambios en el código o en la lógica de negocio pueden tener un impacto en el rendimiento del sistema. Si no se optimizan adecuadamente, los cambios podrían resultar en un rendimiento más lento, tiempos de respuesta más largos o un mayor consumo de recursos.  

3. Regresiones en pruebas existentes: Al realizar cambios en el sistema, existe el riesgo de introducir regresiones en pruebas que antes funcionaban correctamente. Esto puede suceder si no se prueban adecuadamente todas las rutas de ejecución del código modificado.  

Puedo concluir que la implementación de cambios siempre conlleva cierto nivel de riesgo. Sin embargo, siguiendo buenas prácticas de desarrollo y tomando las precauciones adecuadas, es posible reducir significativamente los riesgos asociados y asegurarme que la implementación de mi software se realice de manera segura y sin interrupciones graves en la funcionalidad existente.  