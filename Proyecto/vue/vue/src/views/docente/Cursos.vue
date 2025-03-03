<template>
    <div class="cursos-docente">
      <h1>Mis Cursos</h1>
      
      <div class="filters">
        <div class="search-bar">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Buscar por nombre o código..." 
            @input="filterCursos"
          />
        </div>
        <div class="filter-by">
          <select v-model="filterPeriodo" @change="filterCursos">
            <option value="">Todos los períodos</option>
            <option value="2024-1">2024-1</option>
            <option value="2024-2">2024-2</option>
          </select>
        </div>
      </div>
      
      <div class="cursos-list">
        <div v-if="filteredCursos.length === 0" class="no-courses">
          No se encontraron cursos que coincidan con tu búsqueda.
        </div>
        
        <div v-for="curso in filteredCursos" :key="curso.id" class="curso-card">
          <div class="curso-header">
            <h3>{{ curso.nombre }}</h3>
            <span class="curso-codigo">{{ curso.codigo }}</span>
          </div>
          <div class="curso-info">
            <p><strong>Período:</strong> {{ curso.periodo }}</p>
            <p><strong>Horario:</strong> {{ curso.horario }}</p>
            <p><strong>Aula:</strong> {{ curso.aula }}</p>
            <p><strong>Estudiantes:</strong> {{ curso.estudiantes }}</p>
          </div>
          <div class="curso-actions">
            <button class="btn-primary">Ver detalles</button>
            <button class="btn-secondary">Calificaciones</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, computed } from 'vue'
  
  export default {
    name: 'DocenteCursosView',
    setup() {
      const cursos = ref([])
      const filteredCursos = ref([])
      const searchQuery = ref('')
      const filterPeriodo = ref('')
      
      // Simulación de datos
      onMounted(() => {
        // Aquí normalmente se haría una llamada a la API
        cursos.value = [
          {
            id: 1,
            nombre: 'Programación Avanzada',
            codigo: 'PROG2023',
            periodo: '2024-1',
            horario: 'Lunes y Miércoles 10:00 - 12:00',
            aula: 'B-201',
            estudiantes: 25
          },
          {
            id: 2,
            nombre: 'Bases de Datos',
            codigo: 'BD2023',
            periodo: '2024-1',
            horario: 'Martes y Jueves 08:00 - 10:00',
            aula: 'A-101',
            estudiantes: 30
          },
          {
            id: 3,
            nombre: 'Ingeniería de Software',
            codigo: 'IS2023',
            periodo: '2024-2',
            horario: 'Viernes 14:00 - 18:00',
            aula: 'C-305',
            estudiantes: 20
          }
        ]
        
        filteredCursos.value = [...cursos.value]
      })
      
      const filterCursos = () => {
        filteredCursos.value = cursos.value.filter(curso => {
          const matchesSearch = curso.nombre.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
                              curso.codigo.toLowerCase().includes(searchQuery.value.toLowerCase())
          
          const matchesPeriodo = filterPeriodo.value === '' || curso.periodo === filterPeriodo.value
          
          return matchesSearch && matchesPeriodo
        })
      }
      
      return {
        cursos,
        filteredCursos,
        searchQuery,
        filterPeriodo,
        filterCursos
      }
    }
  }
  </script>
  
  <style scoped>
  .cursos-docente {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1 {
    margin-bottom: 30px;
    color: #333;
  }
  
  .filters {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;
  }
  
  .search-bar {
    flex: 1;
  }
  
  input, select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
  }
  
  .cursos-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
  }
  
  .curso-card {
    background-color: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .curso-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  }
  
  .curso-header {
    padding: 15px;
    background-color: #f5f5f5;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .curso-header h3 {
    margin: 0;
    font-size: 1.2rem;
  }
  
  .curso-codigo {
    font-weight: 500;
    color: #555;
  }
  
  .curso-info {
    padding: 15px;
  }
  
  .curso-info p {
    margin: 8px 0;
  }
  
  .curso-actions {
    padding: 15px;
    border-top: 1px solid #eee;
    display: flex;
    gap: 10px;
  }
  
  .btn-primary, .btn-secondary {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
  }
  
  .btn-primary {
    background-color: #1976d2;
    color: white;
  }
  
  .btn-secondary {
    background-color: #f5f5f5;
    color: #333;
  }
  
  .no-courses {
    grid-column: 1 / -1;
    text-align: center;
    padding: 30px;
    background-color: #f9f9f9;
    border-radius: 8px;
    color: #666;
  }
  </style>