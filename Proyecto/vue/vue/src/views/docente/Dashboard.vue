<template>
    <div class="dashboard-container">
      <h1>Panel de Docente</h1>
      
      <div class="welcome-card">
        <h2>Bienvenido, {{ teacherName }}</h2>
        <p>Desde aquí podrás gestionar tus cursos, ver tus horarios y administrar las calificaciones de tus estudiantes.</p>
      </div>
      
      <div class="stats-cards">
        <div class="stat-card">
          <h3>Mis Cursos</h3>
          <p class="stat-value">5</p>
        </div>
        <div class="stat-card">
          <h3>Total Estudiantes</h3>
          <p class="stat-value">120</p>
        </div>
        <div class="stat-card">
          <h3>Tareas Pendientes</h3>
          <p class="stat-value">15</p>
        </div>
      </div>
      
      <div class="upcoming-classes">
        <h2>Próximas Clases</h2>
        <div class="class-list">
          <div class="class-card">
            <div class="class-time">Hoy, 10:00 - 12:00</div>
            <div class="class-name">Cálculo Diferencial</div>
            <div class="class-location">Aula 305, Edificio A</div>
          </div>
          <div class="class-card">
            <div class="class-time">Hoy, 14:00 - 16:00</div>
            <div class="class-name">Álgebra Lineal</div>
            <div class="class-location">Laboratorio 2, Edificio B</div>
          </div>
          <div class="class-card">
            <div class="class-time">Mañana, 08:00 - 10:00</div>
            <div class="class-name">Estadística Básica</div>
            <div class="class-location">Aula 201, Edificio C</div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DocenteDashboard',
    data() {
      return {
        teacherName: 'Profesor'
      }
    },
    created() {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      this.teacherName = user.username || 'Profesor';
    }
  }
  </script>
  
  <style scoped>
  .dashboard-container {
    padding: 24px;
  }
  
  h1 {
    margin-bottom: 24px;
    font-size: 24px;
  }
  
  h2 {
    margin-bottom: 16px;
    font-size: 20px;
  }
  
  .welcome-card {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 24px;
  }
  
  .welcome-card h2 {
    margin-top: 0;
  }
  
  .stats-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 32px;
  }
  
  .stat-card {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .stat-card h3 {
    margin: 0 0 8px 0;
    font-size: 16px;
    color: #666;
  }
  
  .stat-value {
    font-size: 24px;
    font-weight: bold;
    margin: 0;
    color: #1890ff;
  }
  
  .upcoming-classes {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .class-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 16px;
  }
  
  .class-card {
    border-left: 4px solid #1890ff;
    background-color: #f8f8f8;
    padding: 16px;
    border-radius: 4px;
  }
  
  .class-time {
    font-size: 14px;
    color: #999;
    margin-bottom: 8px;
  }
  
  .class-name {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 4px;
  }
  
  .class-location {
    font-size: 14px;
    color: #666;
  }
  </style>