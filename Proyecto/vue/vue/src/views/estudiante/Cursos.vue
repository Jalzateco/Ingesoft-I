<template>
    <div class="cursos-container">
      <h1>Mis Cursos</h1>
      
      <div class="search-filter">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Buscar cursos..." 
          class="search-input"
        />
      </div>
      
      <div class="cursos-grid">
        <div 
          v-for="curso in filteredCursos" 
          :key="curso.id" 
          class="curso-card"
        >
          <div class="curso-header" :style="{ backgroundColor: curso.color }">
            <h2>{{ curso.nombre }}</h2>
            <span class="curso-codigo">{{ curso.codigo }}</span>
          </div>
          <div class="curso-content">
            <p><strong>Profesor:</strong> {{ curso.profesor }}</p>
            <p><strong>Horario:</strong> {{ curso.horario }}</p>
            <p><strong>Salón:</strong> {{ curso.salon }}</p>
          </div>
          <div class="curso-footer">
            <router-link :to="`/estudiante/calificaciones/${curso.id}`" class="btn-calificaciones">
              Ver Calificaciones
            </router-link>
          </div>
        </div>
      </div>
      
      <div v-if="filteredCursos.length === 0" class="no-cursos">
        <p v-if="searchQuery">No se encontraron cursos que coincidan con "{{ searchQuery }}"</p>
        <p v-else>No tienes cursos asignados</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue'
  
  export default {
    name: 'EstudianteCursosView',
    setup() {
      const searchQuery = ref('')
      
      // Datos de ejemplo - En producción, estos vendrían de una API
      const cursos = ref([
        {
          id: 1,
          nombre: 'Programación Avanzada',
          codigo: 'PROG2023',
          profesor: 'Dr. Juan Rodríguez',
          horario: 'Lunes y Miércoles 10:00 - 12:00',
          salon: 'Edificio A - Salón 101',
          color: '#3498db'
        },
        {
          id: 2,
          nombre: 'Bases de Datos',
          codigo: 'BD2023',
          profesor: 'Dra. María López',
          horario: 'Martes y Jueves 14:00 - 16:00',
          salon: 'Edificio B - Salón 205',
          color: '#2ecc71'
        },
        {
          id: 3,
          nombre: 'Ingeniería de Software',
          codigo: 'IS2023',
          profesor: 'Dr. Carlos Martínez',
          horario: 'Viernes 08:00 - 12:00',
          salon: 'Edificio C - Salón 310',
          color: '#e74c3c'
        },
        {
          id: 4,
          nombre: 'Algoritmos y Estructuras de Datos',
          codigo: 'AED2023',
          profesor: 'Dr. Pedro González',
          horario: 'Lunes y Miércoles 16:00 - 18:00',
          salon: 'Edificio A - Salón 205',
          color: '#9b59b6'
        }
      ])
      
      const filteredCursos = computed(() => {
        if (!searchQuery.value) return cursos.value
        
        const query = searchQuery.value.toLowerCase()
        return cursos.value.filter(curso => 
          curso.nombre.toLowerCase().includes(query) ||
          curso.codigo.toLowerCase().includes(query) ||
          curso.profesor.toLowerCase().includes(query)
        )
      })
      
      return {
        searchQuery,
        cursos,
        filteredCursos
      }
    }
  }
  </script>
  
  <style scoped>
  .cursos-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1 {
    color: #2c3e50;
    margin-bottom: 30px;
    text-align: center;
  }
  
  .search-filter {
    margin-bottom: 30px;
    display: flex;
    justify-content: center;
  }
  
  .search-input {
    width: 80%;
    max-width: 500px;
    padding: 12px 20px;
    border: 1px solid #ddd;
    border-radius: 50px;
    font-size: 1rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .cursos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
  }
  
  .curso-card {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .curso-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
  }
  
  .curso-header {
    padding: 20px;
    color: white;
  }
  
  .curso-header h2 {
    margin: 0 0 10px 0;
    font-size: 1.5rem;
  }
  
  .curso-codigo {
    font-size: 0.9rem;
    opacity: 0.8;
  }
  
  .curso-content {
    padding: 20px;
  }
  
  .curso-content p {
    margin: 10px 0;
  }
  
  .curso-footer {
    padding: 15px 20px;
    background-color: #f8f9fa;
    text-align: center;
  }
  
  .btn-calificaciones {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }
  
  .btn-calificaciones:hover {
    background-color: #2980b9;
  }
  
  .no-cursos {
    text-align: center;
    padding: 40px 0;
    color: #7f8c8d;
    font-size: 1.2rem;
  }
  
  @media (max-width: 768px) {
    .cursos-grid {
      grid-template-columns: 1fr;
    }
  }
  </style>