import Axios from "axios";
const url = 'http://127.0.0.1:8000/api/categories/';

const state = {
  categories: []
}

const getters = {
  CATEGORIES: state => {
    return state.categories;
  }
};

const mutations = {
  SET_CATEGORIES: (state, payload) => {
    state.categories = payload;
  }
};

const actions = {
  GET_CATEGORIES: async (context, payload) => {
    const res = await Axios.get(url);
    const data = res.data.data.data;
    context.commit('SET_CATEGORIES', data);
  }
};


export default {
  state,
  getters,
  mutations,
  actions,
}
