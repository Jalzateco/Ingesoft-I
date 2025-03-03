import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      state.isAuthenticated = !!user;
    },
    logout(state) {
      state.user = null;
      state.isAuthenticated = false;
    }
  },
  actions: {
    login({ commit }, user) {
      // Aquí irían las llamadas a la API para autenticar al usuario
      commit('setUser', user);
      localStorage.setItem('user', JSON.stringify(user));
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('user');
    },
    initAuth({ commit }) {
      const user = JSON.parse(localStorage.getItem('user') || 'null');
      if (user) {
        commit('setUser', user);
      }
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    currentUser: state => state.user,
    userRole: state => state.user ? state.user.role : null
  }
})