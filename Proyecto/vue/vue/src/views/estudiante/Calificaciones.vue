<template>
    <div class="calificaciones-container">
      <div class="page-header">
        <h1>Mis Calificaciones</h1>
        <div class="curso-info" v-if="curso">
          <h2>{{ curso.nombre }}</h2>
          <div class="curso-details">
            <p><strong>Código:</strong> {{ curso.codigo }}</p>
            <p><strong>Profesor:</strong> {{ curso.profesor }}</p>
          </div>
        </div>
      </div>
      
      <div v-if="loading" class="loading">
        <p>Cargando calificaciones...</p>
      </div>
      
      <div v-else-if="curso" class="calificaciones-content">
        <div class="calificaciones-summary">
          <div class="nota-final-container">
            <div class="nota-final" :class="notaFinalClase">
              {{ calcularNotaFinal() }}
            </div>
            <p class="nota-label">Calificación Final</p>
            <p class="estado" :class="estadoClase">{{ estadoCurso }}</p>
          </div>
          
          <div class="progress-container">
            <h3>Progreso del curso</h3>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: calcularProgresoTotal() + '%' }"></div>
            </div>
            <p>{{ calcularProgresoTotal() }}% completado</p>
          </div>
        </div>
        
        <div class="actividades-list">
          <h3>Actividades Evaluativas</h3>
          <div class="actividad-item" v-for="actividad in actividades" :key="actividad.id">
            <div class="actividad-header">
              <h4>{{ actividad.nombre }}</h4>
              <span class="actividad-fecha">{{ formatDate(actividad.fecha) }}</span>
            </div>
            <div class="actividad-data">
              <div class="actividad-porcentaje">
                <span class="label">Porcentaje</span>
                <span class="value">{{ actividad.porcentaje }}%</span>
              </div>
              <div class="actividad-nota" :class="getNotaClass(actividad.nota)">
                <span class="label">Calificación</span>
                <span class="value">{{ actividad.nota === null ? 'Pendiente' : actividad.nota }}</span>
              </div>
            </div>
            <div class="actividad-comentarios" v-if="actividad.comentarios">
              <p><strong>Comentarios:</strong> {{ actividad.comentarios }}</p>
            </div>
          </div>
        </div>
        
        <div class="no-actividades" v-if="actividades.length === 0">
          <p>No hay actividades evaluativas registradas para este curso</p>
        </div>
      </div>
      
      <div v-else class="no-curso">
        <p>El curso solicitado no existe o no estás inscrito en él</p>
        <router-link to="/estudiante/cursos" class="btn-back">
          Volver a Mis Cursos
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  
  export default {
    name: 'EstudianteCalificacionesView',
    setup() {
      const route = useRoute()
      const loading = ref(true)
      const cursoId = route.params.id
      
      const curso = ref(null)
      const actividades = ref([])
      
      // Cargar datos del curso y calificaciones
      onMounted(() => {
        // Simulación de carga de datos - En producción, esto se obtendría de una API
        setTimeout(() => {
          // Datos de ejemplo
          const cursos = [
            {
              id: 1,
              nombre: 'Programación Avanzada',
              codigo: 'PROG2023',
              profesor: 'Dr. Juan Rodríguez'
            },
            {
              id: 2,
              nombre: 'Bases de Datos',
              codigo: 'BD2023',
              profesor: 'Dra. María López'
            },
            {
              id: 3,
              nombre: 'Ingeniería de Software',
              codigo: 'IS2023',
              profesor: 'Dr. Carlos Martínez'
            }
          ]
          
          // Buscar el curso por ID
          curso.value = cursos.find(c => c.id === parseInt(cursoId))
          
          if (curso.value) {
            // Cargar actividades del curso
            actividades.value = [
              {
                id: 1,
                nombre: 'Parcial 1',
                fecha: '2024-03-15',
                porcentaje: 25,
                nota: 4.2,
                comentarios: 'Buen trabajo, pero podría mejorar en la implementación de algoritmos'
              },
              {
                id: 2,
                nombre: 'Taller Práctico',
                fecha: '2024-04-10',
                porcentaje: 15,
                nota: 3.8,
                comentarios: null
              },
              {
                id: 3,
                nombre: 'Parcial 2',
                fecha: '2024-05-20',
                porcentaje: 30,
                nota: null,
                comentarios: null
              },
              {
                id: 4,
                nombre: 'Proyecto Final',
                fecha: '2024-06-12',
                porcentaje: 30,
                nota: null,
                comentarios: null
              }
            ]
          }
          
          loading.value = false
        }, 800)
      })
      
      // Formatear fecha
      const formatDate = (dateString) => {
        const date = new Date(dateString)
        return date.toLocaleDateString()
      }
      
      // Calcular nota final
      const calcularNotaFinal = () => {
        if (!actividades.value.length) return '0.0'
        
        let notaAcumulada = 0
        let porcentajeAcumulado = 0
        
        actividades.value.forEach(act => {
          if (act.nota !== null) {
            notaAcumulada += act.nota * (act.porcentaje / 100)
            porcentajeAcumulado += act.porcentaje
          }
        })
        
        // Si no hay ninguna nota registrada
        if (porcentajeAcumulado === 0) return '0.0'
        
        // Calcular nota proyectada
        const notaFinal = notaAcumulada * (100 / porcentajeAcumulado)
        return notaFinal.toFixed(1)
      }
      
      // Determinar clase CSS según la nota
      const notaFinalClase = computed(() => {
        const nota = parseFloat(calcularNotaFinal())
        if (nota >= 4.0) return 'excelente'
        if (nota >= 3.0) return 'aprobado'
        return 'reprobado'
      })
      
      // Determinar estado del curso
      const estadoCurso = computed(() => {
        const nota = parseFloat(calcularNotaFinal())
        if (nota >= 4.0) return 'Excelente'
        if (nota >= 3.0) return 'Aprobado'
        return 'En riesgo'
      })
      
      // Clase CSS para el estado
      const estadoClase = computed(() => {
        return notaFinalClase.value
      })
      
      // Calcular progreso del curso
      const calcularProgresoTotal = () => {
        if (!actividades.value.length) return 0
        
        let porcentajeEvaluado = 0
        
        actividades.value.forEach(act => {
          if (act.nota !== null) {
            porcentajeEvaluado += act.porcentaje
          }
        })
        
        return Math.min(100, porcentajeEvaluado)
      }
      
      // Determinar clase CSS para cada nota
      const getNotaClass = (nota) => {
        if (nota === null) return ''
        if (nota >= 4.0) return 'excelente'
        if (nota >= 3.0) return 'aprobado'
        return 'reprobado'
      }
      
      return {
        loading,
        curso,
        actividades,
        formatDate,
        calcularNotaFinal,
        notaFinalClase,
        estadoCurso,
        estadoClase,
        calcularProgresoTotal,
        getNotaClass
      }
    }
  }
  </script>
  
  <style scoped>
  .calificaciones-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .page-header {
    margin-bottom: 30px;
  }
  
  h1 {
    color: #2c3e50;
    margin-bottom: 10px;
    text-align: center;
  }
  
  .curso-info {
    background-color: #f8f9fa;
    border-radius: 8px;
    padding: 15px;
    margin-top: 20px;
    text-align: center;
  }
  
  .curso-info h2 {
    margin: 0 0 10px 0;
    color: #3498db;
  }
  
  .curso-details {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  .loading, .no-curso {
    text-align: center;
    padding: 50px 0;
    color: #7f8c8d;
    font-size: 1.2rem;
  }
  
  .calificaciones-summary {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-bottom: 40px;
    justify-content: space-around;
  }
  
  .nota-final-container {
    text-align: center;
  }
  
  .nota-final {
    font-size: 4.5rem;
    font-weight: bold;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    color: white;
  }
  
  .nota-final.excelente {
    background-color: #27ae60;
  }
  
  .nota-final.aprobado {
    background-color: #f39c12;
  }
  
  .nota-final.reprobado {
    background-color: #e74c3c;
  }
  
  .nota-label {
    margin-top: 10px;
    font-size: 1.2rem;
    color: #7f8c8d;
  }
  
  .estado {
    display: inline-block;
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: bold;
    margin-top: 10px;
    color: white;
  }
  
  .estado.excelente {
    background-color: #27ae60;
  }
  
  .estado.aprobado {
    background-color: #f39c12;
  }
  
  .estado.reprobado {
    background-color: #e74c3c;
  }
  
  .progress-container {
    max-width: 500px;
    width: 100%;
  }
  
  .progress-container h3 {
    margin-bottom: 15px;
    color: #34495e;
  }
  
  .progress-bar {
    height: 25px;
    background-color: #ecf0f1;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 10px;
  }
  
  .progress-fill {
    height: 100%;
    background-color: #3498db;
    transition: width 0.3s ease;
  }
  
  .actividades-list {
    margin-top: 40px;
  }
  
  .actividades-list h3 {
    margin-bottom: 20px;
    color: #34495e;
    border-bottom: 1px solid #ecf0f1;
    padding-bottom: 10px;
  }
  
  .actividad-item {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .actividad-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  
  .actividad-header h4 {
    margin: 0;
    color: #2c3e50;
    font-size: 1.2rem;
  }
  
  .actividad-fecha {
    color: #7f8c8d;
    font-size: 0.9rem;
  }
  
  .actividad-data {
    display: flex;
    gap: 20px;
    margin-bottom: 15px;
  }
  
  .actividad-porcentaje, .actividad-nota {
    display: flex;
    flex-direction: column;
    background-color: #f8f9fa;
    padding: 10px 15px;
    border-radius: 5px;
    min-width: 100px;
  }
  
  .label {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 5px;
  }
  
  .value {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
  }
  
  .actividad-nota.excelente .value {
    color: #27ae60;
  }
  
  .actividad-nota.aprobado .value {
    color: #f39c12;
  }
  
  .actividad-nota.reprobado .value {
    color: #e74c3c;
  }
  
  .actividad-comentarios {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #ecf0f1;
  }
  
  .actividad-comentarios p {
    margin: 0;
    color: #7f8c8d;
  }
  
  .no-actividades {
    text-align: center;
    padding: 30px 0;
    color: #7f8c8d;
    background-color: #f8f9fa;
    border-radius: 8px;
  }
  
  .btn-back {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 20px;
  }
  
  @media (max-width: 768px) {
    .curso-details {
      flex-direction: column;
      gap: 5px;
    }
    
    .actividad-data {
      flex-direction: column;
      gap: 10px;
    }
  }
  </style>