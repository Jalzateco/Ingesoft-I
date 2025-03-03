<template>
    <div class="usuarios-container">
      <h1>Gestión de Usuarios</h1>
      
      <div class="actions-bar">
        <div>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Buscar usuario..." 
            class="search-input"
          />
          <select v-model="filterRole" class="filter-select">
            <option value="">Todos los roles</option>
            <option value="admin">Administrador</option>
            <option value="docente">Docente</option>
            <option value="estudiante">Estudiante</option>
          </select>
        </div>
        <button @click="showAddUserForm = true" class="add-button">Agregar Usuario</button>
      </div>
      
      <div class="users-table-container">
        <table class="users-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Email</th>
              <th>Rol</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in filteredUsers" :key="user.id">
              <td>{{ user.id }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td>
                <span :class="'role-badge ' + user.role">{{ 
                  user.role === 'admin' ? 'Administrador' : 
                  user.role === 'docente' ? 'Docente' : 'Estudiante'
                }}</span>
              </td>
              <td>
                <span :class="'status-badge ' + (user.active ? 'active' : 'inactive')">
                  {{ user.active ? 'Activo' : 'Inactivo' }}
                </span>
              </td>
              <td class="actions-cell">
                <button @click="editUser(user)" class="action-button edit">Editar</button>
                <button @click="toggleUserStatus(user)" class="action-button toggle">
                  {{ user.active ? 'Desactivar' : 'Activar' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- Modal para agregar/editar usuario -->
      <div v-if="showAddUserForm || editingUser" class="modal-overlay">
        <div class="modal">
          <h2>{{ editingUser ? 'Editar Usuario' : 'Agregar Usuario' }}</h2>
          <form @submit.prevent="saveUser">
            <div class="form-group">
              <label for="userName">Nombre:</label>
              <input type="text" id="userName" v-model="userForm.name" required />
            </div>
            <div class="form-group">
              <label for="userEmail">Email:</label>
              <input type="email" id="userEmail" v-model="userForm.email" required />
            </div>
            <div class="form-group">
              <label for="userRole">Rol:</label>
              <select id="userRole" v-model="userForm.role" required>
                <option value="admin">Administrador</option>
                <option value="docente">Docente</option>
                <option value="estudiante">Estudiante</option>
              </select>
            </div>
            <div class="form-group" v-if="!editingUser">
              <label for="userPassword">Contraseña:</label>
              <input type="password" id="userPassword" v-model="userForm.password" required />
            </div>
            <div class="form-group">
              <label for="userActive">Estado:</label>
              <select id="userActive" v-model="userForm.active">
                <option :value="true">Activo</option>
                <option :value="false">Inactivo</option>
              </select>
            </div>
            <div class="form-actions">
              <button type="button" @click="closeForm" class="cancel-button">Cancelar</button>
              <button type="submit" class="save-button">Guardar</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminUsuarios',
    data() {
      return {
        users: [
          { id: 1, name: 'Admin User', email: 'admin@example.com', role: 'admin', active: true },
          { id: 2, name: 'Juan Pérez', email: 'jperez@example.com', role: 'docente', active: true },
          { id: 3, name: 'María Rodríguez', email: 'mrodriguez@example.com', role: 'docente', active: true },
          { id: 4, name: 'Carlos González', email: 'cgonzalez@example.com', role: 'estudiante', active: true },
          { id: 5, name: 'Ana López', email: 'alopez@example.com', role: 'estudiante', active: false },
        ],
        searchQuery: '',
        filterRole: '',
        showAddUserForm: false,
        editingUser: null,
        userForm: {
          name: '',
          email: '',
          role: 'estudiante',
          password: '',
          active: true
        }
      };
    },
    computed: {
      filteredUsers() {
        return this.users.filter(user => {
          const matchesSearch = user.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                              user.email.toLowerCase().includes(this.searchQuery.toLowerCase());
          const matchesRole = this.filterRole ? user.role === this.filterRole : true;
          return matchesSearch && matchesRole;
        });
      }
    },
    methods: {
      editUser(user) {
        this.editingUser = user;
        this.userForm = { ...user };
        delete this.userForm.password; // No editamos la contraseña
      },
      toggleUserStatus(user) {
        const index = this.users.findIndex(u => u.id === user.id);
        if (index !== -1) {
          this.users[index].active = !this.users[index].active;
        }
      },
      saveUser() {
        if (this.editingUser) {
          // Actualizar usuario existente
          const index = this.users.findIndex(u => u.id === this.editingUser.id);
          if (index !== -1) {
            this.users[index] = { ...this.userForm, id: this.editingUser.id };
          }
        } else {
          // Agregar nuevo usuario
          const newId = Math.max(0, ...this.users.map(u => u.id)) + 1;
          this.users.push({ ...this.userForm, id: newId });
        }
        this.closeForm();
      },
      closeForm() {
        this.showAddUserForm = false;
        this.editingUser = null;
        this.userForm = {
          name: '',
          email: '',
          role: 'estudiante',
          password: '',
          active: true
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .usuarios-container {
    padding: 24px;
  }
  
  h1 {
    margin-bottom: 24px;
    font-size: 24px;
  }
  
  .actions-bar {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .search-input, .filter-select {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-right: 10px;
    font-size: 14px;
  }
  
  .search-input {
    width: 250px;
  }
  
  .add-button {
    background-color: #1890ff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .users-table-container {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .users-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .users-table th, .users-table td {
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid #f0f0f0;
  }
  
  .users-table th {
    background-color: #fafafa;
    font-weight: 500;
  }
  
  .role-badge, .status-badge {
    display: inline-block;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
  }
  
  .role-badge.admin {
    background-color: #722ed1;
    color: white;
  }
  
  .role-badge.docente {
    background-color: #13c2c2;
    color: white;
  }
  
  .role-badge.estudiante {
    background-color: #1890ff;
    color: white;
  }
  
  .status-badge.active {
    background-color: #52c41a;
    color: white;
  }
  
  .status-badge.inactive {
    background-color: #f5222d;
    color: white;
  }
  
  .actions-cell {
    white-space: nowrap;
  }
  
  .action-button {
    padding: 4px 8px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
    margin-right: 8px;
  }
  
  .action-button.edit {
    background-color: #faad14;
    color: white;
  }
  
  .action-button.toggle {
    background-color: #d9d9d9;
    color: #595959;
  }
  
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal {
    width: 500px;
    background-color: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  
  .modal h2 {
    margin-top: 0;
    margin-bottom: 24px;
  }
  
  .form-group {
    margin-bottom: 16px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 500;
  }
  
  .form-group input, .form-group select {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #d9d9d9;
    border-radius: 4px;
    font-size: 14px;
  }
  
  .form-actions {
    display: flex;
    justify-content: flex-end;
    margin-top: 24px;
  }
  
  .cancel-button {
    background-color: #f0f0f0;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    margin-right: 12px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .save-button {
    background-color: #1890ff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    cursor: pointer;
    font-size: 14px;
  }
  </style>