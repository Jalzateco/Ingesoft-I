<template>
  <div id="app">
    <nav v-if="isLoggedIn">
      <button @click="logout">Cerrar Sesión</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token')
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('userRole')
      this.$router.push('/')
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
}

nav {
  padding: 1rem;
  text-align: right;
}

button {
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>  