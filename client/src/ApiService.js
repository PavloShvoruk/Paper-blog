import axios from 'axios';
class ApiService {
  static getCategories() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get('categories/');
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    })
  }
}

export default ApiService;
