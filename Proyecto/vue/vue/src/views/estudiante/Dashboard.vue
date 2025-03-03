<template>
    <div class="dashboard-container">
      <h1>Panel de Estudiante</h1>
      
      <div class="welcome-card">
        <h2>Bienvenido, {{ studentName }}</h2>
        <p>Desde aquí podrás ver tus cursos, consultar calificaciones y acceder a los materiales de estudio.</p>
      </div>
      
      <div class="stats-cards">
        <div class="stat-card">
          <h3>Cursos Inscritos</h3>
          <p class="stat-value">5</p>
        </div>
        <div class="stat-card">
          <h3>Promedio General</h3>
          <p class="stat-value">4.2</p>
        </div>
        <div class="stat-card">
          <h3>Tareas Pendientes</h3>
          <p class="stat-value">3</p>
        </div>
      </div>
      
      <div class="upcoming-activities">
        <h2>Próximas Actividades</h2>
        <div class="activity-list">
          <div class="activity-card">
            <div class="activity-badge exam">Examen</div>
            <div class="activity-details">
              <div class="activity-date">15 Mar - 10:00</div>
              <div class="activity-title">Examen Parcial - Cálculo Diferencial</div>
              <div class="activity-course">Prof. Martínez</div>
            </div>
          </div>
          <div class="activity-card">
            <div class="activity-badge assignment">Tarea</div>
            <div class="activity-details">
              <div class="activity-date">12 Mar - 23:59</div>
              <div class="activity-title">Ejercicios de Álgebra Lineal</div>
              <div class="activity-course">Prof. Rodríguez</div>
            </div>
          </div>
          <div class="activity-card">
            <div class="activity-badge lab">Laboratorio</div>
            <div class="activity-details">
              <div class="activity-date">14 Mar - 14:00</div>
              <div class="activity-title">Práctica 3 - Estadística</div>
              <div class="activity-course">Prof. González</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EstudianteDashboard',
    data() {
      return {
        studentName: 'Estudiante'
      }
    },
    created() {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      this.studentName = user.username || 'Estudiante';
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
  
  .upcoming-activities {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .activity-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  
  .activity-card {
    display: flex;
    background-color: #f8f8f8;
    border-radius: 4px;
    overflow: hidden;
  }
  
  .activity-badge {
    width: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    font-size: 12px;
    font-weight: bold;
    color: white;
    padding: 12px 4px;
  }
  
  .activity-badge.exam {
    background-color: #f5222d;
  }
  
  .activity-badge.assignment {
    background-color: #1890ff;
  }
  
  .activity-badge.lab {
    background-color: #52c41a;
  }
  
  .activity-details {
    padding: 16px;
    flex-grow: 1;
  }
  
  .activity-date {
    font-size: 12px;
    color: #999;
    margin-bottom: 8px;
  }
  
  .activity-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 4px;
  }
  
  .activity-course {
    font-size: 14px;
    color: #666;
  }
  </style>