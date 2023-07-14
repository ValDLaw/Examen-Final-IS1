from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos

class BilleteraUTEC:
    def __init__(self):
        self.cuentas = []
        self.agregar_cuentas_iniciales()

    def agregar_cuentas_iniciales(self):
        # Agregar cuentas iniciales de estudiantes de UTEC
        self.cuentas.append(Cuenta("20210001", "Juan Perez", 200, ["20210002", "20210003"]))
        self.cuentas.append(Cuenta("20210002", "Maria Lopez", 400, ["20210003"]))
        self.cuentas.append(Cuenta("20210003", "Carlos Ramirez", 300, ["20210001"]))

    def obtener_cuenta(self, numero):
        # Obtener una cuenta en base a su número
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta
        return None

    def obtener_contactos(self, numero):
        # Obtener los contactos de una cuenta
        cuenta = self.obtener_cuenta(numero)
        if cuenta:
            return cuenta.contactos
        else:
            return []

    def pagar(self, numero, numero_destino, valor):
        # Realizar un pago entre dos cuentas
        cuenta = self.obtener_cuenta(numero)
        cuenta_destino = self.obtener_cuenta(numero_destino)

        if cuenta and cuenta_destino:
            if cuenta.saldo >= valor:
                cuenta.saldo -= valor
                cuenta_destino.saldo += valor
                return True
            else:
                return False
        else:
            return False

    def obtener_historial(self, numero):
        # Obtener el saldo y el historial de operaciones de una cuenta
        cuenta = self.obtener_cuenta(numero)
        if cuenta:
            print("Operaciones de ", cuenta.nombre)
            saldo = cuenta.saldo
            operaciones = []
            for cuenta_destino in self.cuentas:
                if cuenta_destino.numero in cuenta.contactos:
                    operaciones.append(f"Pago recibido de {cuenta_destino.saldo} de {cuenta_destino.nombre}")
            operaciones.append(f"2 de {len(cuenta.contactos) + 1}")
            return saldo, operaciones
        else:
            return None, None

billetera_utec = BilleteraUTEC()

@app.route('/billetera-utec/contactos')
def mostrar_contactos():
    numero = request.args.get('minumero')
    contactos = billetera_utec.obtener_contactos(numero)
    if contactos:
        return jsonify(contactos=contactos)
    else:
        return jsonify(error='No se encontró la cuenta.'), 404

@app.route('/billetera-utec/pagar')
def pagar():
    numero = request.args.get('minumero')
    numero_destino = request.args.get('numerodestino')
    valor = int(request.args.get('valor'))

    if billetera_utec.pagar(numero, numero_destino, valor):
        return 'Realizado en {date}.'.format(date=date.today().strftime("%d/%m/%Y"))
    else:
        return jsonify(error='No se pudo realizar el pago.'), 400

@app.route('/billetera-utec/historial')
def mostrar_historial():
    numero = request.args.get('minumero')
    saldo, operaciones = billetera_utec.obtener_historial(numero)

    if saldo is not None and operaciones is not None:
        return jsonify(saldo=saldo, operaciones=operaciones)
    else:
        return jsonify(error='No se encontró la cuenta.'), 404

if __name__ == '__main__':
    app.run()