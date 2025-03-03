<template>
    <div class="docente-dashboard">
      <nav class="docente-nav">
        <h1>Panel de Docente</h1>
        <div class="user-info">
          <span>{{ userData.nombre }}</span>
          <button @click="logout">Cerrar Sesión</button>
        </div>
      </nav>
  
      <div class="docente-content">
        <div class="tabs">
          <button 
            :class="{ active: activeTab === 'examenes' }"
            @click="activeTab = 'examenes'"
          >
            Exámenes
          </button>
          <button 
            :class="{ active: activeTab === 'preguntas' }"
            @click="activeTab = 'preguntas'"
          >
            Preguntas
          </button>
        </div>
  
        <div v-if="activeTab === 'examenes'">
          <ExamenComponent />
        </div>
        
        <div v-if="activeTab === 'preguntas'">
          <PreguntaComponent />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import ExamenComponent from '@/components/ExamenComponent.vue';
  import PreguntaComponent from '@/components/PreguntaComponent.vue';
  
  export default {
    name: 'DocenteView',
    components: {
      ExamenComponent,
      PreguntaComponent
    },
    data() {
      return {
        userData: {
          nombre: 'Docente'
        },
        activeTab: 'examenes'
      }
    },
    methods: {
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('userRole');
        this.$router.push('/');
      }
    }
  }
  </script>
  
  <style scoped>
  .docente-dashboard {
    padding: 20px;
  }
  
  .docente-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f5f5f5;
  }
  
  .tabs {
    margin-bottom: 20px;
  }
  
  .tabs button {
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    background-color: #f0f0f0;
    cursor: pointer;
  }
  
  .tabs button.active {
    background-color: #007bff;
    color: white;
  }
  
  .docente-content {
    padding: 20px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  </style>