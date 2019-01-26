import axios from 'axios';
class ApiService {
  static getCategories() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get('categories/');
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error.message);
      }
    })
  }
  static getArticles() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get('articles/');
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    })
  }

  static createToken(username, password) {
    return axios.post('auth/token/create', {
      username,
      password
    });
  }

  static getUser() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get('auth/me');
        const data = res.data.attributes.username;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    })
  }
}

export default ApiService;
