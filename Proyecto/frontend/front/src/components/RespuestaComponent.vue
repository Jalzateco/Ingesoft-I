<template>
    <div class="respuesta-component">
      <h2>Respuestas</h2>
      <div class="respuesta-form" v-if="isEstudiante">
        <select v-model="nuevaRespuesta.pregunta">
          <option v-for="pregunta in preguntas" :key="pregunta.id_pregunta" :value="pregunta.id_pregunta">
            {{ pregunta.enunciado }}
          </option>
        </select>
        <input v-model="nuevaRespuesta.contenido" placeholder="Tu respuesta" />
        <button @click="enviarRespuesta">Enviar Respuesta</button>
      </div>
      <div class="respuestas-list">
        <div v-for="respuesta in respuestas" :key="respuesta.id_respuesta" class="respuesta-item">
          <p>{{ respuesta.contenido }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/axios';
  
  export default {
    name: 'RespuestaComponent',
    data() {
      return {
        respuestas: [],
        preguntas: [],
        nuevaRespuesta: {
          pregunta: null,
          contenido: ''
        },
        isEstudiante: false
      }
    },
    methods: {
      async obtenerRespuestas() {
        try {
          const response = await axios.get('/api/evaluaciones/respuestas/');
          this.respuestas = response.data;
        } catch (error) {
          console.error('Error al obtener respuestas:', error);
        }
      },
      async obtenerPreguntas() {
        try {
          const response = await axios.get('/api/evaluaciones/preguntas/');
          this.preguntas = response.data;
        } catch (error) {
          console.error('Error al obtener preguntas:', error);
        }
      },
      async enviarRespuesta() {
        try {
          await axios.post('/api/evaluaciones/respuestas/', this.nuevaRespuesta);
          this.obtenerRespuestas();
          this.nuevaRespuesta = { pregunta: null, contenido: '' };
        } catch (error) {
          console.error('Error al enviar respuesta:', error);
        }
      }
    },
    created() {
      this.obtenerRespuestas();
      this.obtenerPreguntas();
    }
  }
  </script>