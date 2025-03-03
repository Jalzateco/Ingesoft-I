<template>
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/">Sistema Académico</router-link>
      </div>
      <div class="navbar-menu">
        <template v-if="isAuthenticated">
          <template v-if="userRole === 'docente'">
            <router-link to="/docente/cursos" class="navbar-item">Mis Cursos</router-link>
            <router-link to="/docente/calificaciones" class="navbar-item">Calificaciones</router-link>
          </template>
          <template v-else-if="userRole === 'estudiante'">
            <router-link to="/estudiante/cursos" class="navbar-item">Mis Cursos</router-link>
            <router-link to="/estudiante/calificaciones" class="navbar-item">Mis Calificaciones</router-link>
          </template>
          <a @click="logout" class="navbar-item logout">Cerrar Sesión</a>
        </template>
        <template v-else>
          <router-link to="/login" class="navbar-item">Iniciar Sesión</router-link>
        </template>
      </div>
    </nav>
  </template>
  
  <script>
  import { computed } from 'vue'
  import { useStore } from 'vuex'
  import { useRouter } from 'vue-router'
  
  export default {
    name: 'NavbarComponent',
    setup() {
      const store = useStore()
      const router = useRouter()
      
      const isAuthenticated = computed(() => store.getters.isAuthenticated)
      const userRole = computed(() => store.getters.getUserRole)
      
      const logout = () => {
        store.dispatch('logout')
        router.push('/login')
      }
      
      return {
        isAuthenticated,
        userRole,
        logout
      }
    }
  }
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    height: 60px;
    background-color: #333;
    color: white;
  }
  
  .navbar-brand a {
    color: white;
    font-size: 1.5rem;
    text-decoration: none;
    font-weight: bold;
  }
  
  .navbar-menu {
    display: flex;
    gap: 20px;
  }
  
  .navbar-item {
    color: white;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 4px;
  }
  
  .navbar-item:hover {
    background-color: #555;
  }
  
  .logout {
    cursor: pointer;
    background-color: #d32f2f;
  }
  
  .logout:hover {
    background-color: #b71c1c;
  }
  </style>