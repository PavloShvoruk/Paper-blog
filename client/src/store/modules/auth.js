// import {
//   AUTH_REQUEST,
//   AUTH_ERROR,
//   AUTH_SUCCESS,
//   AUTH_LOGOUT
// } from '../actions/auth'
// import {
//   USER_REQUEST
// } from '../actions/user'
// import ApiService from "../ApiService.js"

// const state = {
//   token: localStorage.getItem('user-token') || '',
//   status: '',
//   hasLoadedOnce: false
// }

// const getters = {
//   isAuthenticated: state => !!state.token,
//   authStatus: state => state.status,
// }

// const actions = {
//     [AUTH_REQUEST]: ({
//         commit,
//         dispatch
//       }, user) => {
//         return new Promise((resolve, reject) => {
//               commit(AUTH_REQUEST)
//               ApiService.createToken()
