import Vue from 'vue'
import Vuex from 'vuex'
import categories from './modules/categories'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    categories
  },
  strict: process.env.NODE_ENV !== 'production'
})
