import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// Otros imports que puedas tener...

const app = createApp(App)
app.use(router)
// Otros plugins que puedas tener...

app.mount('#app')