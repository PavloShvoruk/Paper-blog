import {
  AUTH_REQUEST,
  AUTH_ERROR,
  AUTH_SUCCESS,
  AUTH_LOGOUT
} from '../actions/auth'
import {
  USER_REQUEST
} from '../actions/user'
import ApiService from '../../ApiService'
import axios from 'axios'

const state = {
  token: localStorage.getItem('user-token') || '',
  status: '',
  hasLoadedOnce: false
}

const getters = {
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
}

const actions = {
  [AUTH_REQUEST]: ({
    commit,
    dispatch
  }, user) => {
    return new Promise(async (resolve, reject) => {
      commit(AUTH_REQUEST)
      try {
        await ApiService.createToken(user)
          .then(resp => {
            localStorage.setItem('user-token', `Token ${resp.data.data.id}`)
            axios.defaults.headers.common['Authorization'] = `Token ${resp.data.data.id}`
            commit(AUTH_SUCCESS, resp)
            dispatch(USER_REQUEST)
            resolve(resp)
          })
      } catch (error) {
        commit(AUTH_ERROR, error.response.status)
        localStorage.removeItem('user-token')
        reject(error)
      }

    })
  },
  [AUTH_LOGOUT]: ({
    commit,
    dispatch
  }) => {
    return new Promise((resolve, reject) => {
      commit(AUTH_LOGOUT)
      localStorage.removeItem('user-token')
      resolve()
    })
  }
}

const mutations = {
  [AUTH_REQUEST]: (state) => {
    state.status = 'loading'
  },
  [AUTH_SUCCESS]: (state, resp) => {
    state.status = 'success'
    state.token = resp.data.data.id
    state.hasLoadedOnce = true
  },
  [AUTH_ERROR]: (state, resp) => {
    state.status = resp
    state.hasLoadedOnce = true
  },
  [AUTH_LOGOUT]: (state) => {
    state.token = ''
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
}
