<template>
  <div class="container">
    <h1 class="title">BILLETERA UTEC</h1>

    <h2 class="section-title">Lista de Contactos</h2>
    <button class="btn" @click="mostrarContactos">Mostrar Contactos</button>
    <ul v-if="Object.keys(contactos).length > 0" class="contact-list">
      <li v-for="(nombre, alias) in contactos" :key="alias" class="contact-item">{{ alias }}: {{ nombre }}</li>
    </ul>
    <p v-else></p>

    <h2 class="section-title">Realizar Pago</h2>
    <form @submit.prevent="realizarPago" class="payment-form">
      <label for="minumero" class="form-label">Mi Número:</label>
      <input type="text" id="minumero" v-model="minumero" class="form-input" required>
      <label for="numerodestino" class="form-label">Número de Destino:</label>
      <input type="text" id="numerodestino" v-model="numerodestino" class="form-input" required>
      <label for="valor" class="form-label">Valor:</label>
      <input type="number" id="valor" v-model="valor" class="form-input" required>
      <button type="submit" class="btn">Realizar Pago</button>
    </form>
    <p>{{ pagoStatus }}</p>

    <h2 class="section-title">Historial de Operaciones</h2>
    <button class="btn" @click="mostrarHistorial">Mostrar Historial</button>
    <ul v-if="historial.length > 0" class="history-list">
      <li v-for="operacion in historial" :key="operacion" class="history-item">{{ operacion }}</li>
    </ul>
    <p v-else></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contactos: {},
      historial: [],
      minumero: '',
      numerodestino: '',
      valor: 0,
      pagoStatus: '',
    };
  },
  methods: {
    mostrarContactos() {
      fetch('http://127.0.0.1:5000/billetera-utec/contactos')
        .then(response => response.json())
        .then(data => {
          this.contactos = data;
        })
        .catch(error => {
          console.error('Error al obtener los contactos:', error);
        });
    },
    realizarPago() {
      const requestBody = {
        minumero: this.minumero,
        numerodestino: this.numerodestino,
        valor: this.valor,
      };

      fetch('http://127.0.0.1:5000/billetera-utec/pagar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      })
        .then(response => response.text())
        .then(data => {
          this.pagoStatus = data;
        })
        .catch(error => {
          console.error('Error al realizar el pago:', error);
        });
    },
    mostrarHistorial() {
      fetch('http://127.0.0.1:5000/billetera-utec/historial')
        .then(response => response.json())
        .then(data => {
          this.historial = data.operaciones;
        })
        .catch(error => {
          console.error('Error al obtener el historial:', error);
        });
    },
  },
};
</script>

<style>
.container {
  margin: 0 auto;
  padding: 20px;
  height: auto;
  background-color: #47c3f0;
}

.title {
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 60px;
  color: #333;
  margin-bottom: 20px;
}

.section-title {
  font-size: 24px;
  color: #555;
  text-align: center;
  justify-content: center;
  margin-bottom: 10px;
}

.btn {
  text-align: center;
  margin-left: 640px;
  justify-content: center;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #45a049;
}

.form-label {
  display: block;
  text-align: center;
  margin-bottom: 5px;
  font-size: 16px;
  color: #333;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  font-size: 16px;
}

.contact-list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 10px;
}

.contact-item {
  margin-bottom: 5px;
  font-size: 16px;
}

.history-list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 10px;
}

.history-item {
  margin-bottom: 5px;
  font-size: 16px;
}

/* Animaciones */
@keyframes fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

.fade-in {
  animation: fade-in 1s;
}

@keyframes slide-up {
  0% { transform: translateY(100%); }
  100% { transform: translateY(0); }
}

.slide-up {
  animation: slide-up 0.5s;
}
</style>