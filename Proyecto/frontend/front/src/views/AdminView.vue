<template>
    <div class="admin-dashboard">
      <nav class="admin-nav">
        <h1>Panel de Administración</h1>
        <div class="user-info">
          <span>{{ userData.nombre }}</span>
          <button @click="logout">Cerrar Sesión</button>
        </div>
      </nav>
  
      <div class="admin-content">
        <div class="admin-section">
          <h2>Gestión de Usuarios</h2>
          <div class="action-buttons">
            <button @click="showUserForm = !showUserForm">Crear Usuario</button>
            <button @click="loadUsers">Ver Usuarios</button>
          </div>
  
          <!-- Formulario de creación de usuario -->
          <div v-if="showUserForm" class="user-form">
            <input v-model="newUser.nombre" placeholder="Nombre" />
            <input v-model="newUser.id_usuario" placeholder="ID Usuario" />
            <input v-model="newUser.email" placeholder="Email" />
            <select v-model="newUser.rol">
              <option value="Docente">Docente</option>
              <option value="Estudiante">Estudiante</option>
            </select>
            <button @click="createUser">Guardar Usuario</button>
          </div>
  
          <!-- Lista de usuarios -->
          <div v-if="users.length" class="users-list">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Email</th>
                  <th>Rol</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users" :key="user.id_usuario">
                  <td>{{ user.id_usuario }}</td>
                  <td>{{ user.nombre }}</td>
                  <td>{{ user.email }}</td>
                  <td>{{ user.rol }}</td>
                  <td>
                    <button @click="editUser(user)">Editar</button>
                    <button @click="deleteUser(user.id_usuario)">Eliminar</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/axios';
  
  export default {
    name: 'AdminView',
    data() {
      return {
        userData: {
          nombre: 'Administrador'
        },
        users: [],
        showUserForm: false,
        newUser: {
          nombre: '',
          id_usuario: '',
          email: '',
          rol: 'Estudiante'
        }
      }
    },
    methods: {
      async loadUsers() {
        try {
          const response = await axios.get('/api/usuarios/');
          this.users = response.data;
        } catch (error) {
          console.error('Error cargando usuarios:', error);
        }
      },
      async createUser() {
        try {
          await axios.post('/api/usuarios/', this.newUser);
          this.loadUsers();
          this.showUserForm = false;
          this.newUser = { nombre: '', id_usuario: '', email: '', rol: 'Estudiante' };
        } catch (error) {
          console.error('Error creando usuario:', error);
        }
      },
      async deleteUser(userId) {
        if (confirm('¿Está seguro de eliminar este usuario?')) {
          try {
            await axios.delete(`/api/usuarios/${userId}/`);
            this.loadUsers();
          } catch (error) {
            console.error('Error eliminando usuario:', error);
          }
        }
      },
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('userRole');
        this.$router.push('/');
      }
    },
    created() {
      this.loadUsers();
    }
  }
  </script>
  
  <style scoped>
  .admin-dashboard {
    padding: 20px;
  }
  
  .admin-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f5f5f5;
  }
  
  .user-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-width: 400px;
    margin: 20px 0;
  }
  
  .users-list table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .users-list th, .users-list td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .action-buttons {
    margin: 20px 0;
  }
  
  button {
    margin: 0 5px;
    padding: 5px 10px;
  }
  </style>