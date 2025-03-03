<template>
    <div class="cursos-container">
      <h1>Gestión de Cursos</h1>
      
      <div class="actions-bar">
        <div>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Buscar curso..." 
            class="search-input"
          />
          <select v-model="filterStatus" class="filter-select">
            <option value="">Todos los estados</option>
            <option value="active">Activo</option>
            <option value="inactive">Inactivo</option>
          </select>
        </div>
        <button @click="showAddCourseForm = true" class="add-button">Agregar Curso</button>
      </div>
      
      <div class="courses-table-container">
        <table class="courses-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Código</th>
              <th>Docente</th>
              <th>Créditos</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="course in filteredCourses" :key="course.id">
              <td>{{ course.id }}</td>
              <td>{{ course.name }}</td>
              <td>{{ course.code }}</td>
              <td>{{ course.teacher }}</td>
              <td>{{ course.credits }}</td>
              <td>
                <span :class="'status-badge ' + (course.active ? 'active' : 'inactive')">
                  {{ course.active ? 'Activo' : 'Inactivo' }}
                </span>
              </td>
              <td class="actions-cell">
                <button @click="editCourse(course)" class="action-button edit">Editar</button>
                <button @click="toggleCourseStatus(course)" class="action-button toggle">
                  {{ course.active ? 'Desactivar' : 'Activar' }}
                </button>
                <button @click="showStudents(course)" class="action-button view">Estudiantes</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminCursos',
    data() {
      return {
        courses: [
          { id: 1, name: 'Cálculo Diferencial', code: 'MAT101', teacher: 'Juan Pérez', credits: 4, active: true },
          { id: 2, name: 'Álgebra Lineal', code: 'MAT102', teacher: 'María Rodríguez', credits: 3, active: true },
          { id: 3, name: 'Programación I', code: 'INF101', teacher: 'Carlos González', credits: 5, active: true },
          { id: 4, name: 'Física I', code: 'FIS101', teacher: 'Juan Pérez', credits: 4, active: false },
        ],
        searchQuery: '',
        filterStatus: '',
        showAddCourseForm: false,
      };
    },
    computed: {
      filteredCourses() {
        return this.courses.filter(course => {
          const matchesSearch = course.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                               course.code.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                               course.teacher.toLowerCase().includes(this.searchQuery.toLowerCase());
          const matchesStatus = this.filterStatus ? 
                               (this.filterStatus === 'active' ? course.active : !course.active) : 
                               true;
          return matchesSearch && matchesStatus;
        });
      }
    },
    methods: {
      editCourse(course) {
        console.log("Editar", course);
      },
      toggleCourseStatus(course) {
        course.active = !course.active;
      },
      showStudents(course) {
        console.log("Ver estudiantes de", course);
      }
    }
  };
  </script>
  
  <style scoped>
  .cursos-container {
    padding: 24px;
  }
  
  h1 {
    margin-bottom: 24px;
    font-size: 24px;
  }
  
  .actions-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  
  .search-input {
    padding: 8px;
    margin-right: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .filter-select {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .add-button {
    padding: 8px 12px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .courses-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .courses-table th, .courses-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .status-badge.active {
    background-color: #28a745;
    color: white;
  }
  
  .status-badge.inactive {
    background-color: #dc3545;
    color: white;
  }
  
  .actions-cell {
    display: flex;
    gap: 8px;
  }
  
  .action-button {
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .edit {
    background-color: #007bff;
    color: white;
  }
  
  .toggle {
    background-color: #ffc107;
    color: black;
  }
  
  .view {
    background-color: #17a2b8;
    color: white;
  }
  </style>
  