import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    isLoggedIn: false,
    token: null,
    username: null
  },
  mutations: {
    initialiseStore (state) {
      if (localStorage.getItem('token')) {
        state.isLoggedIn = true
        state.token = localStorage.getItem('token')
        state.username = localStorage.getItem('username')
      }
    },
    login (state, payload) {
      state.isLoggedIn = true
      state.token = payload.token
      state.username = payload.username
      localStorage.setItem('token', state.token)
      localStorage.setItem('username', state.username)
    },
    logout (state) {
      state.isLoggedIn = false
      localStorage.removeItem('token')
      localStorage.removeItem('username')
    }
  }
})

export default store
