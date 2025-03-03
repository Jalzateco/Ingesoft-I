<template>
    <div class="estudiante-dashboard">
      <nav class="estudiante-nav">
        <h1>Panel de Estudiante</h1>
        <div class="user-info">
          <span>{{ userData.nombre }}</span>
          <button @click="logout">Cerrar Sesión</button>
        </div>
      </nav>
  
      <div class="estudiante-content">
        <div class="examenes-disponibles">
          <h2>Exámenes Disponibles</h2>
          <div class="examenes-list">
            <div v-for="examen in examenes" :key="examen.id_examen" class="examen-card">
              <h3>{{ examen.titulo }}</h3>
              <p>{{ examen.descripcion }}</p>
              <button @click="iniciarExamen(examen.id_examen)">
                Iniciar Examen
              </button>
            </div>
          </div>
        </div>
  
        <div v-if="examenActivo" class="examen-activo">
          <h2>{{ examenActual.titulo }}</h2>
          <div v-for="pregunta in preguntas" :key="pregunta.id_pregunta" class="pregunta">
            <h3>{{ pregunta.enunciado }}</h3>
            <div class="respuestas">
              <template v-if="pregunta.tipo === 'OPCION_MULTIPLE'">
                <div v-for="opcion in pregunta.opciones" :key="opcion.id" class="opcion">
                  <input 
                    type="radio" 
                    :name="'pregunta_' + pregunta.id_pregunta"
                    :value="opcion.id"
                    v-model="respuestas[pregunta.id_pregunta]"
                  >
                  <label>{{ opcion.texto }}</label>
                </div>
              </template>
              <template v-else-if="pregunta.tipo === 'VERDADERO_FALSO'">
                <div class="opcion">
                  <input 
                    type="radio" 
                    :name="'pregunta_' + pregunta.id_pregunta"
                    value="true"
                    v-model="respuestas[pregunta.id_pregunta]"
                  >
                  <label>Verdadero</label>
                </div>
                <div class="opcion">
                  <input 
                    type="radio" 
                    :name="'pregunta_' + pregunta.id_pregunta"
                    value="false"
                    v-model="respuestas[pregunta.id_pregunta]"
                  >
                  <label>Falso</label>
                </div>
              </template>
            </div>
          </div>
          <button @click="enviarRespuestas" class="enviar-btn">
            Enviar Respuestas
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/axios';
  
  export default {
    name: 'EstudianteView',
    data() {
      return {
        userData: {
          nombre: 'Estudiante'
        },
        examenes: [],
        examenActivo: false,
        examenActual: null,
        preguntas: [],
        respuestas: {}
      }
    },
    methods: {
      async cargarExamenes() {
        try {
          const response = await axios.get('/api/evaluaciones/examenes/');
          this.examenes = response.data;
        } catch (error) {
          console.error('Error cargando exámenes:', error);
        }
      },
      async iniciarExamen(examenId) {
        try {
          const response = await axios.get(`/api/evaluaciones/examenes/${examenId}/`);
          this.examenActual = response.data;
          this.preguntas = response.data.preguntas;
          this.examenActivo = true;
          this.respuestas = {};
        } catch (error) {
          console.error('Error iniciando examen:', error);
        }
      },
      async enviarRespuestas() {
        try {
          await axios.post('/api/evaluaciones/respuestas/', {
            examen_id: this.examenActual.id_examen,
            respuestas: this.respuestas
          });
          this.examenActivo = false;
          this.examenActual = null;
          this.preguntas = [];
          this.respuestas = {};
        } catch (error) {
          console.error('Error enviando respuestas:', error);
        }
      },
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('userRole');
        this.$router.push('/');
      }
    },
    created() {
      this.cargarExamenes();
    }
  }
  </script>
  
  <style scoped>
  .estudiante-dashboard {
    padding: 20px;
  }
  
  .estudiante-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f5f5f5;
  }
  
  .examenes-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  
  .examen-card {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: white;
  }
  
  .pregunta {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .respuestas {
    margin-top: 10px;
  }
  
  .opcion {
    margin: 10px 0;
  }
  
  .enviar-btn {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .enviar-btn:hover {
    background-color: #0056b3;
  }
  </style>