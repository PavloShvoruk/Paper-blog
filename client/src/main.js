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
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

const token = localStorage.getItem('user-token')

if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

NProgress.configure({
  showSpinner: false
});

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'

axios.interceptors.request.use(function (config) {
  //do smth before request sent
  NProgress.start();
  return config;
}, function (error) {
  console.log(error);
  return Promise.reject(error);
});

axios.interceptors.response.use(function (response) {
  // Do something with response data
  NProgress.done();
  return response;
}, function (error) {
  // Do something with response error
  return Promise.reject(error);
});

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
