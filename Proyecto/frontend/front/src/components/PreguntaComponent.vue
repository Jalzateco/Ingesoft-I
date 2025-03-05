<template>
    <div class="pregunta-component">
      <h2>Gestión de Preguntas</h2>
      <div class="pregunta-form" v-if="isDocente || isAdmin">
        <input v-model="nuevaPregunta.enunciado" placeholder="Enunciado de la pregunta" />
        <select v-model="nuevaPregunta.tipo">
          <option value="OPCION_MULTIPLE">Opción Múltiple</option>
          <option value="VERDADERO_FALSO">Verdadero/Falso</option>
        </select>
        <button @click="crearPregunta">Crear Pregunta</button>
      </div>
      <div class="preguntas-list">
        <div v-for="pregunta in preguntas" :key="pregunta.id_pregunta" class="pregunta-item">
          <h3>{{ pregunta.enunciado }}</h3>
          <p>Tipo: {{ pregunta.tipo }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/axios';
  
  export default {
    name: 'PreguntaComponent',
    data() {
      return {
        preguntas: [],
        nuevaPregunta: {
          enunciado: '',
          tipo: 'OPCION_MULTIPLE'
        },
        isDocente: false,
        isAdmin: false
      }
    },
    methods: {
      async obtenerPreguntas() {
        try {
          const response = await axios.get('/api/evaluaciones/preguntas/');
          this.preguntas = response.data;
        } catch (error) {
          console.error('Error al obtener preguntas:', error);
        }
      },
      async crearPregunta() {
        try {
          await axios.post('/api/evaluaciones/preguntas/', this.nuevaPregunta);
          this.obtenerPreguntas();
          this.nuevaPregunta = { enunciado: '', tipo: 'OPCION_MULTIPLE' };
        } catch (error) {
          console.error('Error al crear pregunta:', error);
        }
      }
    },
    created() {
      this.obtenerPreguntas();
    }
  }
  </script>