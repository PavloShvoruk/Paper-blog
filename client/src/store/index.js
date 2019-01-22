import Vue from 'vue'
import Vuex from 'vuex'
import articles from './modules/articles'
import categories from './modules/categories'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    articles,
    categories
  },
  strict: process.env.NODE_ENV !== 'production'
})
