<template>
    <div class="login-container">
      <div class="login-form">
        <h2>Iniciar Sesión</h2>
        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <label>ID Usuario:</label>
            <input 
              type="text" 
              v-model="credentials.id_usuario" 
              required
            />
          </div>
          <div class="form-group">
            <label>Contraseña:</label>
            <input 
              type="password" 
              v-model="credentials.password" 
              required
            />
          </div>
          <div class="form-group">
            <label>Rol:</label>
            <select v-model="credentials.rol" required>
              <option value="Administrador">Administrador</option>
              <option value="Docente">Docente</option>
              <option value="Estudiante">Estudiante</option>
            </select>
          </div>
          <button type="submit">Iniciar Sesión</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/axios';
  
  export default {
    name: 'LoginComponent',
    data() {
      return {
        credentials: {
          id_usuario: '',
          password: '',
          rol: ''
        }
      }
    },
    methods: {
      async handleLogin() {
        try {
          const response = await axios.post('/api/usuarios/login/', this.credentials);
          localStorage.setItem('token', response.data.token);
          localStorage.setItem('userRole', this.credentials.rol);
          
          // Redirigir según el rol
          switch(this.credentials.rol) {
            case 'Administrador':
              this.$router.push('/admin');
              break;
            case 'Docente':
              this.$router.push('/docente');
              break;
            case 'Estudiante':
              this.$router.push('/estudiante');
              break;
          }
        } catch (error) {
          console.error('Error de inicio de sesión:', error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .login-form {
    width: 300px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  input, select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>