<template>
    <div class="home">
      <div class="hero">
        <h1>Bienvenido al Sistema de Gestión Académica</h1>
        <p>Administra tus cursos y calificaciones de manera eficiente.</p>
        <div class="cta-buttons">
          <router-link to="/login" class="btn btn-primary">Iniciar Sesión</router-link>
        </div>
      </div>
      
      <div class="features">
        <div class="feature-card">
          <h3>Para Docentes</h3>
          <p>Gestiona tus cursos, registra asistencia y calificaciones de manera sencilla.</p>
        </div>
        <div class="feature-card">
          <h3>Para Estudiantes</h3>
          <p>Consulta tus cursos, horarios y calificaciones en un solo lugar.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomeView'
  }
  </script>
  
  <style scoped>
  .home {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .hero {
    text-align: center;
    padding: 60px 20px;
    background-color: #f5f5f5;
    border-radius: 8px;
    margin-bottom: 40px;
  }
  
  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #333;
  }
  
  .hero p {
    font-size: 1.2rem;
    color: #666;
    max-width: 700px;
    margin: 0 auto 30px;
  }
  
  .cta-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
  }
  
  .btn {
    display: inline-block;
    padding: 12px 24px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 500;
    font-size: 1rem;
    transition: background-color 0.3s;
  }
  
  .btn-primary {
    background-color: #1976d2;
    color: white;
  }
  
  .btn-primary:hover {
    background-color: #1565c0;
  }
  
  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 40px;
  }
  
  .feature-card {
    background-color: white;
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  }
  
  .feature-card h3 {
    font-size: 1.5rem;
    margin-bottom: 15px;
    color: #333;
  }
  
  .feature-card p {
    color: #666;
    line-height: 1.6;
  }
  </style>