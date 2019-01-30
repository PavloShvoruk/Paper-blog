// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import {
  store
} from './store'
import axios from 'axios'
import {
  cacheAdapterEnhancer
} from "axios-extensions";
import router from './router'
import './assets/paper.min.css'

const token = localStorage.getItem('user-token')

if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'

axios.defaults.adapter = cacheAdapterEnhancer(axios.defaults.adapter, {
  enabledByDefault: false,
  cacheFlag: "useCache"
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
