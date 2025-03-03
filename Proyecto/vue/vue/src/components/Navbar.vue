<template>
    <div class="navbar">
      <div class="navbar-logo">
        <router-link to="/">Sistema Académico</router-link>
      </div>
      <div class="navbar-links">
        <template v-if="userRole === 'admin'">
          <router-link to="/admin/dashboard">Dashboard</router-link>
          <router-link to="/admin/usuarios">Gestión de Usuarios</router-link>
          <router-link to="/admin/cursos">Gestión de Cursos</router-link>
        </template>
        <template v-else-if="userRole === 'docente'">
          <router-link to="/docente/dashboard">Dashboard</router-link>
          <router-link to="/docente/cursos">Mis Cursos</router-link>
          <router-link to="/docente/calificaciones">Calificaciones</router-link>
        </template>
        <template v-else-if="userRole === 'estudiante'">
          <router-link to="/estudiante/dashboard">Dashboard</router-link>
          <router-link to="/estudiante/cursos">Mis Cursos</router-link>
          <router-link to="/estudiante/calificaciones">Mis Calificaciones</router-link>
        </template>
      </div>
      <div class="navbar-user">
        <span>{{ username }}</span>
        <button @click="logout">Cerrar sesión</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Navbar',
    data() {
      return {
        username: '',
        userRole: ''
      };
    },
    created() {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      this.username = user.username || 'Usuario';
      this.userRole = user.role || '';
    },
    methods: {
      logout() {
        localStorage.removeItem('user');
        this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #001529;
    color: white;
    padding: 0 24px;
    height: 64px;
  }
  
  .navbar-logo a {
    color: white;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
  }
  
  .navbar-links {
    display: flex;
  }
  
  .navbar-links a {
    color: rgba(255, 255, 255, 0.65);
    text-decoration: none;
    padding: 0 16px;
    font-size: 14px;
    line-height: 64px;
    transition: color 0.3s;
  }
  
  .navbar-links a:hover {
    color: white;
  }
  
  .navbar-links a.router-link-active {
    color: white;
    border-bottom: 2px solid #1890ff;
  }
  
  .navbar-user {
    display: flex;
    align-items: center;
  }
  
  .navbar-user span {
    margin-right: 12px;
    font-size: 14px;
  }
  
  .navbar-user button {
    background-color: transparent;
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: rgba(255, 255, 255, 0.65);
    padding: 4px 12px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s;
  }
  
  .navbar-user button:hover {
    color: white;
    border-color: white;
  }
  </style>