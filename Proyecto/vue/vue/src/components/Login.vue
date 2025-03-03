<template>
    <div class="login-container">
      <div class="login-card">
        <h2>Sistema de Gestión Académica</h2>
        <div class="form-group">
          <label for="username">Usuario:</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            placeholder="Ingrese su usuario"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Contraseña:</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="Ingrese su contraseña"
            required
          />
        </div>
        <div class="form-group">
          <label for="role">Rol:</label>
          <select id="role" v-model="selectedRole">
            <option value="">Seleccione un rol</option>
            <option value="admin">Administrador</option>
            <option value="docente">Docente</option>
            <option value="estudiante">Estudiante</option>
          </select>
        </div>
        <button @click="login" :disabled="!isFormValid">Iniciar sesión</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginComponent',
    data() {
      return {
        username: '',
        password: '',
        selectedRole: '',
        errorMessage: ''
      };
    },
    computed: {
      isFormValid() {
        return this.username && this.password && this.selectedRole;
      }
    },
    methods: {
      login() {
        if (!this.isFormValid) {
          this.errorMessage = 'Por favor complete todos los campos';
          return;
        }
        
        // Simulación de autenticación
        // En una aplicación real, aquí harías una llamada a tu API
        setTimeout(() => {
          // Almacenar información del usuario en localStorage o Vuex store
          localStorage.setItem('user', JSON.stringify({
            username: this.username,
            role: this.selectedRole
          }));
          
          // Redireccionar según el rol
          this.$router.push(`/${this.selectedRole}/dashboard`);
        }, 1000);
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f2f5;
  }
  
  .login-card {
    width: 350px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    margin-bottom: 24px;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 16px;
  }
  
  label {
    display: block;
    margin-bottom: 6px;
    font-weight: 500;
  }
  
  input, select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
  }
  
  button {
    width: 100%;
    padding: 12px;
    background-color: #1890ff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    margin-top: 16px;
  }
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  
  .error-message {
    color: #f5222d;
    margin-top: 16px;
    text-align: center;
  }
  </style>