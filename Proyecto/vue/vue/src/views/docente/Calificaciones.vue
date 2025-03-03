<template>
    <div class="calificaciones-container">
      <h1>Gestión de Calificaciones</h1>
      
      <div class="curso-selector">
        <label for="curso">Seleccionar Curso:</label>
        <select id="curso" v-model="cursoSeleccionado" @change="cargarEstudiantes">
          <option value="">Seleccione un curso</option>
          <option v-for="curso in cursos" :key="curso.id" :value="curso.id">
            {{ curso.nombre }} ({{ curso.codigo }})
          </option>
        </select>
      </div>
      
      <div v-if="cursoSeleccionado && estudiantes.length > 0" class="calificaciones-content">
        <div class="actividades-section">
          <h2>Actividades de Evaluación</h2>
          <button class="btn-add" @click="agregarActividad">
            Agregar Actividad
          </button>
          
          <div v-if="showActividadForm" class="actividad-form">
            <h3>{{ editandoActividad ? 'Editar' : 'Nueva' }} Actividad</h3>
            <div class="form-group">
              <label for="actividadNombre">Nombre:</label>
              <input type="text" id="actividadNombre" v-model="nuevaActividad.nombre" placeholder="Nombre de la actividad">
            </div>
            <div class="form-group">
              <label for="actividadPorcentaje">Porcentaje (%):</label>
              <input type="number" id="actividadPorcentaje" v-model="nuevaActividad.porcentaje" min="1" max="100">
            </div>
            <div class="form-group">
              <label for="actividadFecha">Fecha:</label>
              <input type="date" id="actividadFecha" v-model="nuevaActividad.fecha">
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelarActividad">Cancelar</button>
              <button class="btn-save" @click="guardarActividad">Guardar</button>
            </div>
          </div>
          
          <div class="actividades-list">
            <div v-for="actividad in actividades" :key="actividad.id" class="actividad-item">
              <div class="actividad-info">
                <h3>{{ actividad.nombre }}</h3>
                <p><strong>Porcentaje:</strong> {{ actividad.porcentaje }}%</p>
                <p><strong>Fecha:</strong> {{ formatDate(actividad.fecha) }}</p>
              </div>
              <div class="actividad-actions">
                <button class="btn-edit" @click="editarActividad(actividad)">Editar</button>
                <button class="btn-delete" @click="eliminarActividad(actividad.id)">Eliminar</button>
              </div>
            </div>
          </div>
        </div>
        
        <div class="calificaciones-table">
          <h2>Registro de Calificaciones</h2>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Estudiante</th>
                  <th v-for="actividad in actividades" :key="actividad.id">
                    {{ actividad.nombre }} ({{ actividad.porcentaje }}%)
                  </th>
                  <th>Nota Final</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="estudiante in estudiantes" :key="estudiante.id">
                  <td>{{ estudiante.nombre }}</td>
                  <td v-for="actividad in actividades" :key="actividad.id">
                    <input 
                      type="number" 
                      min="0" 
                      max="5" 
                      step="0.1" 
                      v-model="calificaciones[estudiante.id][actividad.id]"
                      @change="calcularNotaFinal(estudiante.id)"
                    >
                  </td>
                  <td class="nota-final">
                    {{ calcularNotaFinal(estudiante.id).toFixed(1) }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="save-actions">
            <button class="btn-save-all" @click="guardarCalificaciones">Guardar Calificaciones</button>
          </div>
        </div>
      </div>
      
      <div v-else-if="cursoSeleccionado && estudiantes.length === 0" class="no-students">
        No hay estudiantes registrados en este curso.
      </div>
      
      <div v-else class="select-curso-msg">
        Por favor seleccione un curso para gestionar las calificaciones.
      </div>
    </div>
  </template>
  
  <script>
  import { ref, reactive, computed } from 'vue'
  
  export default {
    name: 'DocenteCalificacionesView',
    setup() {
      const cursos = ref([
        { id: 1, nombre: 'Programación Avanzada', codigo: 'PROG2023' },
        { id: 2, nombre: 'Bases de Datos', codigo: 'BD2023' },
        { id: 3, nombre: 'Ingeniería de Software', codigo: 'IS2023' }
      ])
      
      const estudiantes = ref([])
      const actividades = ref([])
      const calificaciones = reactive({})
      const cursoSeleccionado = ref('')
      
      const showActividadForm = ref(false)
      const editandoActividad = ref(false)
      const nuevaActividad = ref({
        id: null,
        nombre: '',
        porcentaje: 10,
        fecha: ''
      })
      
      // Cargar estudiantes al seleccionar un curso
      const cargarEstudiantes = () => {
        if (!cursoSeleccionado.value) {
          estudiantes.value = []
          actividades.value = []
          return
        }
        
        // Simulación de carga de datos
        estudiantes.value = [
          { id: 1, nombre: 'Juan Pérez' },
          { id: 2, nombre: 'María López' },
          { id: 3, nombre: 'Carlos Rodríguez' },
          { id: 4, nombre: 'Ana Martínez' },
          { id: 5, nombre: 'Pedro Sánchez' }
        ]
        
        actividades.value = [
          { id: 1, nombre: 'Parcial 1', porcentaje: 25, fecha: '2024-03-15' },
          { id: 2, nombre: 'Taller Práctico', porcentaje: 15, fecha: '2024-04-10' },
          { id: 3, nombre: 'Parcial 2', porcentaje: 30, fecha: '2024-05-20' },
          { id: 4, nombre: 'Proyecto Final', porcentaje: 30, fecha: '2024-06-12' }
        ]
        
        // Inicializar calificaciones
        estudiantes.value.forEach(estudiante => {
          calificaciones[estudiante.id] = {}
          actividades.value.forEach(actividad => {
            calificaciones[estudiante.id][actividad.id] = (Math.random() * 4 + 1).toFixed(1)
          })
        })
      }
      
      // Formato de fecha
      const formatDate = (dateString) => {
        const date = new Date(dateString)
        return date.toLocaleDateString()
      }
      
      // Gestión de actividades
      const agregarActividad = () => {
        nuevaActividad.value = {
          id: null,
          nombre: '',
          porcentaje: 10,
          fecha: ''
        }
        editandoActividad.value = false
        showActividadForm.value = true
      }
      
      const editarActividad = (actividad) => {
        nuevaActividad.value = { ...actividad }
        editandoActividad.value = true
        showActividadForm.value = true
      }
      
      const guardarActividad = () => {
        if (!nuevaActividad.value.nombre || !nuevaActividad.value.fecha) {
          alert('Por favor complete todos los campos')
          return
        }
        
        if (editandoActividad.value) {
          const index = actividades.value.findIndex(a => a.id === nuevaActividad.value.id)
          if (index !== -1) {
            actividades.value[index] = { ...nuevaActividad.value }
          }
        } else {
          const newId = Math.max(0, ...actividades.value.map(a => a.id)) + 1
          actividades.value.push({
            ...nuevaActividad.value,
            id: newId
          })
          
          // Inicializar calificaciones para la nueva actividad
          estudiantes.value.forEach(estudiante => {
            calificaciones[estudiante.id][newId] = 0
          })
        }
        
        showActividadForm.value = false
      }
      
      const cancelarActividad = () => {
        showActividadForm.value = false
      }
      
      const eliminarActividad = (id) => {
        if (confirm('¿Está seguro que desea eliminar esta actividad?')) {
          actividades.value = actividades.value.filter(a => a.id !== id)
          
          // Limpiar calificaciones de esta actividad
          estudiantes.value.forEach(estudiante => {
            delete calificaciones[estudiante.id][id]
          })
        }
      }
      
      // Calcular nota final
      const calcularNotaFinal = (estudianteId) => {
        let notaFinal = 0
        let porcentajeTotal = 0
        
        actividades.value.forEach(actividad => {
          const nota = parseFloat(calificaciones[estudianteId][actividad.id] || 0)
          const porcentaje = actividad.porcentaje / 100
          
          notaFinal += nota * porcentaje
          porcentajeTotal += porcentaje
        })
        
        // Normalizar en caso de que los porcentajes no sumen 100%
        if (porcentajeTotal > 0) {
          notaFinal = notaFinal / porcentajeTotal * (porcentajeTotal < 1 ? 1 : porcentajeTotal)
        }
        
        return notaFinal
      }
      
      // Guardar todas las calificaciones
      const guardarCalificaciones = () => {
        // Aquí se implementaría la lógica para enviar los datos al servidor
        alert('Las calificaciones han sido guardadas correctamente.')
        
        // Simulación de guardado (en un caso real, se enviaría al backend)
        const datosParaGuardar = {
          cursoId: cursoSeleccionado.value,
          calificaciones: { ...calificaciones },
          actividades: [...actividades.value]
        }
        
        console.log('Datos guardados:', datosParaGuardar)
      }
      
      // Verificar porcentaje total
      const porcentajeTotal = computed(() => {
        return actividades.value.reduce((total, actividad) => total + parseInt(actividad.porcentaje), 0)
      })
      
      return {
        cursos,
        estudiantes,
        actividades,
        calificaciones,
        cursoSeleccionado,
        showActividadForm,
        editandoActividad,
        nuevaActividad,
        porcentajeTotal,
        cargarEstudiantes,
        formatDate,
        agregarActividad,
        editarActividad,
        guardarActividad,
        cancelarActividad,
        eliminarActividad,
        calcularNotaFinal,
        guardarCalificaciones
      }
    }
  }
  </script>
  
  <style scoped>
  .calificaciones-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1 {
    color: #2c3e50;
    margin-bottom: 30px;
    text-align: center;
  }
  
  h2 {
    color: #3498db;
    margin-bottom: 20px;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
  }
  
  .curso-selector {
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .curso-selector select {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    width: 300px;
    font-size: 1rem;
  }
  
  .actividades-section {
    margin-bottom: 30px;
  }
  
  .btn-add {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    margin-bottom: 20px;
  }
  
  .actividad-form {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  .form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
  }
  
  .btn-save, .btn-save-all {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .btn-cancel {
    background-color: #95a5a6;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .btn-edit {
    background-color: #f39c12;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
  }
  
  .btn-delete {
    background-color: #e74c3c;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
  }
  
  .actividades-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
  }
  
  .actividad-item {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  
  .actividad-info h3 {
    margin-top: 0;
    color: #2c3e50;
  }
  
  .actividad-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 15px;
  }
  
  .calificaciones-table {
    overflow-x: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: center;
  }
  
  th {
    background-color: #f2f2f2;
    font-weight: bold;
  }
  
  input[type="number"] {
    width: 60px;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    text-align: center;
  }
  
  .nota-final {
    font-weight: bold;
    background-color: #f8f9fa;
  }
  
  .save-actions {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }
  
  .btn-save-all {
    padding: 10px 25px;
    font-size: 1rem;
    background-color: #2980b9;
  }
  
  .no-students, .select-curso-msg {
    text-align: center;
    padding: 50px 0;
    color: #7f8c8d;
    font-size: 1.2rem;
    background-color: #f9f9f9;
    border-radius: 8px;
    margin-top: 20px;
  }
  </style>