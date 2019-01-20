import axios from 'axios';

const url = 'http://127.0.0.1:8000/api/categories/';

class ApiService {
  static getCategories() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get(url);
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    })
  }
}

export default ApiService;
