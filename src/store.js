import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const userModule = {
  namespaced: true,
  state: {
    username: '',
    loggedIn: false
  },
  mutations: {
    // set, clear など短いメソッド名で？
    set (state, payload) {
      state.username = payload.user.username
      state.loggedIn = true
    },
    clear (state) {
      state.username = ''
      state.loggedIn = false
    }
  }
}

const messageModule = {
  namespaced: true,
  state: {
    error: '',
    warnings: [],
    info: ''
  },
  mutations: {
    set (state, payload) {
      if (payload.error) {
        state.error = payload.error
        state.warnings = []
        state.info = ''
      } else if (payload.warnings) {
        state.error = ''
        state.warnings = payload.warnings
        state.info = ''
      } else if (payload.info) {
        state.error = ''
        state.warnings = []
        state.info = payload.info
      }
    },
    clear (state) {
      state.error = ''
      state.warnings = []
      state.info = ''
    }
  }
}

const store = new Vuex.Store({
  modules: {
    user: userModule,
    message: messageModule
  }
})

export default store
