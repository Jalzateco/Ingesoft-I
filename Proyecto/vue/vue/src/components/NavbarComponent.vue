<template>
    <nav class="navbar">
      <div class="navbar-logo">
        <router-link to="/">
          <img src="@/assets/logo.png" alt="Logo" v-if="logoExists" />
          <span v-else>SISCAL</span>
        </router-link>
      </div>
      
      <div class="navbar-links">
        <template v-if="userRole === 'docente'">
          <router-link to="/docente/cursos" class="nav-link">Mis Cursos</router-link>
          <router-link to="/docente/calificaciones" class="nav-link">Calificaciones</router-link>
        </template>
        
        <template v-else-if="userRole === 'estudiante'">
          <router-link to="/estudiante/cursos" class="nav-link">Mis Cursos</router-link>
          <router-link to="/estudiante/calificaciones" class="nav-link">Mis Calificaciones</router-link>
        </template>
        
        <template v-else-if="userRole === 'admin'">
          <router-link to="/admin/users" class="nav-link">Usuarios</router-link>
          <router-link to="/admin/cursos" class="nav-link">Gestión de Cursos</router-link>
          <router-link to="/admin/reports" class="nav-link">Reportes</router-link>
        </template>
      </div>
      
      <div class="navbar-user">
        <div class="user-info" @click="toggleUserMenu">
          <img :src="userAvatar" alt="Usuario" class="user-avatar" />
          <span class="user-name">{{ userName }}</span>
          <i class="fas fa-chevron-down"></i>
        </div>
        
        <div class="user-menu" v-if="showUserMenu">
          <router-link to="/profile" class="menu-item">Mi Perfil</router-link>
          <router-link to="/settings" class="menu-item">Configuración</router-link>
          <div class="menu-divider"></div>
          <button @click="logout" class="menu-item logout">Cerrar Sesión</button>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue'
  
  export default {
    name: 'AppNavbar',
    setup() {
      const userRole = ref('docente') // Esto podría venir de un store de autenticación
      const userName = ref('Usuario Demo')
      const userAvatar = ref('/img/avatar-placeholder.png')
      const showUserMenu = ref(false)
      const logoExists = ref(false)
      
      const toggleUserMenu = () => {
        showUserMenu.value = !showUserMenu.value
      }
      
      const logout = () => {
        // Implementar lógica de cierre de sesión
        console.log('Cerrando sesión...')
        // Redireccionar a la página de login
      }
      
      // Comprobar si el logo existe
      onMounted(() => {
        const img = new Image()
        img.src = '@/assets/logo.png'
        img.onload = () => {
          logoExists.value = true
        }
      })
      
      // Cerrar menú al hacer click fuera
      onMounted(() => {
        document.addEventListener('click', (e) => {
          const userMenu = document.querySelector('.navbar-user')
          if (userMenu && !userMenu.contains(e.target) && showUserMenu.value) {
            showUserMenu.value = false
          }
        })
      })
      
      return {
        userRole,
        userName,
        userAvatar,
        showUserMenu,
        logoExists,
        toggleUserMenu,
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
    background-color: #2c3e50;
    padding: 10px 20px;
    color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .navbar-logo a {
    color: white;
    text-decoration: none;
    font-size: 1.5rem;
    font-weight: bold;
    display: flex;
    align-items: center;
  }
  
  .navbar-logo img {
    height: 40px;
    margin-right: 10px;
  }
  
  .navbar-links {
    display: flex;
    gap: 20px;
  }
  
  .nav-link {
    color: #ecf0f1;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 4px;
    transition: all 0.3s ease;
  }
  
  .nav-link:hover, .router-link-active {
    background-color: #34495e;
    color: white;
  }
  
  .navbar-user {
    position: relative;
  }
  
  .user-info {
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
  }
  
  .user-info:hover {
    background-color: #34495e;
  }
  
  .user-avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #3498db;
  }
  
  .user-menu {
    position: absolute;
    right: 0;
    top: 45px;
    background-color: white;
    border-radius: 4px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    width: 200px;
    z-index: 100;
  }
  
  .menu-item {
    display: block;
    padding: 12px 20px;
    color: #2c3e50;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }
  
  .menu-item:hover {
    background-color: #f8f9fa;
  }
  
  .menu-divider {
    height: 1px;
    background-color: #ecf0f1;
    margin: 5px 0;
  }
  
  .logout {
    color: #e74c3c;
    text-align: left;
    width: 100%;
    border: none;
    background: none;
    cursor: pointer;
    font-size: 1rem;
  }
  
  @media (max-width: 768px) {
    .navbar {
      flex-direction: column;
      padding: 10px;
    }
    
    .navbar-logo {
      margin-bottom: 10px;
    }
    
    .navbar-links {
      margin-bottom: 10px;
      width: 100%;
      justify-content: space-around;
    }
    
    .user-name {
      display: none;
    }
  }
  </style>