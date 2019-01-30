import axios from "axios";
import qs from "qs";
class ApiService {
  static getCategories() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get("categories/", {
          useCache: true
        });
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error.message);
      }
    });
  }
  static getArticles() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get("articles/", {
          useCache: true
        });
        const data = res.data.data.data;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    });
  }

  static createToken({
    username,
    password
  }) {
    return axios.post(
      "auth/token/create/",
      qs.stringify({
        username,
        password
      }), {
        "content-type": "application/x-www-form-urlencoded"
      }
    );
  }

  static getUser() {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await axios.get("auth/me");
        const data = res.data.data.attributes.username;
        resolve(data);
      } catch (error) {
        reject(error);
      }
    });
  }
}

export default ApiService;
