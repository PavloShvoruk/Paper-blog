import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import loginForm from '@/components/Login'
import articleDetails from '@/components/articleDetails/index'
import NProgress from 'nprogress'

Vue.use(Router)

const router = new Router({
  routes: [{
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: loginForm
    },
    {
      path: '/articles/:articleID',
      name: 'article',
      component: articleDetails
    }
  ],
  mode: 'history'
})

router.beforeResolve((to, from, next) => {
  // If this isn't an initial page load.
  if (to.name) {
    // Start the route progress bar.
    NProgress.start()
  }
  next()
})

router.afterEach((to, from) => {
  // Complete the animation of the route progress bar.
  NProgress.done()
})

export default router
