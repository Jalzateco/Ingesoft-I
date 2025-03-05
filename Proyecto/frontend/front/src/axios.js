import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:8000',  // URL de tu API Django
    headers: {
        'Content-Type': 'application/json',
    }
})

// Interceptor para agregar el token a las peticiones
instance.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

// Interceptor para manejar errores de respuesta
instance.interceptors.response.use(
    response => response,
    error => {
        if (error.response && error.response.status === 401) {
            // Redirigir al login si el token expiró
            localStorage.removeItem('token')
            localStorage.removeItem('userRole')
            window.location.href = '/'
        }
        return Promise.reject(error)
    }
)

export default instance