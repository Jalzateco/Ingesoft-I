import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/Login.vue'

// Admin views
import AdminDashboard from '@/views/admin/Dashboard.vue'
import AdminUsuarios from '@/views/admin/Usuarios.vue'
import AdminCursos from '@/views/admin/Cursos.vue'

// Docente views
import DocenteDashboard from '@/views/docente/Dashboard.vue'
import DocenteCursos from '@/views/docente/Cursos.vue'
import DocenteCalificaciones from '@/views/docente/Calificaciones.vue'

// Estudiante views
import EstudianteDashboard from '@/views/estudiante/Dashboard.vue'
import EstudianteCursos from '@/views/estudiante/Cursos.vue'
import EstudianteCalificaciones from '@/views/estudiante/Calificaciones.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  // Rutas de Administrador
  {
    path: '/admin/dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, role: 'admin' }
  },
  {
    path: '/admin/usuarios',
    name: 'AdminUsuarios',
    component: AdminUsuarios,
    meta: { requiresAuth: true, role: 'admin' }
  },
  {
    path: '/admin/cursos',
    name: 'AdminCursos',
    component: AdminCursos,
    meta: { requiresAuth: true, role: 'admin' }
  },
  // Rutas de Docente
  {
    path: '/docente/dashboard',
    name: 'DocenteDashboard',
    component: DocenteDashboard,
    meta: { requiresAuth: true, role: 'docente' }
  },
  {
    path: '/docente/cursos',
    name: 'DocenteCursos',
    component: DocenteCursos,
    meta: { requiresAuth: true, role: 'docente' }
  },
  {
    path: '/docente/calificaciones',
    name: 'DocenteCalificaciones',
    component: DocenteCalificaciones,
    meta: { requiresAuth: true, role: 'docente' }
  },
  // Rutas de Estudiante
  {
    path: '/estudiante/dashboard',
    name: 'EstudianteDashboard',
    component: EstudianteDashboard,
    meta: { requiresAuth: true, role: 'estudiante' }
  },
  {
    path: '/estudiante/cursos',
    name: 'EstudianteCursos',
    component: EstudianteCursos,
    meta: { requiresAuth: true, role: 'estudiante' }
  },
  {
    path: '/estudiante/calificaciones',
    name: 'EstudianteCalificaciones',
    component: EstudianteCalificaciones,
    meta: { requiresAuth: true, role: 'estudiante' }
  },
  // Ruta por defecto (404)
  {
    path: '*',
    redirect: '/'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// Guardia de navegación
router.beforeEach((to, from, next) => {
  // Verificar si la ruta requiere autenticación
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const userData = JSON.parse(localStorage.getItem('user') || '{}');
    const isLoggedIn = !!userData.username;
    const userRole = userData.role || '';
    
    // Si no está logueado, redirigir al login
    if (!isLoggedIn) {
      next('/');
    } 
    // Si está logueado pero intenta acceder a una ruta que no corresponde a su rol
    else if (to.meta.role && to.meta.role !== userRole) {
      next(`/${userRole}/dashboard`);
    } 
    // Si todo está bien, permite la navegación
    else {
      next();
    }
  } else {
    // Si la ruta no requiere autenticación, permitir
    next();
  }
})

export default router