<template>
    <div class="dashboard-container">
      <h1>Panel de Administración</h1>
      
      <div class="stats-cards">
        <div class="stat-card">
          <h3>Usuarios Totales</h3>
          <p class="stat-value">120</p>
        </div>
        <div class="stat-card">
          <h3>Docentes</h3>
          <p class="stat-value">30</p>
        </div>
        <div class="stat-card">
          <h3>Estudiantes</h3>
          <p class="stat-value">85</p>
        </div>
        <div class="stat-card">
          <h3>Cursos Activos</h3>
          <p class="stat-value">25</p>
        </div>
      </div>
      
      <div class="recent-activity">
        <h2>Actividad Reciente</h2>
        <ul class="activity-list">
          <li>
            <span class="activity-time">Hoy, 10:23 AM</span>
            <span class="activity-text">Nuevo usuario registrado: Juan Pérez (Estudiante)</span>
          </li>
          <li>
            <span class="activity-time">Ayer, 3:45 PM</span>
            <span class="activity-text">Curso "Matemáticas Avanzadas" creado por Prof. Martínez</span>
          </li>
          <li>
            <span class="activity-time">12/03/2023, 9:30 AM</span>
            <span class="activity-text">Usuario modificado: Carlos Rodríguez (Docente)</span>
          </li>
          <li>
            <span class="activity-time">10/03/2023, 2:15 PM</span>
            <span class="activity-text">Curso "Física I" actualizado</span>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminDashboard'
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
  
  .recent-activity {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .activity-list {
    list-style: none;
    padding: 0;
  }
  
  .activity-list li {
    padding: 12px 0;
    border-bottom: 1px solid #f0f0f0;
    display: flex;
    flex-direction: column;
  }
  
  .activity-list li:last-child {
    border-bottom: none;
  }
  
  .activity-time {
    color: #999;
    font-size: 12px;
    margin-bottom: 4px;
  }
  
  .activity-text {
    font-size: 14px;
  }
  </style>