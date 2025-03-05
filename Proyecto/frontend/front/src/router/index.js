import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('@/components/LoginComponent.vue')
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('@/views/AdminView.vue'),
    meta: { requiresAuth: true, role: 'Administrador' }
  },
  {
    path: '/docente',
    name: 'Docente',
    component: () => import('@/views/DocenteView.vue'),
    meta: { requiresAuth: true, role: 'Docente' }
  },
  {
    path: '/estudiante',
    name: 'Estudiante',
    component: () => import('@/views/EstudianteView.vue'),
    meta: { requiresAuth: true, role: 'Estudiante' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router